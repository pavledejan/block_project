import random 
import time
import pygame as pg
import os
import sys

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


battle_state = "player_turn_action"  # player chooses: attack/pass/etc.
battle_state = "player_select_enemy"  # player picks enemy to attack
battle_state = "player_super_attack"  # timed attack (green box)
battle_state = "enemy_turn"  # AI moves

player_turn_actions = 0
player_actions_per_turn = 2  # Number of actions the player can take

super_color = (red)
super_cords_stb = (0,150,50,50)
super_cords_pwr_stb = (80,150,50,50)
super_wait_time = random.randint(2000,5000) 

battle_state = "player_turn_action"
selected_attack = None
selected_enemy = None
super_timer_started = False
super_wait_time = random.randint(2000, 5000)
super_start = 0
super_green_time = 0
super_hit_window = 0.5  # seconds
super_color = red
super_success = False

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
tut_text2 = font_small.render("You can attack,use items,or difrent actions.If you fight after clicking attack click the enemy",False,(0,40,56))
tut_text3 = font_small.render("With the sword you need to click it two times(when its green),to deal more damage",False,(0,40,56))
tut_rect1 = tut_text1.get_rect(center = (700,30))
tut_rect2 = tut_text2.get_rect(center = (630,80))
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

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(event.pos):
                    tutorial = False
                    main_menu = True

                if battle_state == "player_turn_action":
                    if stb_rect.collidepoint(event.pos):
                        selected_attack = "stab"
                        battle_state = "player_select_enemy"

                    elif pwr_stb_rect.collidepoint(event.pos):
                        if player.has_enough_sp():
                            selected_attack = "pwr_stab"
                            battle_state = "player_select_enemy"

                    elif cure_rect.collidepoint(event.pos):
                        if player.has_enough_sp2():
                            player.cure()
                            player_turn_actions += 1
                            if player_turn_actions >= player_actions_per_turn:
                                battle_state = "enemy_turn"
                            else:
                                battle_state = "player_turn_action"

                    elif pass_rect.collidepoint(event.pos):
                        player.pass_()
                        player_turn_actions += 1
                        if player_turn_actions >= player_actions_per_turn:
                            battle_state = "enemy_turn"
                        else:
                            battle_state = "player_turn_action"

                elif battle_state == "player_select_enemy":
                    if nooblet1.rect.collidepoint(event.pos) and nooblet2.if_not_dead():
                        selected_enemy = nooblet1
                        battle_state = "player_super_attack"
                        super_timer_started = False

                elif battle_state == "player_super_attack":
                    if super_color == green:
                        if stb_rect.collidepoint(event.pos) or pwr_stb_rect.collidepoint(event.pos):
                            super_success = True

            # Handle super attack timing and drawing
        if battle_state == "player_super_attack":
            if not super_timer_started:
                super_color = red
                pg.draw.rect(screen, super_color, super_cords_stb)
                pg.display.update()
                pg.time.wait(super_wait_time)

                super_color = green
                super_start = time.perf_counter()
                super_timer_started = True
                super_success = False

            else:
                elapsed = time.perf_counter() - super_start
                if elapsed < super_hit_window:
                    pg.draw.rect(screen, super_color, super_cords_stb)
                else:
                    # Resolve attack outcome
                    if selected_attack == "stab":
                        if super_success:
                            selected_enemy.dmg_stab()
                        else:
                            selected_enemy.weak_dmg_stab()

                    elif selected_attack == "pwr_stab":
                        if super_success:
                            selected_enemy.pwr_stb_dmg()
                        else:
                            selected_enemy.dmg_stab()
                        player.pwr_stb()  # Always use stamina

                    # Reset after attack
                    selected_attack = None
                    selected_enemy = None
                    super_timer_started = False
                    super_wait_time = random.randint(2000, 5000)

                    # Always count the action
                    player_turn_actions += 1
                    if player_turn_actions >= player_actions_per_turn:
                        battle_state = "enemy_turn"
                    else:
                        battle_state = "player_turn_action"

        elif battle_state == "enemy_turn":
            # Only execute once
            if nooblet1.if_not_dead():
                player.nooblet_dmg()


            player_turn_actions = 0
            battle_state = "player_turn_action"
    
    
    if battle:
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

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(event.pos):
                    battle = False
                    main_menu = True

                if battle_state == "player_turn_action":
                    if stb_rect.collidepoint(event.pos):
                        selected_attack = "stab"
                        battle_state = "player_select_enemy"

                    elif pwr_stb_rect.collidepoint(event.pos):
                        if player.has_enough_sp():
                            selected_attack = "pwr_stab"
                            battle_state = "player_select_enemy"

                    elif cure_rect.collidepoint(event.pos):
                        if player.has_enough_sp2():
                            player.cure()
                            player_turn_actions += 1
                            if player_turn_actions >= player_actions_per_turn:
                                battle_state = "enemy_turn"
                            else:
                                battle_state = "player_turn_action"

                    elif pass_rect.collidepoint(event.pos):
                        player.pass_()
                        player_turn_actions += 1
                        if player_turn_actions >= player_actions_per_turn:
                            battle_state = "enemy_turn"
                        else:
                            battle_state = "player_turn_action"

                elif battle_state == "player_select_enemy":
                    if nooblet2.rect.collidepoint(event.pos) and nooblet2.if_not_dead():
                        selected_enemy = nooblet2
                        battle_state = "player_super_attack"
                        super_timer_started = False

                    elif noobador1.rect.collidepoint(event.pos) and noobador1.if_not_dead():
                        selected_enemy = noobador1
                        battle_state = "player_super_attack"
                        super_timer_started = False

                elif battle_state == "player_super_attack":
                    if super_color == green:
                        if stb_rect.collidepoint(event.pos) or pwr_stb_rect.collidepoint(event.pos):
                            super_success = True

            # Handle super attack timing and drawing
        if battle_state == "player_super_attack":
            if not super_timer_started:
                super_color = red
                pg.draw.rect(screen, super_color, super_cords_stb)
                pg.display.update()
                pg.time.wait(super_wait_time)

                super_color = green
                super_start = time.perf_counter()
                super_timer_started = True
                super_success = False

            else:
                elapsed = time.perf_counter() - super_start
                if elapsed < super_hit_window:
                    pg.draw.rect(screen, super_color, super_cords_stb)
                else:
                    # Resolve attack outcome
                    if selected_attack == "stab":
                        if super_success:
                            selected_enemy.dmg_stab()
                        else:
                            selected_enemy.weak_dmg_stab()

                    elif selected_attack == "pwr_stab":
                        if super_success:
                            selected_enemy.pwr_stb_dmg()
                        else:
                            selected_enemy.dmg_stab()
                        player.pwr_stb()  # Always use stamina

                    # Reset after attack
                    selected_attack = None
                    selected_enemy = None
                    super_timer_started = False
                    super_wait_time = random.randint(2000, 5000)

                    # Always count the action
                    player_turn_actions += 1
                    if player_turn_actions >= player_actions_per_turn:
                        battle_state = "enemy_turn"
                    else:
                        battle_state = "player_turn_action"

        elif battle_state == "enemy_turn":
            # Only execute once
            if nooblet2.if_not_dead():
                player.nooblet_dmg()
            if noobador1.if_not_dead():
                nbdr_att_choice = ["slam", "punch", "heal"]
                nbdr_att_chance = [0.45, 0.4, 0.15]
                nbdr_att_result = random.choices(nbdr_att_choice, weights=nbdr_att_chance, k=1)[0]

                if nbdr_att_result == "slam":
                    player.noobador_slam()
                elif nbdr_att_result == "punch":
                    player.noobador_punch()
                else:
                    noobador1.noobador_heal()
            player_turn_actions = 0
            battle_state = "player_turn_action"



    clock.tick(60)
    pg.display.update()

pg.quit
