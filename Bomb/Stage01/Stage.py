from pico2d import *
#클래스 정의
class Stage:
    def __init__(self):
        self.image = load_image('map_flopy_tile2.png')

    def draw(self):
        self.image.draw(10, 10)
    pass

# 초기화
global running
stage = Stage()

running = True

# 반복구간
while running:
    stage.draw()
