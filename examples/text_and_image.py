from processing_py import *

app = App(1000,600)
app.colorMode(RGB)
c = color(255,0,0)
print(c.parameters())
i = 0

while(True):
    app.background(c)
    app.fill(0,255,0)
    app.ellipse(200,200,50,50)
    app.fill(0,0,255)
    app.rect(300,200,80,20)
    app.noFill()    
    app.text('lorem ipsum',200,300)
    app.ellipse(app.mouseX,app.mouseY,50,50)
    app.redraw()
    app.saveFrame('a.png')
    #print(i)
    i+=1
