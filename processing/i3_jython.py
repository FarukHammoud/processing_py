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
    System.err.println('[Jython] Created!')
    send_echo('online')

def draw():
    listen()        

def send_variables_ack():
    println('!'+str(millis())+','+str(mouseX)+','+str(mouseY)+','+str(key)+',')

def send_echo(txt):
    println(txt)

def listen():
    while(True):
        try:
            reader = BufferedReader(InputStreamReader(System.in))
            input = str(reader.readLine())

            if input == 'redraw()':
                send_variables_ack()
                break
            else:
                send_echo(input) #echo
                exec(input)
   
        except BaseException as e :
            System.err.println(e)
  
#def exit():
#    System.err.println('[Jython] Closed.')
#    super.exit()
