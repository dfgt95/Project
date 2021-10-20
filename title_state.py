from pico2d import *
import gfw
import bg
import button
import logo
import game_state
import score_state

def enter():
    gfw.world.init(['bg', 'button', 'logo', 'ui'])

    bg.init()
    gfw.world.add(gfw.layer.bg, bg)

    button.init()
    gfw.world.add(gfw.layer.button, button)

    logo.init()
    gfw.world.add(gfw.layer.logo, logo)
    

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    global target
    
    target = e.x, e.y
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    elif e.type == SDL_MOUSEBUTTONDOWN:
        target = e.x, get_canvas_height() - 1 - e.y
        print(target)
        if get_canvas_width() // 2 - 50 <= e.x <= get_canvas_width() // 2 + 50:
            if 133 <= get_canvas_height() - 1 - e.y <= 167:
                gfw.change(game_state)
            elif 83 <= get_canvas_height() - 1 - e.y <= 117:
                gfw.push(score_state)

def exit():
    pass

def pause():
    pass

def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()