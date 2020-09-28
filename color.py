import colorsys
from processing_py.constants import *

color_mode = RGB

class Color:
    
    def __init__(self,*args):
        if color_mode == RGB and len(args) == 4:
            self.red = args[0]
            self.green = args[1]
            self.blue = args[2]
            self.alpha = args[3]
        
        if color_mode == RGB and len(args) == 3:
            self.red = args[0]
            self.green = args[1]
            self.blue = args[2]
            self.alpha = 0
        
        if color_mode == RGB and len(args) == 2:
            self.red = args[0]
            self.green = args[0]
            self.blue = args[0]
            self.alpha = args[1]
        
        if color_mode == RGB and len(args) == 1:
            self.red = args[0]
            self.green = args[0]
            self.blue = args[0]
            self.alpha = 0
        
        if color_mode == HSB and len(args) == 2:
            self.hue = args[0]
            self.saturation = args[1]
            self.value = args[2]
            self.alpha = 0
    
    def parameters(self):
        if color_mode == RGB:
            return self.red, self.green, self.blue, self.alpha
        if color_mode == HSB:
            return self.hue, self.saturation, self.value, self.alpha
    
def color(*args):
    return Color(*args)

def alpha(color):
    return color.alpha

def red(color):
    if color_mode == RGB:
        return color.red
    else:
        r,g,b = colorsys.hsv_to_rgb(color.hue/255.0, color.saturation/255.0, color.value/255.0)
        return r*255

def green(color):
    if color_mode == RGB:
        return color.green
    else:
        r,g,b = colorsys.hsv_to_rgb(color.hue/255.0, color.saturation/255.0, color.value/255.0)
        return g*255

def blue(color):
    if color_mode == RGB:
        return color.blue
    else:
        r,g,b = colorsys.hsv_to_rgb(color.hue/255.0, color.saturation/255.0, color.value/255.0)
        return b*255

def saturation(color):
    if color_mode == HSB:
        return color.saturation
    else:
        h,s,v = colorsys.rgb_to_hsv(color.red/255.0, color.green/255.0, color.blue/255.0)
        return s*255
    
def brightness(color):
    if color_mode == HSB:
        return color.value
    else:
        h,s,v = colorsys.rgb_to_hsv(color.red/255.0, color.green/255.0, color.blue/255.0)
        return v*255

def hue(color):
    if color_mode == HSB:
        return color.hue
    else:
        h,s,v = colorsys.rgb_to_hsv(color.red/255.0, color.green/255.0, color.blue/255.0)
        return h*255

