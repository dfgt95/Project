from pico2d import *
import gfw

def init():
    global logo_button, trigon
    logo_button = gfw.image.load('res/Logo.png')
    trigon = gfw.image.load('res/Trigon_logo.png')
 
 
def draw():
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    logo_button.draw(x, y+200)
    trigon.draw(x, y)

def update():
    pass
