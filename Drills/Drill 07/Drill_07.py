from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    pass
class Ball:
    def __init__(self):
        self.x, self.y = random.randint(10, 790), 600
        self.speed = random.randint(10, 20)
        self.size = random.randint(1, 2)
        if self.size == 1:
            self.image = load_image('ball21x21.png')
        elif self.size == 2:
            self.image = load_image('ball41x41.png')

    def update(self):
        if self.size == 1:
            if self.y <= 50:
                self.y = 50
            else:
                self.y -= self.speed
        elif self.size == 2:
            if self.y <= 50:
                self.y = 50
            else:
                self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)
    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
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
balls = [Ball() for i in range(20)]
team = [Boy() for aa in range(11)]

running = True


# game main loop code

while running:
    handle_events()

    clear_canvas()
    grass.draw()
    for ball in balls:
        ball.update()
        ball.draw()

    for boy in team:
        boy.update()
        boy.draw()

    update_canvas()

    delay(0.05)

close_canvas()
# finalization code