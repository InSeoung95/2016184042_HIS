from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()

grass = Grass()

running = True


# game main loop code

while running:
    handle_events()



    clear_canvas()
    grass.draw()

    update_canvas()

    delay(0.05)
# finalization code