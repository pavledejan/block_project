import random 
import time
import pygame as pg
import os
import sys
                                                    #bugged version
class Player(pg.sprite.Sprite):
    def __init__(self,x,y,health,max_health,stamina,max_stamina):
        super().__init__()
        global font_small
        global font
        global font_big

        self.x = x
        self.y = y
        original_image = pg.image.load("Player_placeholder.png").convert_alpha()
        self.image = pg.transform.rotozoom(original_image, 0,3)  
        self.rect = self.image.get_rect(center=(self.x,self.y))

        self.health = health
        self.max_health = max_health
        self.stamina = stamina
        self.max_stamina = max_stamina
    


    def health_and_stamina_back(self):
        self.health = self.max_health
        self.stamina = self.max_stamina

    def pwr_stb(self):
            self.stamina -= 1
            print(self.stamina)

    def nooblet_dmg(self):
        self.health -= 1
        print(self.health)

    def noobador_slam(self):
        self.health -= 3
        print(self.health)

    def noobador_punch(self):
        self.health -= 4

    def cure(self):
        self.stamina -= 2
        self.health += 4

    def pass_(self):
        self.stamina += 2

    def cheezeburger(self):
        chezeburger = 1
        if chezeburger > 0:
            chezeburger -= 1
            self.health += 8
            return True
        else: return False

    def bloxy_cola(self):
        bloxy_cola = 1
        if bloxy_cola > 0:
            bloxy_cola -= 1
            self.stamina += 5
            return True
        else: return False


    def too_much_hp_sp(self):
        if self.health > self.max_health:
            self.health = self.max_health
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
    def too_low_sp(self):
        if self.stamina < 0:
            self.stamina = 0

    def drawing_hp_sp(self):
        str_health = str(self.health)
        str_stamina = str(self.stamina)
        str_max_health = str(self.max_health)
        str_max_stamina = str(self.max_stamina)

        hp_sp_text_current = f"{str_health} HP / {str_stamina} SP"
        hp_sp_info_max = font_small.render(hp_sp_text_current, False, (0, 40, 56))
        hp_sp_i_rect_max = hp_sp_info_max.get_rect(center=(self.x, self.y + 100))
        hp_sp_text = f"{str_max_health} HP MAX / {str_max_stamina} SP MAX"
        hp_sp_info = font_small.render(hp_sp_text, False, (0, 40, 56))
        hp_sp_i_rect = hp_sp_info.get_rect(center=(self.x, self.y + 125))

        screen.blit(hp_sp_info, hp_sp_i_rect)
        screen.blit(hp_sp_info_max, hp_sp_i_rect_max)
    def has_enough_sp(self):
        if self.stamina > 0:
            return True
        else:
            return False
    def has_enough_sp2(self):
        if self.stamina > 1:
            return True
        else:
            return False



