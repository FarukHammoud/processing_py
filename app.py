from threading import Thread, Event
from subprocess import Popen, PIPE
from processing_py.listener import Listener
from processing_py.color import Color, color_mode
import sys
import datetime as date
import os

class App(Thread):

	def __init__(self,size_x = -1,size_y = -1):
		Thread.__init__(self)

		self.millis_ = 0
		self.mouseX = 0
		self.mouseY = 0
		self.pmouseX = 0
		self.pmouseY = 0
		self.width = size_x
		self.height = size_y
		self.key = ''

		self.isDead = Event()
		print('Starting App...',file=sys.stderr)
		os.environ['SIZE_X'] = str(size_x)
		os.environ['SIZE_Y'] = str(size_y)
		self.stream = Popen(['java','-jar','processing-py.jar','i3_jython.py'],cwd=os.path.dirname(os.path.realpath(__file__))+'/processing',stdin=PIPE, stdout=PIPE,stderr=PIPE)
		Listener(self.stream.stderr,self.isDead)
		print(self.waitAnswer())
		self.start()
	
	def waitAnswer(self):
		return self.stream.stdout.readline().decode('utf-8')

	def run(self):
		while(not self.isDead.isSet()):
			self.get_global_variables()

	def get_global_variables(self):
		try:
			file = open(os.path.dirname(os.path.realpath(__file__))+'/processing/global_variables.txt','r')
			lines = file.readlines()
			#global millis_,mouseX,mouseY,key
			self.millis_ = int(lines[0])
			self.pmouseX = self.mouseX
			self.pmouseY = self.mouseY
			self.mouseX = int(lines[1])
			self.mouseY = int(lines[2])
			self.key = str(lines[3])
			file.close()
		except BaseException as e:
			pass
			#print(e) ignoring IO errors

	def print_(self,*args):
		print(*args, file=sys.stderr)

	def millis(self):
		return self.millis_

	def sendLine(self,line):
		line += '\n'
		self.stream.stdin.write(line.encode('utf-8'))
		self.stream.stdin.flush()
		return self.waitAnswer()

	def std_function(self,name,*args):
		s = name+'('
		l = list(args)
		if len(l) > 0:
			for i in range(len(l)-1):
				s += str(l[i])
				s += ','
			s += str(l[len(l)-1])
		s += ')'
		self.sendLine(s)
	
	def colorMode(self,*args):
		color_mode = args[0] 
		self.std_function('colorMode',*args)

	def background(self,*args):
		if isinstance(args[0], Color):
			color = args[0]
			self.std_function('background',*color.parameters())
		else:
			self.std_function('background',*args)

	def ellipse(self,*args):
		self.std_function('ellipse',*args)

	def stroke(self,*args):
		if isinstance(args[0], Color):
			color = args[0]
			self.std_function('stroke',*color.parameters())
		else:
			self.std_function('stroke',*args)

	def arc(self,*args):
		self.std_function('arc',*args)

	def circle(self,*args):
		self.std_function('circle',*args)

	def rect(self,*args):
		self.std_function('rect',*args)

	def fill(self,*args):
		if isinstance(args[0], Color):
			color = args[0]
			self.std_function('fill',*color.parameters())
		else:
			self.std_function('fill',*args)

	def scale(self,*args):
		self.std_function('scale',*args)

	def translate(self,*args):
		self.std_function('translate',*args)

	def pushMatrix(self,*args):
		self.std_function('pushMatrix',*args)
	
	def applyMatrix(self,*args):
		self.std_function('applyMatrix',*args)
	
	def push(self,*args):
		self.std_function('push',*args)
	
	def pop(self,*args):
		self.std_function('pop',*args)
	
	def pushStyle(self,*args):
		self.std_function('pushStyle',*args)

	def popStyle(self,*args):
		self.std_function('popStyle',*args)

	def popMatrix(self,*args):
		self.std_function('popMatrix',*args)
	
	def box(self,*args):
		self.std_function('box',*args)
	
	def sphere(self,*args):
		self.std_function('sphere',*args)
	
	def sphereDetail(self,*args):
		self.std_function('sphereDetail',*args)

	def redraw(self,*args):
		self.std_function('redraw',*args)

	def strokeWeight(self,*args):
		self.std_function('strokeWeight',*args)
	
	def texture(self,*args):
		self.std_function('texture',*args)
	
	def textureMode(self,*args):
		self.std_function('textureMode',*args)

	def text(self,text,x,y):
		self.sendLine('text(\''+str(text)+'\','+str(x)+','+str(y)+')')
	
	def textWidth(self,*args):
		self.std_function('textWidth',*args)
	
	def textFont(self,*args):
		self.std_function('textFont',*args)
	
	def textSize(self,*args):
		self.std_function('textSize',*args)
	
	def textAlign(self,*args):
		self.std_function('textAlign',*args)
	
	def textLeading(self,*args):
		self.std_function('textLeading',*args)

	def point(self,*args):
		self.std_function('point',*args)

	def shear(self,*args):
		self.std_function('shear',*args)

	def shearX(self,*args):
		self.std_function('shearX',*args)

	def shearY(self,*args):
		self.std_function('shearY',*args)

	def rotate(self,*args):
		self.std_function('rotate',*args)

	def rotateX(self,*args):
		self.std_function('rotateX',*args)

	def rotateY(self,*args):
		self.std_function('rotateY',*args)

	def rotateZ(self,*args):
		self.std_function('rotateX',*args)

	def triangle(self,*args):
		self.std_function('triangle',*args)

	def beginShape(self,*args):
		self.std_function('beginShape',*args)
	
	def endShape(self,*args):
		self.std_function('endShape',*args)
	
	def beginContour(self,*args):
		self.std_function('beginContour',*args)
	
	def endContour(self,*args):
		self.std_function('endContour',*args)

	def shape(self,*args):
		self.std_function('shape',*args)
	
	def createShape(self,*args):
		self.std_function('createShape',*args)

	def save(self,*args):
		self.std_function('save',*args)
	
	def saveFrame(self,file_name):
		self.sendLine('saveFrame(\''+str(file_name)+'\''+')')
		
	def loadShape(self,*args):
		self.std_function('loadShape',*args)
	
	def shapeMode(self,*args):
		self.std_function('shapeMode',*args)

	def vertex(self,*args):
		self.std_function('vertex',*args)
	
	def bezierVertex(self,*args):
		self.std_function('bezierVertex',*args)
	
	def curveVertex(self,*args):
		self.std_function('curveVertex',*args)
	
	def quadraticVertex(self,*args):
		self.std_function('quadraticVertex',*args)

	def line(self,*args):
		self.std_function('line',*args)

	def quad(self,*args):
		self.std_function('quad',*args)

	def bezier(self,*args):
		self.std_function('bezier',*args)
	
	def bezierDetail(self,*args):
		self.std_function('bezierDetail',*args)
	
	def bezierPoint(self,*args):
		self.std_function('bezierPoint',*args)
	
	def bezierTangent(self,*args):
		self.std_function('bezierTangent',*args)
	
	def curve(self,*args):
		self.std_function('curve',*args)
	
	def curveDetail(self,*args):
		self.std_function('curveDetail',*args)
	
	def curvePoint(self,*args):
		self.std_function('curvePoint',*args)
	
	def curveTangent(self,*args):
		self.std_function('curveTangent',*args)
	
	def curveTightness(self,*args):
		self.std_function('curveTightness',*args)
	
	def strokeCap(self,*args):
		self.std_function('strokeCap',*args)
	
	def strokeJoin(self,*args):
		self.std_function('strokeJoin',*args)
	
	def ellipseMode(self,*args):
		self.std_function('ellipseMode',*args)
	
	def rectMode(self,*args):
		self.std_function('rectMode',*args)

	def square(self,*args):
		self.std_function('square',*args)
	
	def ambientLight(self,*args):
		self.std_function('ambientLight',*args)
	
	def directionalLight(self,*args):
		self.std_function('directionalLight',*args)
	
	def lightFalloff(self,*args):
		self.std_function('lightFalloff',*args)

	def lightSpecular(self,*args):
		self.std_function('lightSpecular',*args)	
	
	def lights(self,*args):
		self.std_function('lights',*args)
	
	def noLights(self,*args):
		self.std_function('noLights',*args)
	
	def normal(self,*args):
		self.std_function('normal',*args)
	
	def pointLight(self,*args):
		self.std_function('pointLight',*args)
	
	def spotLight(self,*args):
		self.std_function('spotLight',*args)
	
	def beginCamera(self,*args):
		self.std_function('beginCamera',*args)

	def camera(self,*args):
		self.std_function('camera',*args)
	
	def endCamera(self,*args):
		self.std_function('endCamera',*args)
	
	def frustum(self,*args):
		self.std_function('frustum',*args)
	
	def ortho(self,*args):
		self.std_function('ortho',*args)
	
	def perspective(self,*args):
		self.std_function('perspective',*args)
	
	def printCamera(self,*args):
		self.std_function('printCamera',*args)
	
	def printProjection(self,*args):
		self.std_function('printProjection',*args)

	def noFill(self):
		self.std_function('noFill')
	
	def noStroke(self):
		self.std_function('noStroke')
	
	def noSmooth(self):
		self.std_function('noSmooth')

	def noCursor(self):
		self.std_function('noCursor')
	
	def cursor(self):
		self.std_function('cursor')

	def delay(self):
		self.std_function('delay')

	def frameRate(self):
		self.std_function('frameRate')

	def smooth(self):
		self.std_function('smooth')
	
	def printMatrix(self):
		self.std_function('printMatrix')
	
	def resetMatrix(self):
		self.std_function('resetMatrix')
	
	def exit(self):
		self.std_function('exit')
		self.std_function('redraw')
		self.stream.terminate()
		self.isDead.set()
		
	def day(self):
		import datetime
		now = datetime.datetime.now()
		return now.day

	def hour(self):
		import datetime
		now = datetime.datetime.now()
		return now.hour

	def minute(self):
		import datetime
		now = datetime.datetime.now()
		return now.minute

	def month(self):
		import datetime
		now = datetime.datetime.now()
		return now.month

	def second(self):
		import datetime
		now = datetime.datetime.now()
		return now.second

	def year(self):
		import datetime
		now = datetime.datetime.now()
		return now.year





