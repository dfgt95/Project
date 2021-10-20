from pico2d import *
import gfw
import random
from stick import Stick

Genertate_time = 2
time = 0

def update(score, color):
    global time, Genertate_time
    time += gfw.delta_time
    if time > Genertate_time:
        generate_stick(score, color)
        time = 0
        Genertate_time -= 0.01

def generate_stick(score, color):
    x, y, dy = get_canvas_width()/2, get_canvas_height() - 75, -50
    s = Stick((x,y), dy, color)
    gfw.world.add(gfw.layer.stick, s)