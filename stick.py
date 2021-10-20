from pico2d import *
import gfw
import random

MOVE_PPS = 5

class Stick:
    def __init__(self, pos, dy, color):
        x, y = 0, 0
        self.pos = x, y
        self.color = color 
        self.init(pos, dy, color)
        self.height = self.image.h // 2
        self.time = get_time()

    def init(self, pos, dy, color):
        self.pos = 200, 675
        self.dy = dy
        color = random.randint(0,2)
        if color == 0:
            self.image = gfw.image.load('res/Stick_Red.png')
            self.image.color = 0
        elif color == 1:
            self.image = gfw.image.load('res/Stick_Green.png')
            self.image.color = 1
        elif color == 2:
            self.image = gfw.image.load('res/Stick_Blue.png')
            self.image.color = 2
        self.height = self.image.h // 2

    def update(self):
        x, y = self.pos
        x = x
        y += -0.5 * MOVE_PPS
        self.pos = x,y

    def draw(self):
        x, y = self.pos
        self.image.draw(x, y)