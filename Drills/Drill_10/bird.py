import game_framework
from pico2d import *

import game_world

PIXEL_PER_METER = (10.0 / 0.3)

BIRD_SIZE = 2

BIRD_SPEED_KMPH = 20.0
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    def __init__(self):
        self.x, self.y = 15, 400
        self.image = load_image('bird_animation.png')
        self.velocity = BIRD_SPEED_PPS
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.velocity * game_framework.frame_time

        self.x = clamp(150, self.x, 1600 - 150)
        if self.x == 1600 - 150:
            self.velocity = -BIRD_SPEED_PPS
        if self.x == 150:
            self.velocity = BIRD_SPEED_PPS

    def draw(self):
        if self.velocity > 0:
            self.image.clip_draw((int(self.frame) % 5) * 182, (2 - (int(self.frame) // 5)) * 166, 182, 166,
                                 self.x, self.y, 66,66)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * 182, (2 - (int(self.frame) // 5)) * 166, 182, 166,0, 'h', self.x, self.y, 66, 66)