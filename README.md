
# Processing Python     ![](https://processing.org/favicon) 

Processing Python is a powerful and easy-to-use Graphics Library for Python based on [Processing](https://processing.org/).

It allows you to draw shapes in a window with simple functions like **rect()** or **line()**, design animations using the mouse position and much more.


## Installation


Install the processing-py package using **pip**:
```
 pip install processing-py --upgrade
```
The first time you run some code using the library, a script will automatically download the appropriate Processing-py command line tools and Java Runtime Enviromment 8u202 for you system (~120 MB). 

## How to use


```python
from processing_py import *

app = App(600,400) # create window: width, height
app.background(255,0,0) # set background:  red, green, blue
app.redraw() # refresh the window

#app.exit() # close the window

```

## Drawing


```python
from processing_py import *

app = App(600,400) # create window: width, height
app.background(0,0,0) # set background:  red, green, blue
app.fill(255,255,0) # set color for objects: red, green, blue
app.rect(100,100,200,100) # draw a rectangle: x0, y0, size_x, size_y
app.fill(0,0,255) # set color for objects: red, green, blue
app.ellipse(300,200,50,50) # draw a circle: center_x, center_y, size_x, size_y
app.redraw() # refresh the window


```
![Result:](https://i.ibb.co/hypdG2r/Untitled.png)

# Mouse & Animation

```python
from processing_py import *
app = App(600,400) # create window: width, height

while(True):
   app.background(0,0,0) # set background:  red, green, blue
   app.fill(255,255,0) # set color for objects: red, green, blue
   app.ellipse(app.mouseX,app.mouseY,50,50) # draw a circle: center_x, center_y, size_x, size_y
   app.redraw() # refresh the window

```
![Result:](https://i.ibb.co/mHJVcnn/Untitled.png)

## More functions

Explore all the possibilities in the [Processing Reference](https://processing.org/reference/).
