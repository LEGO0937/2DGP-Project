import game_framework
import main_game
import how
from pico2d import *

name = "TitleState"

image = None

def enter():
    global image,bgm
    image = load_image('메인화면수정.png')

def exit():
    global image
    del(image)

def handle_events(frame_time):
    global x,y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_game)

        if event.type == SDL_MOUSEMOTION:
            x,y = event.x, 600 - event.y
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if 590< x and x <870 and 480<y and y<540:
                game_framework.change_state(main_game)
            if 590< x and x <870 and 380<y and y<440:
                game_framework.change_state(how)
def draw(frame_time):
    clear_canvas()
    image.draw(450,300)
    update_canvas()

def update(frame_time):
    show_cursor()

def pause():
    pass

def resume():
    pass





