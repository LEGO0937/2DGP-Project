import game_framework
import title_state
import main_game
from pico2d import *

name = "Char_Select"

image = None

def enter():
    global image
    image = load_image('조작법1.png')

def exit():
    pass

def update(frame_time):
   pass

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(450, 300)
    update_canvas()

def handle_events(frame_time):
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(main_game)

       # if event.type == SDL_MOUSEMOTION:
       #     x,y = event.x, 600 - event.y
       # if event.type == SDL_MOUSEBUTTONDOWN and event.button ==  SDL_BUTTON_LEFT:
       #     if 720< x and x <840 and 480<y and y<540:
       #         game_framework.change_state(avoid)
       #     if 720< x and x <840 and 40<y and y<90:
       #         game_framework.change_state(title_state)

def pause():
    pass

def resume():
    pass