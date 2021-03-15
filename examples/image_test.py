from processing_py import *

app = App(600,400) # create window: width, height
img = app.loadImage('C:\\Users\\Faruk\\Desktop\\code\\processing_py\\processing_py\\examples\\laDefense.png')
app.background(0,0,0) # set background:  red, green, blue
app.image(img,100,100,400,200)
app.redraw() # refresh the window