class Color:
    
    def __init__(self,red,green,blue,alpha=0):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

def color(red,green,blue,alpha=0):
    return Color(red,green,blue,alpha)

def alpha(color):
    return color.alpha

def red(color):
    return color.red

def green(color):
    return color.green

def hue(color):
    return 0
