from java.io import InputStreamReader, BufferedReader
from java.lang import System
import os

size_x = int(os.environ['SIZE_X'])
size_y = int(os.environ['SIZE_Y'])

def settings():
    if size_x == -1:
        fullScreen()
    elif size_y == -1:
        size(size_x,size_x)
    else:
        size(size_x,size_y)
    println('[Jython] Created!')


def draw():
    refresh_global_variables()
    listen()        

def refresh_global_variables():
	list_ = [str(millis()),str(mouseX),str(mouseY),str(key)]
	saveStrings("global_variables.txt", list_)

def listen():
    while(True):
        try:
            reader = BufferedReader(InputStreamReader(System.in))
            input = str(reader.readLine())
            println(input) #echo
            if input == 'redraw()':
                break
            exec(input)
        except BaseException as e :
            System.err.println(e)
  
#def exit():
#    System.err.println('[Jython] Closed.')
#    super.exit()
