from pico2d import *

POKE_WIDTH, POKE_HEIGHT = 1200, 653


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, POKE_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(POKE_WIDTH, POKE_HEIGHT)
poke_ground = load_image('스테이지1.png')
character = load_image('jiwoo.png')

running = True
x, y = POKE_WIDTH // 2, POKE_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    poke_ground.draw(POKE_WIDTH // 2, POKE_HEIGHT // 2)
    character.clip_draw((frame * 51) + 89, 0 * 1, 51, 59, x, y) #51씩 프레임 증가
    update_canvas()
    frame = (frame + 1) % 3

    delay(0.02)
    handle_events()

close_canvas()




