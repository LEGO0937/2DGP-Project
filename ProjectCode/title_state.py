import game_framework
import how
from pico2d import *

name = "TitleState"

image = None

def enter():
    global main_image, press_key, frame, real_frame, bgm
    main_image = load_image('메인화면수정.png')
    press_key = load_image('press_any_button.png')
    bgm = load_music('메인테마.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    frame = 0
    real_frame = 0

def exit():
    global image
    del(image)

def handle_events(frame_time):
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(how)

        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y

def draw(frame_time):
    clear_canvas()
    main_image.draw(450, 300)
    #press_key.clip_draw((real_frame % 2) * 500, 150, 500, 150, 450, 100)
    press_key.draw(450, 100)
    update_canvas()

def update(frame_time):
    global frame, real_frame
    show_cursor()
    frame = (frame + 1)
    real_frame = frame % 100

def pause():
    pass

def resume():
    pass





