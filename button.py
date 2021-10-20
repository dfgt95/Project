from pico2d import *
import gfw

def init():
    global start_button, score_button
    start_button = gfw.image.load('res/Start_Button.png')
    score_button = gfw.image.load('res/Score_Button.png')

def draw():
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    start_button.draw(x, y-200)
    score_button.draw(x, y-250)

def update():
    pass
