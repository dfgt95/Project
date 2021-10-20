from pico2d import *
import gfw
import generator
import bg
import title_state
import stick
import trigon_draw
from trigon import Trigon

def enter():
    gfw.world.init(['bg', 'stick', 'Trigon', 'ui'])

    bg.init()
    gfw.world.add(gfw.layer.bg, bg)

    global font
    font = gfw.font.load('res/ConsolaMalgun.ttf', 20)
    
    global score
    score = 0

    global color, NUM_TRIGON
    NUM_TRIGON = 1
    color = 0
    trigon_draw.update(color, NUM_TRIGON)

    global state
    state = 2

def update():
    global score
    gfw.world.update()
    generator.update(score, color)
    score = score


def draw():
    gfw.world.draw()
    score_pos = 20, get_canvas_height() - 30
    font.draw(*score_pos, 'Score: %.1f' % score, (255,255,255))

def handle_event(e):
    global color, NUM_TRIGON
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.change(title_state)
    elif e.type == SDL_MOUSEBUTTONDOWN:
        print(color, NUM_TRIGON)
        NUM_TRIGON += 1
        trigon_draw.update(color, NUM_TRIGON)
        color = (color +1) % 3
        NUM_TRIGON -= 1
           

def exit():
    global NUM_TRIGON
    NUM_TRIGON = 0

def pause():
    pass

def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()