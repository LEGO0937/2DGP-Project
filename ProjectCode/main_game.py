from pico2d import *


import random
import game_framework
import title_state
import game_over_state
import clear_state

name = "MainState"

class Back1:
    image = None
    def __init__(self):
        if Back1.image == None:
            Back1.image = load_image('스테이지1.png')
        self.bgm = load_music('게임진행.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.back1_x = 450      #first background, 'x' location

    def update(self, frame_time):
        self.back1_x -= 2
        if self.back1_x <= -450:
            self.back1_x = 1350

    def draw(self):
        self.image.draw(self.back1_x, 300)

class Back2:
    image = None
    def __init__(self):
        if Back2.image == None:
            Back2.image = load_image('스테이지1.png')
        self.back2_x = 1350     #second background, 'x' location

    def update(self,frame_time):
        self.back2_x -= 2
        if self.back2_x <= -450:
            self.back2_x = 1350

    def draw(self):
        self.image.draw(self.back2_x, 300)

class Weapone:
    def __init__(self):
        self.xx = 0
        self.yy = 0
        self.state = False

class Item:

    image = None

    def __init__(self):
        if Item.image == None:
            Item.image = load_image('루기아 깃털.png')
        self.x = 800
        self.y = 300


    def draw(self):
            self.image.clip_draw(50, 0, 50, 50, self.x, self.y)

    def update(self):
        self.x -= random.randint(0, 10)
        self.y += random.randint(-10, 10)
        if self.x <= 0:
            self.x = random.randint(900, 2000)
            self.y = random.randint(80, 570)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

class Trainer:

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    trainer_image = None
    trainer_attack_image = None
    trainer_weapone_image = None
    trainer_item_image = None

    def __init__(self):
        self.x = 50
        self.y = 300
        self.count = 0          #트레이너 weapone count
        self.diecount = 100      #트레이너 hp
        self.weap = [Weapone() for i in range(20)]      #트레이너 weapone
        self.frame = 0    # 트레이너 frame
        self.framea = 0   # 트레이너 weapone frame
        self.righton = False
        self.lefton = False
        self.upon = False
        self.downon = False
        self.state = False  # enter 'a' key(image change)
        #self.attstate = False   # 트레이너 무기 state
        self.item = 3
        self.fire_item = False

        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1

        self.summon_assist = False

        self.god_time = 0
        self.collide = False

        if Trainer.trainer_image == None:
            Trainer.trainer_image = load_image('지우.png')
        if Trainer.trainer_attack_image == None:
            Trainer.trainer_attack_image = load_image('지우.png')
        if Trainer.trainer_weapone_image == None:
            Trainer.trainer_weapone_image = load_image('몬스터볼무기.png')


    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                trainer.righton = True
            elif event.key == SDLK_LEFT:
                trainer.lefton = True
            elif event.key == SDLK_UP:
                trainer.upon = True
            elif event.key == SDLK_DOWN:
                trainer.downon = True
            elif event.key == SDLK_a:
                trainer.weap[trainer.count].state = True
                trainer.weap[trainer.count].xx = trainer.x + 30
                trainer.weap[trainer.count].yy = trainer.y
                trainer.count += 1
                if (trainer.count >= 20):
                    trainer.count = 0
            elif event.key == SDLK_s:
                trainer.fire_item = True

        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                trainer.righton = False
            elif event.key == SDLK_LEFT:
                trainer.lefton = False
            elif event.key == SDLK_UP:
                trainer.upon = False
            elif event.key == SDLK_DOWN:
                trainer.downon = False
            elif event.key == SDLK_a:
                pass

    def update(self, frame_time):

        self.frame += int(self.total_frames) % 20
        self.framea += int(self.total_frames) % 20
        self.life_time += frame_time
        distance = trainer.RUN_SPEED_PPS * frame_time
        self.total_frames += trainer.FRAMES_PER_ACTION * trainer.ACTION_PER_TIME * frame_time

        if self.righton == True and self.x < 860:
            self.x += (self.dir * distance)
        if self.lefton == True and self.x > 40:
            self.x -= (self.dir * distance)
        if self.upon == True and self.y < 560:
            self.y += (self.dir * distance)
        if self.downon == True and self.y > 30:
            self.y -= (self.dir * distance)
        for i in range(20):
                if self.weap[i].state == True:
                    self.weap[i].xx += (self.dir * distance*1.3)

    def draw(self):
        if self.state == True:
            self.trainer_attack_image.clip_draw(((self.frame % 3) * 70), 0, 70, 70, self.x, self.y)
        if self.state == False:
            self.trainer_attack_image.clip_draw(((self.frame % 3) * 70), 0, 70, 70, self.x, self.y)
        for i in range(20):
            if self.weap[i].state == True:
                self.trainer_weapone_image.clip_draw((self.framea % 4) * 30, 0, 30, 30, self.weap[i].xx, self.weap[i].yy)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 35, self.y - 20, self.x + 25, self.y + 30

    def draw_aa(self, i):
        draw_rectangle(*self.get_aa(i))

    def get_aa(self, i):
        return self.weap[i].xx-10, self.weap[i].yy-10, self.weap[i].xx-10, self.weap[i].yy+12

class Assist:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.x = Trainer.x
        self.y = Trainer.y
        self.count = 0  # 트레이너 weapone count
        self.weap = [Weapone() for i in range(20)]  #펫의 weapone
        self.frame = 0  # 트레이너 frame
        self.framea = 0  # 트레이너 weapone frame

        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1

        self.god_time = 0
        self.collide = False

        if Trainer.trainer_image == None:
            Trainer.trainer_image = load_image('.png')
        if Trainer.trainer_attack_image == None:
            Trainer.trainer_attack_image = load_image('이슬이.png')
        if Trainer.trainer_weapone_image == None:
            Trainer.trainer_weapone_image = load_image('몬스터볼무기.png')


    def update(self, frame_time):

        self.frame += int(self.total_frames) % 20
        self.framea += int(self.total_frames) % 20
        self.life_time += frame_time
        distance = trainer.RUN_SPEED_PPS * frame_time
        self.total_frames += trainer.FRAMES_PER_ACTION * trainer.ACTION_PER_TIME * frame_time

        if self.righton == True and self.x < 860:
            self.x += (self.dir * distance)
        if self.lefton == True and self.x > 40:
            self.x -= (self.dir * distance)
        if self.upon == True and self.y < 560:
            self.y += (self.dir * distance)
        if self.downon == True and self.y > 30:
            self.y -= (self.dir * distance)
        for i in range(20):
            if self.weap[i].state == True:
                self.weap[i].xx += (self.dir * distance * 1.3)

    def draw(self):
        if self.state == True:
            self.trainer_attack_image.clip_draw(((self.frame % 3) * 70), 0, 70, 70, self.x, self.y)
        if self.state == False:
            self.trainer_attack_image.clip_draw(((self.frame % 3) * 70), 0, 70, 70, self.x, self.y)
        for i in range(20):
            if self.weap[i].state == True:
                self.trainer_weapone_image.clip_draw((self.framea % 4) * 30, 0, 30, 30, self.weap[i].xx,
                                                     self.weap[i].yy)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 35, self.y - 20, self.x + 25, self.y + 30

    def draw_aa(self, i):
        draw_rectangle(*self.get_aa(i))

    def get_aa(self, i):
        return self.weap[i].xx - 10, self.weap[i].yy - 10, self.weap[i].xx - 10, self.weap[i].yy + 12




class Monster1:

    PIXEL_PER_METER = (20.0 / 0.3)  # 10 pixel 20 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None
    def __init__(self):
        if Monster1.image == None:
            Monster1.image = load_image('부스터.png')
        self.frame = random.randint(0, 10)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1.0
        self.x, self.y = random.randint(1200, 3500), random.randint(60, 570)

    def update(self, frame_time):
        self.frame += int(self.total_frames) % 2
        self.life_time += frame_time
        distance = trainer.RUN_SPEED_PPS * frame_time
        self.total_frames += trainer.FRAMES_PER_ACTION * trainer.ACTION_PER_TIME * frame_time

        self.x -= (self.dir * distance)
        if self.x <= 0:
            self.x = random.randint(900, 1500)
            self.y = random.randint(80, 570)

    def draw(self):
        self.image.clip_draw((self.frame % 3) * 60, 100, 60, 50, self.x, self.y)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 20, self.x + 15, self.y + 20

class Monster2:

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None
    hit_image = None
    def __init__(self):
        if Monster2.image == None:
            Monster2.image = load_image('파이리.png')
        if Monster2.hit_image == None:
            Monster2.hit_image = load_image('몬스터볼잡을때.png')
        self.frame = random.randint(0,10)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1.25
        self.x, self.y = random.randint(2000, 3500), random.randint(60, 570)
        self.state = False

    def update(self, frame_time):
        self.frame += int(self.total_frames) % 3
        self.framea = int(self.total_frames) % 5
        self.life_time += frame_time
        distance = trainer.RUN_SPEED_PPS * frame_time
        self.total_frames += trainer.FRAMES_PER_ACTION * trainer.ACTION_PER_TIME * frame_time

        self.x -= (self.dir * distance)
        if self.x <= 0:
            self.x = random.randint(900, 2000)
            self.y = random.randint(80, 570)

    def draw(self):
        if self.state == False:
            self.image.clip_draw((self.frame % 3) * 70, 0, 70, 70, self.x, self.y)
        if self.state == True:
            self.hit_image.clip_draw((self.framea % 4) * 32, 0, 32, 49, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 30, self.x + 25, self.y + 40

class Boss:

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7

    image = None

    def __init__(self):
        if Boss.image == None:
            Boss.image = load_image('fire2.png')
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0.5
        self.x, self.y = 1200, 300

    def update(self, frame_time):
        self.frame += int(self.total_frames) % 7
        self.life_time += frame_time
        distance = trainer.RUN_SPEED_PPS * frame_time
        self.total_frames += trainer.FRAMES_PER_ACTION * trainer.ACTION_PER_TIME * frame_time

        if score_count >= 400:
            self.x -= (self.dir * distance)
            self.y -= random.randint(-10, 10)

        if self.x <= 700:
            self.x = 700
            #self.y = 300
        if self.y <= 0:
            self.y = 0
        elif self.y >= 600:
            self.y = 600

    def draw(self):
        if score_count >= 400:
            #self.image.clip_draw((self.frame % 46) * 217, 0, 217, 182, self.x, self.y)
            self.image.clip_draw((self.frame % 3) * 140, 0, 140, 100, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

class Boss_monster:

    PIXEL_PER_METER = (30.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None
    def __init__(self):
        if Boss_monster.image == None:
            Boss_monster.image = load_image('이펙트.png')
        self.frame = random.randint(0, 5)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1.5
        self.x, self.y = random.randint(1200, 2000), random.randint(30, 590)

    def update(self, frame_time):
        self.frame += int(self.total_frames) % 2
        self.life_time += frame_time
        distance = trainer.RUN_SPEED_PPS * frame_time
        self.total_frames += trainer.FRAMES_PER_ACTION * trainer.ACTION_PER_TIME * frame_time

        if score_count >= 400:               
            self.x -= (self.dir * distance)

        if self.x <= 0:
            self.x = random.randint(1300, 1500)
            self.y = random.randint(30, 590)

    def draw(self):
        if score_count >= 400:
            self.image.clip_draw((self.frame % 4) * 22, 0, 25, 30, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 7, self.y + 10

class Collision_line:       
    def __init__(self):
        self.x, self.y = 900, 300
        Collision_line.image = load_image('line.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 5, self.y - 300, self.x + 5, self.y + 300

def handle_events(frame_time):
    global trainer
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            trainer.handle_event(event)

def enter():
    global back1, back2, trainer, live_font, item, item_score, enemy1, items, enemy2, enemies1, time, enemies2, score_count, second_collision, boss, boss1, collision_line, line, boss_monster, boss2, clear_count, warning_font,score_font
    back1 = Back1()
    back2 = Back2()
    trainer = Trainer()
    item = Item()
    items = [Item() for i in range(3)]  # 아이템
    enemy1 = Monster1()
    enemies1 = [Monster1() for i in range(25)]  # 몬스터1
    enemy2 = Monster2()
    enemies2 = [Monster2() for i in range(15)]  # 몬스터2
    boss = Boss()
    boss1 = [Boss() for i in range(1)]
    boss_monster = Boss_monster()
    boss2 = [Boss_monster() for i in range(20) ]
    collision_line = Collision_line()
    line = [Collision_line() for i in range(1)]
    score_count = 0             #score
    clear_count = 0
    second_collision = 0        # 두방에 사라진다
    time = get_time()

    score_font = load_font('Pokemon Hollow.ttf', 25)  # score view
    live_font = load_font('Pokemon Hollow.ttf', 25)

def exit():
    global back1, back2, enemy1, enemy2, boss, item
    del(back1)
    del(back2)
    del(enemy1)
    del(enemy2)
    del(boss)
    del(item)

def collide1(a, b):                             #트레이너와, 적 collision
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True

def collide2(a, b, i):                          #트레이너와, 적 collision
    left_a, bottom_a, right_a, top_a = a.get_aa(i)
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True

def update(frame_time):
    global score_count, second_collision, die_delay, clear_count, item_score
    back1.update(frame_time)
    back2.update(frame_time)
    trainer.update(frame_time)
    for enemy1 in enemies1:
        enemy1.update(frame_time)
    for enemy2 in enemies2:
        enemy2.update(frame_time)
    for boss in boss1:
        boss.update(frame_time)
    for boss_monster in boss2:
        boss_monster.update(frame_time)
    for item in items:
        item.update()

    for i in range(20):
        for enemy1 in enemies1:
            if collide2(trainer, enemy1,i):        #트레이너랑 몬스터1 collision
                score_count += 10                   #score+
                trainer.attstate = False
                enemies1.remove(enemy1)
                trainer.weap[i].yy = 1000

    for i in range(20):
        for enemy2 in enemies2:                 
            if collide2(trainer, enemy2,i):
                second_collision += 20          
                trainer.attstate = False
                enemy2.state = True
                trainer.weap[i].yy = 1000
                if second_collision >= 21:      
                    score_count += 20  # score+
                    second_collision = 0
                    enemies2.remove(enemy2)
                    trainer.weap[i].yy = 1000

    for i in range(20):                         
        for collision_line in line:
            if collide2(trainer, collision_line, i):
                trainer.attstate = False
                trainer.weap[i].yy =1000

    for i in range(20):                       
        for boss in boss1:
            if collide2(trainer, boss, i):
                second_collision += 20
                trainer.attstate = False
                trainer.weap[i].yy = 1000
                if second_collision >= 200:
                    score_count += 600
                    second_collision = 0
                    boss1.remove(boss)
                    trainer.weap[i].yy = 1000

    if score_count >= 1000:
        clear_count += 1
        trainer.diecount = 100
        if clear_count >= 30:
            game_framework.change_state(clear_state)

    if trainer.fire_item == True:
        for i in range(20):
            for enemy1 in enemies1:
                    if enemy1.x <= 800 and enemy1.x >= 0:
                        score_count += 10  # score+
                        trainer.attstate = False
                        enemies1.remove(enemy1)
                        if score_count > 400:
                            trainer.fire_item = False

        for i in range(20):
            for enemy2 in enemies2:
                if enemy2.x <= 800 and enemy2.x >= 0:
                    second_collision += 20
                    trainer.attstate = False
                    enemy2.state = True
                    trainer.weap[i].yy = 1000
                    if score_count > 400:
                        trainer.fire_item = False
                    if second_collision >= 21:
                        score_count += 20  # score+
                        second_collision = 0
                        enemies2.remove(enemy2)


def draw(frame_time):
    hide_cursor()
    clear_canvas()
    back1.draw()
    back2.draw()
    trainer.draw()



    for enemy1 in enemies1:
        enemy1.draw()
    for enemy2 in enemies2:
        enemy2.draw()
    for boss in boss1:
        boss.draw()
    for boss_monster in boss2:
        boss_monster.draw()
    for item in items:
        item.draw()

    score_font.draw(700, 570, 'Score: ' + str(score_count), (0, 0, 255))
    #live_font.draw(500, 570, 'Live: ' + str(trainer.diecount), (255, 0, 0))

    for enemy1 in enemies1:             
        if collide1(trainer, enemy1):
            #sleep(0.01)
            trainer.diecount -= 1
            if trainer.diecount <= 0:
                game_framework.change_state(game_over_state)

    for enemy2 in enemies2:           
        if collide1(trainer, enemy2):
            #sleep(0.01)
            trainer.diecount -= 1
            if trainer.diecount <= 0:
                game_framework.change_state(game_over_state)

    for boss in boss1:                 
        if collide1(trainer, boss):
            trainer.diecount -= 1
            if trainer.diecount <= 0:
                game_framework.change_state(game_over_state)

    for boss_monster in boss2:
        if collide1(trainer, boss_monster):
            #sleep(0.02)
            trainer.diecount -= 1 
            if trainer.diecount <= 0:
                game_framework.change_state(game_over_state)

    for item in items:
        if collide1(trainer, item):
            trainer.item += 1
            if trainer.item >= 3:
                trainer.item = 3

    update_canvas()
    delay(0.001)


