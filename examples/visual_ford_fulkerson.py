from processing_py import App, CENTER
from math import atan2, inf

class Vertex:

    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
        self.selected = False

    def show(self,app):
        app.fill(255,255,255)
        app.stroke(150,150,150)
        app.pushMatrix()
        app.translate(self.x,self.y)
        app.ellipse(0,0,50,50)
        app.popMatrix()
        app.fill(150,150,150)
        app.textSize(20)
        app.text(self.name,self.x,self.y)

class Edge():
    def __init__(self,inicial_vertex,final_vertex,flow,max_flow):
        self.inicial_vertex = inicial_vertex
        self.final_vertex = final_vertex
        self.flow = flow
        self.max_flow = max_flow
        self.selected = False

    def show(self,app):
        x0, y0 = self.inicial_vertex.x, self.inicial_vertex.y
        x1, y1 = self.final_vertex.x, self.final_vertex.y
        app.stroke(255,255,255)
        if self.selected:
            app.stroke(0,255,0)
        app.line(x0,y0,x1,y1)
        app.pushMatrix()
        app.translate((x0+x1)/2,(y0+y1)/2)
        app.rotate(atan2(y1-y0, x1-x0))
        app.fill(250,150,150)
        app.noStroke()
        app.triangle(0, 0, -10, 5, -10, -5)
        app.popMatrix()
        app.fill(150,150,250)
        app.textSize(20)
        app.textAlign(CENTER,CENTER)
        app.text(str(self.flow)+'/'+str(self.max_flow),(x0+x1)/2,(y0+y1)/2)

class FlowGraph:

    def __init__(self):
        self.V = {}
        self.E = {}

    def neighbours(self,s):
        neighbours = []
        for v in self.V:
            if (s,v) in self.E or (v,s) in self.E:
                neighbours.append(v)
        return neighbours

    def residual_neighbours(self,s):
        residual_neighbours = []
        for v in self.V:
            if (s,v) in self.E:
                if self.E[(s,v)].flow < self.E[(s,v)].max_flow:
                    residual_neighbours.append((v,self.E[(s,v)].max_flow-self.E[(s,v)].flow))
            elif (v,s) in self.E:
                if self.E[(v,s)].flow > 0:
                    residual_neighbours.append((v,self.E[(v,s)].flow))
        return residual_neighbours
    
    def unselect(self,edges_list):
        for (s,t) in edges_list:
            self.E[(s,t)].selected = False
    
    def selectPath(self,path):
        s = path[0]
        for i in range(1,len(path)):
            t = path[i]
            if (s,t) in self.E:
                self.E[(s,t)].selected = True
            if (t,s) in self.E:
                self.E[(t,s)].selected = True
            s = t
            


    def addVertices(self,*vertices):
        for vertex in vertices:
            self.V[vertex[0]] = Vertex(*vertex)

    def addEdges(self,*edges):
        for edge in edges:
            self.E[(edge[0],edge[1])] = Edge(self.V[edge[0]],self.V[edge[1]],edge[2],edge[3])

    def show(self,app):
        app.background(0,0,0)

        for edge_pair in self.E:
            edge = self.E[edge_pair]
            edge.show(app)

        for vertex_name in self.V:
            vertex = self.V[vertex_name]
            vertex.show(app)
        
        app.redraw()

    def animate(self,app):
        reached, augmenting_path, residous = self.findAugmentingPath('s','t',[])
        print(reached,augmenting_path,residous)
        while reached:
            self.selectPath(augmenting_path)
            self.show(app)
            input()
            self.improveFlow(augmenting_path,residous)
            self.show(app)
            self.unselect(self.E)
            input()
            reached, augmenting_path, residous = self.findAugmentingPath('s','t',[])
            print(reached,augmenting_path,residous)

    def improveFlow(self,augmenting_path,residous):
        s = augmenting_path[0]
        for i in range(1,len(augmenting_path)):
            t = augmenting_path[i]
            if (s,t) in self.E:
                self.E[(s,t)].flow += residous
            if (t,s) in self.E:
                self.E[(t,s)].flow -= residous
            s = t
    def findAugmentingPath(self,s,t,visited = []):
        visited.append(s)
        if s == t:
            return True, [t], inf
        for (rn,r) in self.residual_neighbours(s):
            if not rn in visited:
                reached, path, total = self.findAugmentingPath(rn,t,visited)
                if reached:
                    return True, [s] + path, min(total,r)
        return False, [], 0

app = App(800,600)

fg = FlowGraph()
fg.addVertices(('s',100,300),('t',700,300),('1',300,150),('2',500,150),('3',300,450),('4',500,450))
fg.addEdges(('s','1',11,16),('1','2',12,12),('2','t',15,20),('s','3',8,13),('3','4',11,14),('4','t',4,4),('3','1',1,4),('4','2',7,7),('2','3',4,9))
print(fg.findAugmentingPath('s','t',[]))
fg.animate(app)
