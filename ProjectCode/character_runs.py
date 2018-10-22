from pico2d import *
from time import sleep

import random

#name = "MainState"
POKE_WIDTH, POKE_HEIGHT = 900, 600

open_canvas(POKE_WIDTH, POKE_HEIGHT)

class BackGround1:
    image = None
    def __init__(self):
        if BackGround1.image == None:
            BackGround1.image = load_image('스테이지1.png')
        self.back1_x = 450

    def update(self):
        self.back1_x -= 10
        if self.back1_x <= -450:
            self.back1_x = 1350

    def draw(self):
        self.image.draw(self.back1_x, 300)

class BackGround2:
    image = None
    def __init__(self):
        if BackGround2.image == None:
            BackGround2.image = load_image('스테이지1.png')
        self.back2_x = 1350

    def update(self):
        self.back2_x -= 10
        if self.back2_x <= -450:
            self.back2_x = 1350

    def draw(self):
        self.image.draw(self.back2_x, 300)

class Weapone:
    def __init__(self):
        self.Wx = 0
        self.Wy = 0
        self.state = False

class Char:

    PIXEL_PER_METER = (13.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    Char_image = None
    Char_attack_image = None
    Char_weapone_image = None

    def __init__(self):
        self.x = 50
        self.y = 300
        self.count = 0
        self.diecount = 5
        self.weapon = [Weapone() for i in range(20)]
        self.frame = 0
        self.framea = 0
        self.righton = False
        self.lefton = False
        self.upon = False
        self.downon = False
        self.state = False
        self.attstate = False

        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1

        if Char.image == None:
            Char.image = load_image('jiwoo.png')
       #if Char.attack_image == None:#
       #    Char.attack_image = load_image('throw.png')
        if Char.weapone_image == None:
            Char.weapone_image = load_image('무기.png')

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                Char.righton = True
            elif event.key == SDLK_LEFT:
                Char.lefton = True
            elif event.key == SDLK_UP:
                Char.upon = True
            elif event.key == SDLK_DOWN:
                Char.downon = True
            elif event.key == SDLK_a and Char.attstate == False:
               Char.state = True
               Char.attstate = True
               Char.weap[Char.count].state = True
               Char.weap[Char.couCharnt].xx = Char.x + 30
               Char.weap[Char.count].yy = Char.Chary
               Char.count += 1
               if (Char.count >= 20):
                    Char.count = 0

        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                Char.righton = False
            elif event.key == SDLK_LEFT:
                Char.lefton = False
            elif event.key == SDLK_UP:
                Char.upon = False
            elif event.key == SDLK_DOWN:
                Char.downon = False
            elif event.key == SDLK_a:
                Char.state = False
                Char.weap[Char.count].state = False

    def update(self, frame_time):

        self.frame += int(self.total_frames) % 8
        self.framea += int(self.total_frames) % 5
        self.life_time += frame_time
        distance = Char.RUN_SPEED_PPS * frame_time
        self.total_frames += Char.FRAMES_PER_ACTION * Char.ACTION_PER_TIME * frame_time

        if self.righton == True and self.x < 860:
            self.x += (self.dir * distance)
        if self.lefton == True and self.x > 40:
            self.x -= (self.dir * distance)
        if self.upon == True and self.y < 560:
            self.y += (self.dir * distance)
        if self.downon == True and self.y > 30:
            self.y -= (self.dir * distance)
        for i in range(20):
            if self.attstate == True:
                if self.weap[i].state == True:
                    self.weap[i].xx += (self.dir * distance*1.3)

    def draw(self):
        if self.state == True:
            self.attack_image.clip_draw((self.frame % 4) * 105, 0 , 80, 70, self.x, self.y)
        if self.state == False:
            self.image.draw(self.x, self.y)
        for i in range(20):
            if self.weap[i].state == True:
                self.weapone_image.clip_draw((self.framea % 5) * 35, 0, 25, 30, self.weap[i].xx, self.weap[i].yy)

   #def draw_bb(self):
   #    draw_rectangle(*self.get_bb())

   #def get_bb(self):
   #    return self#.x-35,self.y-20,self.x+25,self.y+30

   #def draw_aa(self,i):
   #    draw_rectangle(*self.get_aa(i))

   #def get_aa(self,i):
   #    return self.weap[i].xx-10,self.weap[i].yy-10,self.weap[i].xx-10,self.weap[i].yy+12

def draw(frame_time):
    hide_cursor()
    clear_canvas()
    BackGround1.draw()
    BackGround2.draw()
    Char.draw()

    update_canvas()
    delay(0.001)