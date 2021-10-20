from pico2d import *
import gfw

def init():
    global bg
    bg = gfw.image.load('res/bg.png')

def draw():
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    bg.draw(x, y)

def update():
    pass