class Enemy(pg.sprite.Sprite):
    def __init__(self,enemy_type,x,y,health,max_health):
        super().__init__()
        global font_small
        global font
        global font_big
        global decide_enemy

        self.enemy_type = enemy_type
        self.health = health
        self.max_health = max_health
        self.x = x
        self.y = y
        if enemy_type == 0:
            original_image = pg.image.load("enemy_placeholder.png").convert_alpha()
            self.image= pg.transform.rotozoom(original_image,0,3)
            self.rect = self.image.get_rect(center=(self.x,self.y))
            print(self.health)
        if enemy_type == 1:
            original_image = pg.image.load("boss_placeholder.png").convert_alpha()
            self.image= pg.transform.rotozoom(original_image,0,3)
            self.rect = self.image.get_rect(center=(self.x,self.y))
            print(self.health)

    def if_selected_nooblet2(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    decide_enemy = False
                    return True
    def if_selected_noobador1(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    decide_enemy = False
                    return True

    def weak_dmg_stab(self):
        self.health -= 1
        print(self.health)

    def dmg_stab(self):
        self.health -= 2
        print(self.health)

    def pwr_stb_dmg(self):
        self.health -= 3
        print(self.health)

    def noobador_heal(self):
        self.health += 5

    def health_back(self):
        self.health = self.max_health

    def too_much_hp(self):
        if self.health > self.max_health:
            self.health = self.max_health

    def drawing_self(self):
        if self.health > 0:
            screen.blit(self.image,self.rect)

    def if_not_dead(self):
        if self.health > 0:
            return True
        else:
            self.health = 0
            return False

    def drawing_hp(self):
        str_health = str(self.health)
        str_max_health = str(self.max_health)

        hp_text_current = f"{str_health} HP "
        hp_info_max = font_small.render(hp_text_current, False, (0, 40, 56))
        hp_i_rect_max = hp_info_max.get_rect(center=(self.x, self.y + 100))
        hp_text = f"{str_max_health} HP MAX"
        hp_info = font_small.render(hp_text, False, (0, 40, 56))
        hp_i_rect = hp_info.get_rect(center=(self.x, self.y + 125))

        screen.blit(hp_info, hp_i_rect)
        screen.blit(hp_info_max, hp_i_rect_max)

pg.init()
pg.display.set_caption("Block Tales 2D")
WIDTH,HEIGHT = 1000,700
screen = pg.display.set_mode((WIDTH,HEIGHT))
red = (255,0,0)
green = (0,255,0)

super_color = (red)
super_cords_stb = (0,150,50,50)
super_cords_pwr_stb = (80,150,50,50)
super_wait_time = random.randint(2000,5000) 
super_hit_time = time.perf_counter()
super_duration = 4
count = 0
super_att = False
super_active = False
super_start_time = 0 

player_ = pg.sprite.GroupSingle()
player = Player(100,432,20,20,10,10)
player_.add(player)

enemies_in_tut = pg.sprite.Group()
nooblet1 = Enemy(0,700,460,4,4)
enemies_in_tut.add(nooblet1)

enemies_in_battle = pg.sprite.Group()
noobador1 = Enemy(1,800,460,15,15)
enemies_in_battle.add(noobador1)
nooblet2 = Enemy(0,600,460,4,4)
enemies_in_battle.add(nooblet2)

font_small = pg.font.Font("Pixeltype.ttf",30)             # all text(it could've been done better but who cares ;))
font = pg.font.Font("Pixeltype.ttf",75)
font_big = pg.font.Font("Pixeltype.ttf",125)

title_text1 = font_big.render("2D!",False,(0, 40, 56))
title_text2 = font_big.render("click to play",False,(0, 40, 56))
tit_t_rect1 = title_text1.get_rect(center = (800,100))
tit_t_rect2 = title_text2.get_rect(center = (500,500))

tut_text1 = font_small.render("In this game you will take turns to defeat your opponent.",False,(0,40,56))
tut_text2 = font_small.render("You can attack,use items,or difrent actions.",False,(0,40,56))
tut_text3 = font_small.render("With the sword you need to click it two times(when its green),to deal more damage",False,(0,40,56))
tut_rect1 = tut_text1.get_rect(center = (700,30))
tut_rect2 = tut_text2.get_rect(center = (710,80))
tut_rect3 = tut_text3.get_rect(center = (640,130))

bttl_text1 = font_small.render("There is multiple enemies here,after attacking click the enemy you uwant to attack",False,(0,40,56))
bttl_rect1 = bttl_text1.get_rect(center = (640,30))

title_image = pg.image.load("title.png")
title_image_scale = pg.transform.scale(title_image,(title_image.get_width()*1.5,title_image.get_height()*1.5))

tutorial_button = pg.image.load("Tutorial_button.png")
tut_b_scaled = pg.transform.scale(tutorial_button,(tutorial_button.get_width()*5,tutorial_button.get_height()*5))
battle_button = pg.image.load("Real_battle_button.png")
bttl_b_scaled = pg.transform.scale(battle_button,(battle_button.get_width()*5,battle_button.get_height()*5))
tut_b_rect = tut_b_scaled.get_rect(center = (200,300))
bttl_b_rect = bttl_b_scaled.get_rect(center = (750,320))

stab_image = pg.image.load("stab_button.png").convert_alpha()
stab_i = pg.transform.rotozoom(stab_image,0,2)
stb_rect = stab_i.get_rect(topleft = (0,0))

pwr_stb_image = pg.image.load("power_stab_b.png").convert_alpha()
pwr_stb_i = pg.transform.rotozoom(pwr_stb_image,0,2)
pwr_stb_rect = pwr_stb_i.get_rect(topleft =(80,0) )

cure_image = pg.image.load("cure_button.png").convert_alpha()
cure_i = pg.transform.rotozoom(cure_image, 0, 2)
cure_rect = cure_i.get_rect(topleft=(160,0))

exit_image = pg.image.load("exit_button.png").convert_alpha()
exit_i = pg.transform.rotozoom(exit_image, 0, 2)
exit_rect = exit_i.get_rect(bottomleft=(0,700))

pass_image = pg.image.load("pass_button.png").convert_alpha()
pass_i = pg.transform.rotozoom(pass_image, 0, 2)
pass_rect = pass_i.get_rect(topleft=(240,0))

background = pg.image.load("Background.png")
bckgr_scale = pg.transform.scale(background,(background.get_width()*7,background.get_height()*7))
bckgr_rect = bckgr_scale.get_rect(center = (500,350))

title = True
main_menu = False
tutorial = False
battle = False

clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            os._exit(1)
            sys.exit(1)
            pg.quit()
            os.system("exit")
            #running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                os._exit(1)
                sys.exit(1)
                pg.quit()
                os.system("exit")


    player_.update()
    enemies_in_tut.update()
    
    if title:
        screen.fill((84, 205, 255))
        screen.blit(title_image_scale,(0,-100))
        screen.blit(title_text1,tit_t_rect1)
        screen.blit(title_text2,tit_t_rect2)

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                title = False
                main_menu = True
    if main_menu:
        screen.fill((84,205,255))
        screen.blit(tut_b_scaled,tut_b_rect)
        screen.blit(bttl_b_scaled,bttl_b_rect)
        player.health_and_stamina_back()
        nooblet1.health_back()
        your_turn = True

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if tut_b_rect.collidepoint(event.pos):
                    main_menu = False
                    tutorial = True
                if bttl_b_rect.collidepoint(event.pos):
                    main_menu = False
                    battle = True
    if tutorial:
        super_hit_time =time.perf_counter()
        super_color = red
        super_att = False
        screen.blit(bckgr_scale,bckgr_rect)
        screen.blit(tut_text1,tut_rect1)
        screen.blit(tut_text2,tut_rect2)
        screen.blit(tut_text3,tut_rect3)
        screen.blit(stab_i,stb_rect)
        screen.blit(pwr_stb_i,pwr_stb_rect)
        screen.blit(cure_i,cure_rect)
        screen.blit(exit_i,exit_rect)
        screen.blit(pass_i,pass_rect)
        player.drawing_hp_sp()
        nooblet1.drawing_hp()
        player_.draw(screen)
        nooblet1.drawing_self()
        player.too_much_hp_sp()
        nooblet1.too_much_hp()
        if your_turn:

                for event in pg.event.get():
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if exit_rect.collidepoint(event.pos):
                            tutorial = False
                            main_menu = True
                        for enemy in enemies_in_tut:
                            if enemy == nooblet1:
                                if stb_rect.collidepoint(event.pos):
                                    super_active = True
                                    super_start_time = time.perf_counter()
                                    super_att = False
                                    pg.draw.rect(screen,super_color,super_cords_stb)
                                    pg.display.update()
                                    pg.time.wait(super_wait_time)
                                    super_color = green
                                    pg.draw.rect(screen,super_color,super_cords_stb)
                                    pg.display.update()
                                    while time.perf_counter() - super_hit_time < super_duration:
                                        count += 1
                                        for event in pg.event.get():
                                            if event.type == pg.MOUSEBUTTONDOWN:
                                                if stb_rect.collidepoint(event.pos):
                                                    super_att = True
                                        if super_att == True:
                                            break
                                    if super_att :
                                        nooblet1.dmg_stab()
                                    else:
                                        nooblet1.weak_dmg_stab()
                                    your_turn = False
                                if pwr_stb_rect.collidepoint(event.pos):
                                    super_active = True
                                    super_start_time = time.perf_counter()
                                    super_att = False
                                    pg.draw.rect(screen,super_color,super_cords_stb)
                                    pg.display.update()
                                    pg.time.wait(super_wait_time)
                                    super_color = green
                                    pg.draw.rect(screen,super_color,super_cords_stb)
                                    pg.display.update()
                                    while time.perf_counter() - super_hit_time < super_duration:
                                        count += 1
                                        for event in pg.event.get():
                                            if event.type == pg.MOUSEBUTTONDOWN:
                                                if stb_rect.collidepoint(event.pos):
                                                    super_att = True
                                        if super_att == True:
                                            break
                                    if super_att :
                                        nooblet1.pwr_stb_dmg()
                                    else:
                                        nooblet1.dmg_stab()
                                    your_turn = False
                                    player.pwr_stb()
                                if cure_rect.collidepoint(event.pos):
                                    if player.has_enough_sp2():
                                        player.cure()
                                        your_turn = False
                                if pass_rect.collidepoint(event.pos):
                                    player.pass_()
                                    your_turn = False
        else:
            if  nooblet1.if_not_dead():
                player.nooblet_dmg()
            your_turn = True
    
    
    if battle:
        decide_nooblet2 = False
        decide_noobador1 = False
        decide_enemy = True
        super_hit_time =time.perf_counter()
        super_color = red
        super_att = False
        screen.blit(bckgr_scale,bckgr_rect)
        screen.blit(stab_i,stb_rect)
        screen.blit(pwr_stb_i,pwr_stb_rect)
        screen.blit(cure_i,cure_rect)
        screen.blit(exit_i,exit_rect)
        screen.blit(pass_i,pass_rect)
        player.drawing_hp_sp()
        nooblet2.drawing_hp()
        noobador1.drawing_hp()
        player_.draw(screen)
        nooblet2.drawing_self()
        noobador1.drawing_self()
        player.too_much_hp_sp()
        nooblet2.too_much_hp()
        noobador1.too_much_hp()
        if your_turn:

                for event in pg.event.get():
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if exit_rect.collidepoint(event.pos):
                            battle = False
                            main_menu = True
                        for enemy in enemies_in_battle:
                            if decide_enemy:
                                if nooblet2.if_selected_nooblet2():
                                    decide_enemy = False
                                    if stb_rect.collidepoint(event.pos):
                                        pg.draw.rect(screen,super_color,super_cords_stb)
                                        pg.display.update()
                                        pg.time.wait(super_wait_time)
                                        super_color = green
                                        pg.draw.rect(screen,super_color,super_cords_stb)
                                        pg.display.update()
                                        super_hit_time = time.perf_counter()
                                        while time.perf_counter() - super_hit_time < super_duration:
                                            count += 1
                                            for event in pg.event.get():
                                                if event.type == pg.MOUSEBUTTONDOWN:
                                                    if stb_rect.collidepoint(event.pos):
                                                        super_att = True
                                            if super_att == True:
                                                break
                                        if super_att :
                                            nooblet2.dmg_stab()
                                        else:
                                            nooblet2.weak_dmg_stab()
                                        your_turn = False
                                    if pwr_stb_rect.collidepoint(event.pos):
                                        if player.has_enough_sp():
                                            player.pwr_stb()
                                            pg.draw.rect(screen,super_color,super_cords_pwr_stb)
                                            pg.display.update()
                                            pg.time.wait(super_wait_time)
                                            super_color = green
                                            pg.draw.rect(screen,super_color,super_cords_pwr_stb)
                                            pg.display.update()
                                            super_hit_time = time.perf_counter()
                                        while time.perf_counter() - super_hit_time < super_duration:
                                            count += 1
                                            for event in pg.event.get():
                                                if event.type == pg.MOUSEBUTTONDOWN:
                                                    if stb_rect.collidepoint(event.pos):
                                                        super_att = True
                                            if super_att == True:
                                                break
                                        if super_att :
                                            nooblet2.dmg_stab()
                                        else:
                                            nooblet2.weak_dmg_stab()
                                        your_turn = False
                                        player.pwr_stb()
                                if noobador1.if_selected_noobador1():
                                    decide_enemy = False
                                    if stb_rect.collidepoint(event.pos):
                                        pg.draw.rect(screen,super_color,super_cords_stb)
                                        pg.display.update()
                                        pg.time.wait(super_wait_time)
                                        super_color = green
                                        pg.draw.rect(screen,super_color,super_cords_stb)
                                        pg.display.update()
                                        if super_active:
                                            pg.draw.rect(screen, green, super_cords_stb)
                                            pg.display.update()
                                            super_hit_time = time.perf_counter()
                                            if time.perf_counter() - super_start_time > super_duration:
                                                super_active = False
                                                if super_att:
                                                    nooblet1.dmg_stab()
                                                else:
                                                    nooblet1.weak_dmg_stab()
                                                your_turn = False


                                            for event in pg.event.get():
                                                if event.type == pg.MOUSEBUTTONDOWN:
                                                    if stb_rect.collidepoint(event.pos):
                                                            super_att = True
                                        else:
                                            for event in pg.event.get():
                                                pass
                                    if pwr_stb_rect.collidepoint(event.pos):
                                        if player.has_enough_sp():
                                            player.pwr_stb()
                                            pg.draw.rect(screen,super_color,super_cords_pwr_stb)
                                            pg.display.update()
                                            pg.time.wait(super_wait_time)
                                            super_color = green
                                            pg.draw.rect(screen,super_color,super_cords_pwr_stb)
                                            pg.display.update()
                                            super_hit_time = time.perf_counter()
                                        while time.perf_counter() - super_hit_time < super_duration:
                                            count += 1
                                            for event in pg.event.get():
                                                if event.type == pg.MOUSEBUTTONDOWN:
                                                    if stb_rect.collidepoint(event.pos):
                                                        super_att = True
                                            if super_att == True:
                                                break
                                        if super_att :
                                            noobador1.dmg_stab()
                                        else:
                                            noobador1.weak_dmg_stab()
                                        your_turn = False
                                        player.pwr_stb()
                        if cure_rect.collidepoint(event.pos):
                            if player.has_enough_sp2():
                                player.cure()
                                your_turn = False
                        if pass_rect.collidepoint(event.pos):
                            player.pass_()
                            your_turn = False
        else:
            if  nooblet2.if_not_dead():
                player.nooblet_dmg()
            if noobador1.if_not_dead():
                nbdr_att_choice = ["slam","punch","heal"]
                nbdr_att_chance = [0.45,0.4,0.15]
                nbdr_att_result = random.choices(nbdr_att_choice,weights=nbdr_att_chance,k=1)[0]
                if nbdr_att_result == "slam":
                    player.noobador_slam()
                elif nbdr_att_result == "punch":
                    player.noobador_punch()
                else:
                    noobador1.noobador_heal()
            your_turn = True



    clock.tick(60)
    pg.display.update()
