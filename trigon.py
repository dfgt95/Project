from pico2d import *
import gfw
import random
import math

MAX_TRIGON = 1
NUM_TRIGON = 0

class Trigon:
    def __init__(self, pos, color, NUM_TRIGON):
        self.color = color
        self.init(pos, color, NUM_TRIGON)

    def init(self, pos, color, NUM_TRIGON):
        self.pos = get_canvas_width() // 2, 100
        self.image = gfw.image.load('res/Trigon.png')
        if color == 0:
            self.image.color = 0
        elif color == 1:
            self.image.color = 1
        elif color == 2:
            self.image.clolor = 2
        self.radius = self.image.h // 2
        NUM_TRIGON += 1

    def update(self):
        global NUM_TRIGON
        x, y = self.pos
        self.pos = x,y
        if NUM_TRIGON > MAX_TRIGON:gfw.world.remove(self)

    def color(self):
        return self.color

    def draw(self):
        global NUM_TRIGON
        if NUM_TRIGON > MAX_TRIGON:
            gfw.world.remove(self)
            NUM_TRIGON -= 1
        x, y = self.pos
        color = self.color
        if color == 0:
            self.image.rotate_draw(-math.radians(120), x, y-15, 150, 150)
        elif color == 1:
            self.image.rotate_draw(0, x-7, y, 150, 150)
        else:
            self.image.rotate_draw(math.radians(120), x-16, y-14, 150, 150)
