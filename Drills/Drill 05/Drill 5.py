from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global goal_x, goal_y
    global prev_x, prev_y
    global move_x, move_y
    global mouse_x, mouse_y
    global count

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                goal_x, goal_y = event.x, KPU_HEIGHT - 1 - event.y
                if (count == 1):
                    a = (goal_y-prev_y)/(goal_x-prev_x)
                    b = prev_y-prev_x*a

                move_x = (prev_y-b)/a
                move_y = a*prev_x + b

                prev_x, prev_y = goal_x, goal_y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass
def Player_Location():



open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse_cursor = load_image('hand_arrow.png')

running = True
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
prev_x, prev_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
move_x, move_y = prev_x, prev_y

frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, move_x, move_y)
    mouse_cursor.draw(mouse_x, mouse_y)  # 마우스 커서 표시.
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




