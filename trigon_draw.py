from pico2d import *
import gfw
from trigon import MAX_TRIGON, Trigon

MAX_TRIGON = 1

def update(color, NUM_TRIGON):
    draw_trigon(color, NUM_TRIGON)
    

def draw_trigon(color, NUM_TRIGON):
    global pos
    x, y = get_canvas_width()/2, 100
    pos = x, y
    col = color + 3
    t1 = Trigon(pos, (col - 1) % 3, NUM_TRIGON)
    t2 = Trigon(pos, color, NUM_TRIGON)
    if NUM_TRIGON != 0: gfw.world.remove(t1)
    gfw.world.add(gfw.layer.Trigon, t2)
    NUM_TRIGON += 1

def color():
    return Trigon.color