import random
import time
import pygame as pg
from player import Player




class Enemy(pg.sprite.Sprite):
    def __init__(self, enemy_type, x, y):
        super().__init__()
        global font_small
        global font
        global font_big
        global which_animation_en

        self.enemy_type = enemy_type
        self.x = x
        self.y = y
        self.x_normal = x
        self.y_normal = y
        if self.enemy_type == "nooblet":
            original_image = pg.image.load(
                "assets/images/nooblet/nooblet_idle.png").convert_alpha()
            self.image = pg.transform.scale_by(original_image, 3.5)
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))
            self.health = 2
            self.max_health = 2
            print(self.health)
        if self.enemy_type == "noobador":
            original_image = pg.image.load(
                "assets/images/noobador/noobador_idle.png").convert_alpha()
            self.image = pg.transform.scale_by(original_image, 3.5)
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))
            self.health = 15
            self.max_health = 15
            print(self.health)

    def drawing_animation(self):
        if self.enemy_type == "nooblet":
            if which_animation_en == "idle":
                original_image = pg.image.load(
                    "assets/images/nooblet/nooblet_idle.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "walk1":
                original_image = pg.image.load(
                    "assets/images/nooblet/nooblet_walk1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "walk2":
                original_image = pg.image.load(
                    "assets/images/nooblet/nooblet_walk2.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "sword1":
                original_image = pg.image.load(
                    "assets/images/nooblet/nooblet_sword1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "sword2":
                original_image = pg.image.load(
                    "assets/images/nooblet/nooblet_sword2.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
        elif self.enemy_type == "noobador":
            if which_animation_en == "idle":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_idle.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "walk1":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_walk1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "walk2":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_walk2.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "punch1":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_punch1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "punch2":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_punch2.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "slam1":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_slam1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "slam2":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_slam2.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "cure1":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_cure1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif which_animation_en == "cure2":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_cure2.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)

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
            screen.blit(self.image, self.rect)

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
        hp_info_max = font_small.render(hp_text_current, False, (77, 101, 180))
        hp_i_rect_max = hp_info_max.get_rect(midbottom=(self.x, self.y + 25))
        hp_text = f"{str_max_health} HP MAX"
        hp_info = font_small.render(hp_text, False, (77, 101, 180))
        hp_i_rect = hp_info.get_rect(midbottom=(self.x, self.y + 50))

        screen.blit(hp_info, hp_i_rect)
        screen.blit(hp_info_max, hp_i_rect_max)

    def go_to_player(self):
        self.x -= 50
        if self.x >= 200:
            return True
        else:
            return False

    def go_back(self):
        self.x += 50
        if self.x <= self.x_normal - 10:
            return True
        else:
            return False


pg.init()
pg.mixer.init()
pg.display.set_caption("Block Tales 2D")
WIDTH, HEIGHT = 1000, 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill((143, 211, 255))

battle_state = "player_turn_action"  # player chooses: attack/pass/etc.
battle_state = "player_select_enemy"  # player picks enemy to attack
battle_state = "player_super_attack"  # timed attack (green box)
battle_state = "enemy_turn"  # AI moves

player_turn_actions = 0
player_actions_per_turn = 2  # Number of actions the player can take

which_animation_pl  = "idle"
which_animation_en = "idle"

super_type = "Wait"
super_wait_time = random.randint(2000, 5000)

wait_ind_img = pg.image.load("assets/images/ui/Wait_indicator.png").convert_alpha()
wait_ind_img_con = pg.transform.scale_by(wait_ind_img, 3)
wait_ind_rect = wait_ind_img_con.get_rect(center=(500, 350))

go_ind_img = pg.image.load("assets/images/ui/Go_indicator.png").convert_alpha()
go_ind_img_con = pg.transform.scale_by(go_ind_img, 3)
go_ind_rect = wait_ind_img_con.get_rect(center=(500, 350))

battle_state = "player_turn_action"
selected_attack = None
selected_enemy = None
super_timer_started = False
super_wait_time = random.randint(2000, 5000)
super_start = 0
super_green_time = 0
super_hit_window = 0.5  # seconds
super_success = False

spacebar_pressed = False
super_attack_ready = False

super_phase = None  # Can be "wait", "go", or "resolve"
super_phase_start_time = None
super_success = False

player_ = pg.sprite.GroupSingle()
player = Player(100, 550, 20, 20, 10, 10)
player_.add(player)

enemies_in_tut = pg.sprite.Group()  # enemies
nooblet1 = Enemy("nooblet", 900, 550,)
enemies_in_tut.add(nooblet1)
enemies_in_battle = pg.sprite.Group()
noobador1 = Enemy("noobador", 900, 550,)
enemies_in_battle.add(noobador1)
nooblet2 = Enemy("nooblet", 750, 550,)
enemies_in_battle.add(nooblet2)
# all text(it could've been done better but who cares ;))
font_small = pg.font.Font("assets/fonts/Pixeltype.ttf", 30)
font = pg.font.Font("assets/fonts/Pixeltype.ttf", 75)
font_big = pg.font.Font("assets/fonts/Pixeltype.ttf", 125)
title_text1 = font_big.render("2D!", False, (77, 101, 180))
title_text2 = font_big.render("click to play", False, (77, 101, 180))
tit_t_rect1 = title_text1.get_rect(center=(800, 100))
tit_t_rect2 = title_text2.get_rect(center=(500, 500))
won_text1 = font_big.render("YOU WON!", False, (77, 101, 180))
won_t_rect1 = won_text1.get_rect(center=(500, 350))
lost_text1 = font_big.render("You lost", False, (77, 101, 180))
lost_t_rect1 = lost_text1.get_rect(center=(500, 350))
title_image = pg.image.load("assets/images/ui/title.png")                   # images
title_image_scale = pg.transform.scale_by(
    title_image, 1.5)
title_i_rect = title_image.get_rect(center=(375, 125))
tutorial_button = pg.image.load("assets/images/ui/Tutorial_button.png")
tut_b_scaled = pg.transform.scale(
    tutorial_button, (tutorial_button.get_width()*5, tutorial_button.get_height()*5))
battle_button = pg.image.load("assets/images/ui/Real_battle_button.png")
bttl_b_scaled = pg.transform.scale(
    battle_button, (battle_button.get_width()*5, battle_button.get_height()*5))
tut_b_rect = tut_b_scaled.get_rect(center=(200, 300))
bttl_b_rect = bttl_b_scaled.get_rect(center=(750, 300))
stab_image = pg.image.load("assets/images/ui/stab_button.png").convert_alpha()
stab_i = pg.transform.scale_by(stab_image, 2)
stb_rect = stab_i.get_rect(topleft=(0, 0))
pwr_stb_image = pg.image.load("assets/images/ui/power_stab_b.png").convert_alpha()
pwr_stb_i = pg.transform.scale_by(pwr_stb_image, 2)
pwr_stb_rect = pwr_stb_i.get_rect(topleft=(80, 0))
cure_image = pg.image.load("assets/images/ui/cure_button.png").convert_alpha()
cure_i = pg.transform.scale_by(cure_image, 2)
cure_rect = cure_i.get_rect(topleft=(160, 0))
exit_image = pg.image.load("assets/images/ui/exit_button.png").convert_alpha()
exit_i = pg.transform.scale_by(exit_image, 2)
exit_rect = exit_i.get_rect(topright=(1000, 0))
pass_image = pg.image.load("assets/images/ui/pass_button.png").convert_alpha()
pass_i = pg.transform.scale_by(pass_image, 2)
pass_rect = pass_i.get_rect(topleft=(240, 0))
background = pg.image.load("assets/images/ui/Background.png")
bckgr_scale = pg.transform.scale(
    background, (background.get_width()*7, background.get_height()*7))
bckgr_rect = bckgr_scale.get_rect(center=(500, 350))
title_music = pg.mixer.Sound(
    'assets/music/1-04. Chapter Start.ogg')             # music
title_music.set_volume(1.1)
main_menu_music = pg.mixer.Sound("assets/music/1-01. Main Menu.ogg")
main_menu_music.set_volume(1.1)
tutorial_music = pg.mixer.Sound('assets/music/1-12. Weak Battle.ogg')
tutorial_music.set_volume(1.1)
battle_music = pg.mixer.Sound("assets/music/Noobador.ogg")
battle_music.set_volume(1.1)
battle_lost_music = pg.mixer.Sound("assets/music/battle_lost_block_tales.mp3")
battle_lost_music.set_volume(1.1)
battle_won_music = pg.mixer.Sound("assets/music/battle_victory_block_tales.mp3")
battle_won_music.set_volume(1.1)
placeholder_music = pg.mixer.Sound("assets/music/TutorialTerry.ogg")
downed_sfx = pg.mixer.Sound( "assets/sfx/battle/player_downed_block_tales.mp3")           # sfx
downed_sfx.set_volume(1.1)
nice_sfx = pg.mixer.Sound("assets/sfx/battle/excelent_rating_block_tales.mp3")
nice_sfx.set_volume(1.1)
good_sfx = pg.mixer.Sound("assets/sfx/battle/good_rating_block_tales.mp3")
good_sfx.set_volume(1.1)
amazing_sfx = pg.mixer.Sound("assets/sfx/battle/amazing_rating_block_tales.mp3")
amazing_sfx.set_volume(1.1)
nice_sfx = pg.mixer.Sound("assets/sfx/battle/nice_rating_block_tales.mp3")
nice_sfx.set_volume(1.1)
damage_sfx = pg.mixer.Sound("assets/sfx/battle/block_tales_damage_sound.mp3")
damage_sfx.set_volume(1.1)
charge_sfx = pg.mixer.Sound("assets/sfx/battle/charge_sound_block_tales.mp3")
charge_sfx.set_volume(1.1)
dodge_sfx = pg.mixer.Sound("assets/sfx/battle/block_tales_dodge.mp3")
dodge_sfx.set_volume(1.1)

battle_lost_music_playd = False
battle_won_music_playd = False
title_music_played = False
main_menu_music_playing = False
tutorial_music_playing = False
battle_music_playing = False

title = True
main_menu = False
tutorial = False
battle = False

clock = pg.time.Clock()

running = True
while running:

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    player_.update()
    enemies_in_tut.update()

    if title:
        if not title_music_played:
            title_music.play()  # plays once
            title_music_played = True
        screen.fill((143, 211, 255))
        screen.blit(title_image_scale, title_i_rect)
        screen.blit(title_text1, tit_t_rect1)
        screen.blit(title_text2, tit_t_rect2)

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                title = False
                main_menu = True
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

    if main_menu:
        title_music.stop()
        tutorial_music.stop()
        battle_music.stop()
        battle_won_music.stop()
        battle_lost_music.stop()
        battle_lost_music_playd = False
        battle_won_music_playd = False
        title_music_played = False
        tutorial_music_playing = False
        battle_music_playing = False
        if not main_menu_music_playing:
            main_menu_music.play(-1)
            main_menu_music_playing = True
        player_turn_actions = 0
        screen.fill((143, 211, 255))
        screen.blit(tut_b_scaled, tut_b_rect)
        screen.blit(bttl_b_scaled, bttl_b_rect)
        player.health_and_stamina_back()
        nooblet1.health_back()
        nooblet2.health_back()
        noobador1.health_back()
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
        main_menu_music.stop()
        main_menu_music_playing = False
        if not tutorial_music_playing:
            tutorial_music.play(-1)
            tutorial_music_playing = True
        player_.sprite.which_animation_pl  = "idle"
        screen.blit(bckgr_scale, bckgr_rect)
        screen.blit(stab_i, stb_rect)
        screen.blit(pwr_stb_i, pwr_stb_rect)
        screen.blit(cure_i, cure_rect)
        screen.blit(exit_i, exit_rect)
        screen.blit(pass_i, pass_rect)

        player.drawing_hp_sp()
        nooblet1.drawing_hp()
        player.drawing_animation()
        if nooblet1.if_not_dead():
            nooblet1.drawing_animation()
        if not nooblet1.if_not_dead():
            if not battle_won_music_playd:
                tutorial_music.stop()
                battle_won_music.play()
                battle_won_music_playd = True
            screen.blit(won_text1, won_t_rect1)
        nooblet1.drawing_self()
        player.too_much_hp_sp()
        nooblet1.too_much_hp()
        if event.type == pg.MOUSEBUTTONDOWN:
            if exit_rect.collidepoint(event.pos):
                tutorial = False
                main_menu = True
        if player.if_not_dead():
            for event in events:
                if event.type == pg.QUIT:
                    running = False

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE and super_attack_ready:
                        spacebar_pressed = True

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
                                player_.sprite.which_animation_pl  = "cure1"
                                screen.blit(bckgr_scale, bckgr_rect)
                                player.drawing_animation()
                                pg.display.update()
                                pg.time.wait(250)
                                player_.sprite.which_animation_pl  = "cure2"
                                screen.blit(bckgr_scale, bckgr_rect)
                                player.drawing_animation()
                                pg.display.update()
                                pg.time.wait(250)
                                player.cure()
                                player_turn_actions += 1
                                if player_turn_actions >= player_actions_per_turn:
                                    battle_state = "enemy_turn"
                                else:
                                    battle_state = "player_turn_action"

                        elif pass_rect.collidepoint(event.pos):
                            player_.sprite.which_animation_pl  = "pass1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(250)
                            player_.sprite.which_animation_pl  = "pass2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(250)
                            player.pass_()
                            player_turn_actions += 1
                            if player_turn_actions >= player_actions_per_turn:
                                battle_state = "enemy_turn"
                            else:
                                battle_state = "player_turn_action"

                    elif battle_state == "player_select_enemy":
                        if nooblet1.rect.collidepoint(event.pos) and nooblet1.if_not_dead():
                            selected_enemy = nooblet1
                            battle_state = "player_super_attack"
                            super_timer_started = False
                            super_attack_ready = True
                            spacebar_pressed = False
            if battle_state == "player_super_attack":

                current_time = time.perf_counter()

                # Start phase
                if super_phase is None:
                    super_phase = "wait"
                    super_phase_start_time = current_time
                    super_success = False
                    spacebar_pressed = False
                    super_attack_ready = True
                    print("Starting SUPER ATTACK: wait phase")

                # Wait Phase
                if super_phase == "wait":
                    screen.blit(wait_ind_img_con, wait_ind_rect)
                    pg.display.update()
                    if current_time - super_phase_start_time >= super_wait_time / 1000:
                        super_phase = "go"
                        super_phase_start_time = current_time
                        print("Transitioned to GO phase")

                # Go Phase
                elif super_phase == "go":
                    screen.blit(go_ind_img_con, go_ind_rect)
                    pg.display.update()
                    if spacebar_pressed:
                        super_success = True
                        print("Spacebar pressed in GO phase!")

                    if current_time - super_phase_start_time >= super_hit_window:
                        super_phase = "resolve"
                        print("Transitioned to RESOLVE phase")

                # Resolve Phase
                elif super_phase == "resolve":
                    if super_success:
                        nice_sfx.play()
                        print("Super attack SUCCESS!")
                    else:
                        good_sfx.play()
                        print("Super attack FAILED!")

                    # Reset all super attack variables
                    super_phase = None
                    super_attack_ready = False
                    spacebar_pressed = False

                    # Count the action

                    if player_turn_actions >= player_actions_per_turn:
                        battle_state = "enemy_turn"
                    else:
                        battle_state = "player_turn_action"
                    if selected_enemy == nooblet1:
                        while player.is_close_to_forth():
                            player_.sprite.which_animation_pl  = "walk1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            nooblet1.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                            player_.sprite.which_animation_pl  = "walk2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            nooblet1.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                        player_.sprite.which_animation_pl  = "sword1"
                        screen.blit(bckgr_scale, bckgr_rect)
                        nooblet1.drawing_self()
                        player.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        player_.sprite.which_animation_pl  = "sword2"
                        screen.blit(bckgr_scale, bckgr_rect)
                        nooblet1.drawing_self()
                        player.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        while player.go_back():
                            player_.sprite.which_animation_pl  = "walk1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            nooblet1.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                            player_.sprite.which_animation_pl  = "walk2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            nooblet1.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
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
                        player_.sprite.which_animation_pl  = "idle"

                        # Always count the action
                        player_turn_actions += 1
                        if player_turn_actions >= player_actions_per_turn:
                            battle_state = "enemy_turn"
                        else:
                            battle_state = "player_turn_action"
            if battle_state == "enemy_turn":
                # Only execute once
                player.layer.which_animation_pl = "idle"
                if nooblet1.if_not_dead():
                    while nooblet1.go_to_player():
                        which_animation_en = "walk1"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        nooblet1.drawing_animation()
                        pg.display.update()
                        pg.time.wait(50)
                        which_animation_en = "walk2"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        nooblet1.drawing_animation()
                        pg.display.update()
                        pg.time.wait(50)
                    which_animation_en = "sword1"
                    screen.blit(bckgr_scale, bckgr_rect)
                    player.drawing_animation()
                    nooblet1.drawing_animation()
                    pg.display.update()
                    pg.time.wait(250)
                    which_animation_en = "sword2"
                    screen.blit(bckgr_scale, bckgr_rect)
                    player.drawing_animation()
                    nooblet1.drawing_animation()
                    pg.display.update()
                    pg.time.wait(250)
                    while nooblet1.go_back():
                        which_animation_en = "walk1"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        nooblet1.drawing_animation()
                        pg.display.update()
                        pg.time.wait(50)
                        which_animation_en = "walk2"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        nooblet1.drawing_animation()
                        pg.display.update()
                        pg.time.wait(50)
                    which_animation_en = "idle"
                    player.nooblet_dmg()

                player_turn_actions = 0
                battle_state = "player_turn_action"
        else:
            if not battle_lost_music_playd:
                tutorial_music.stop()
                downed_sfx.play()
                pg.time.wait(1500)
                battle_lost_music.play()
                battle_lost_music_playd = True
            screen.blit(lost_text1, lost_t_rect1)

    if battle:
        main_menu_music.stop()
        main_menu_music_playing = False
        if not battle_music_playing:
            battle_music.play(-1)
            battle_music_playing = True
        player_.sprite.which_animation_pl  = "idle"
        screen.blit(bckgr_scale, bckgr_rect)
        screen.blit(stab_i, stb_rect)
        screen.blit(pwr_stb_i, pwr_stb_rect)
        screen.blit(cure_i, cure_rect)
        screen.blit(exit_i, exit_rect)
        screen.blit(pass_i, pass_rect)

        player.drawing_hp_sp()
        nooblet2.drawing_hp()
        noobador1.drawing_hp()
        player.drawing_animation()
        if nooblet2.if_not_dead():
            nooblet2.drawing_animation()
        if noobador1.if_not_dead():
            noobador1.drawing_animation()
        if not nooblet2.if_not_dead() and not noobador1.if_not_dead():
            if not battle_won_music_playd:
                battle_music.stop()
                battle_won_music.play()
                battle_won_music_playd = True
            screen.blit(won_text1, won_t_rect1)
        nooblet2.drawing_self()
        noobador1.drawing_self()
        player.too_much_hp_sp()
        nooblet2.too_much_hp()
        noobador1.too_much_hp()
        if player.if_not_dead():
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE and super_attack_ready:
                        spacebar_pressed = True
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
                                player_.sprite.which_animation_pl  = "cure1"
                                screen.blit(bckgr_scale, bckgr_rect)
                                player.drawing_animation()
                                pg.display.update()
                                pg.time.wait(250)
                                player_.sprite.which_animation_pl  = "cure2"
                                screen.blit(bckgr_scale, bckgr_rect)
                                player.drawing_animation()
                                pg.display.update()
                                pg.time.wait(250)
                                player.cure()
                                player_turn_actions += 1
                                if player_turn_actions >= player_actions_per_turn:
                                    battle_state = "enemy_turn"
                                else:
                                    battle_state = "player_turn_action"

                        elif pass_rect.collidepoint(event.pos):
                            player_.sprite.which_animation_pl  = "pass1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(250)
                            player_.sprite.which_animation_pl  = "pass2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(250)
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
                            super_attack_ready = True
                            spacebar_pressed = False
                        elif noobador1.rect.collidepoint(event.pos) and noobador1.if_not_dead():
                            selected_enemy = noobador1
                            battle_state = "player_super_attack"
                            super_timer_started = False
                            super_attack_ready = True
                            spacebar_pressed = False

                # Handle super attack timing and drawing
            if battle_state == "player_super_attack":

                current_time = time.perf_counter()

                # Start phase
                if super_phase is None:
                    super_phase = "wait"
                    super_phase_start_time = current_time
                    super_success = False
                    spacebar_pressed = False
                    super_attack_ready = True
                    print("Starting SUPER ATTACK: wait phase")

                # Wait Phase
                if super_phase == "wait":
                    screen.blit(wait_ind_img_con, wait_ind_rect)
                    pg.display.update()
                    if current_time - super_phase_start_time >= super_wait_time / 1000:
                        super_phase = "go"
                        super_phase_start_time = current_time
                        print("Transitioned to GO phase")

                # Go Phase
                elif super_phase == "go":
                    screen.blit(go_ind_img_con, go_ind_rect)
                    pg.display.update()
                    if spacebar_pressed:
                        super_success = True
                        print("Spacebar pressed in GO phase!")

                    if current_time - super_phase_start_time >= super_hit_window:
                        super_phase = "resolve"
                        print("Transitioned to RESOLVE phase")

                # Resolve Phase
                elif super_phase == "resolve":
                    if super_success:
                        nice_sfx.play()
                        print("Super attack SUCCESS!")
                    else:
                        good_sfx.play()
                        print("Super attack FAILED!")

                    # Reset all super attack variables
                    super_phase = None
                    super_attack_ready = False
                    spacebar_pressed = False

                    # Resolve attack outcome
                    if selected_enemy == nooblet2:
                        if super_success == True:
                            nice_sfx.play()
                        else:
                            good_sfx.play()
                        while player.is_close_to_third():
                            player_.sprite.which_animation_pl  = "walk1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            nooblet2.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                            player_.sprite.which_animation_pl  = "walk2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            nooblet2.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                        player_.sprite.which_animation_pl  = "sword1"
                        screen.blit(bckgr_scale, bckgr_rect)
                        nooblet2.drawing_self()
                        player.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        player_.sprite.which_animation_pl  = "sword2"
                        screen.blit(bckgr_scale, bckgr_rect)
                        nooblet2.drawing_self()
                        player.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        while player.go_back():
                            player_.sprite.which_animation_pl  = "walk1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            nooblet2.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                            player_.sprite.which_animation_pl  = "walk2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            nooblet2.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)

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
                        # Reset state
                        super_phase = None
                        super_attack_ready = False
                        spacebar_pressed = False
                        selected_attack = None
                        selected_enemy = None
                        super_wait_time = random.randint(2000, 5000)

                        if player_turn_actions >= player_actions_per_turn:
                            battle_state = "enemy_turn"
                        else:
                            battle_state = "player_turn_action"
                    if selected_enemy == noobador1:
                        if super_success == True:
                            nice_sfx.play()
                        else:
                            good_sfx.play()
                        while player.is_close_to_forth():
                            player_.sprite.which_animation_pl  = "walk1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            noobador1.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                            player_.sprite.which_animation_pl  = "walk2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            noobador1.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                        player_.sprite.which_animation_pl  = "sword1"
                        screen.blit(bckgr_scale, bckgr_rect)
                        noobador1.drawing_self()
                        player.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        player_.sprite.which_animation_pl  = "sword2"
                        screen.blit(bckgr_scale, bckgr_rect)
                        noobador1.drawing_self()
                        player.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        while player.go_back():
                            player_.sprite.which_animation_pl  = "walk1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            noobador1.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                            player_.sprite.which_animation_pl  = "walk2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            noobador1.drawing_self()
                            player.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)

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
                        # Reset state
                        super_phase = None
                        super_attack_ready = False
                        spacebar_pressed = False
                        selected_attack = None
                        selected_enemy = None
                        super_wait_time = random.randint(2000, 5000)

                        if player_turn_actions >= player_actions_per_turn:
                            battle_state = "enemy_turn"
                        else:
                            battle_state = "player_turn_action"

            elif battle_state == "enemy_turn":
                # Only execute once
                player_.sprite.which_animation_pl  = "idle"
                if nooblet2.if_not_dead():
                    while nooblet2.go_to_player():
                        which_animation_en = "walk1"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        nooblet2.drawing_animation()
                        pg.display.update()
                        pg.time.wait(50)
                        which_animation_en = "walk2"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        nooblet2.drawing_animation()
                        pg.display.update()
                        pg.time.wait(50)
                    which_animation_en = "sword1"
                    screen.blit(bckgr_scale, bckgr_rect)
                    player.drawing_animation()
                    nooblet2.drawing_animation()
                    pg.display.update()
                    pg.time.wait(250)
                    which_animation_en = "sword2"
                    screen.blit(bckgr_scale, bckgr_rect)
                    player.drawing_animation()
                    nooblet2.drawing_animation()
                    pg.display.update()
                    pg.time.wait(250)
                    while nooblet2.go_back():
                        which_animation_en = "walk1"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        nooblet2.drawing_animation()
                        pg.display.update()
                        pg.time.wait(50)
                        which_animation_en = "walk2"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        nooblet2.drawing_animation()
                        pg.display.update()
                        pg.time.wait(50)
                    which_animation_en = "idle"
                    player.nooblet_dmg()
                if noobador1.if_not_dead():
                    nbdr_att_choice = ["slam", "punch", "heal"]
                    nbdr_att_chance = [0.45, 0.4, 0.15]
                    nbdr_att_result = random.choices(
                        nbdr_att_choice, weights=nbdr_att_chance, k=1)[0]
                    if nbdr_att_result == "slam":
                        while noobador1.go_to_player():
                            which_animation_en = "walk1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            noobador1.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                            which_animation_en = "walk2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            noobador1.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                        which_animation_en = "slam1"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        noobador1.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        which_animation_en = "slam2"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        noobador1.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        which_animation_en = "slam1"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        noobador1.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        while noobador1.go_back():
                            which_animation_en = "walk1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            noobador1.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                            which_animation_en = "walk2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            noobador1.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                        which_animation_en = "idle"
                        player.noobador_slam()
                    elif nbdr_att_result == "punch":
                        while noobador1.go_to_player():
                            which_animation_en = "walk1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            noobador1.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                            which_animation_en = "walk2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            noobador1.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                        which_animation_en = "punch1"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        noobador1.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        which_animation_en = "punch2"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        noobador1.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        while noobador1.go_back():
                            which_animation_en = "walk1"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            noobador1.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                            which_animation_en = "walk2"
                            screen.blit(bckgr_scale, bckgr_rect)
                            player.drawing_animation()
                            noobador1.drawing_animation()
                            pg.display.update()
                            pg.time.wait(50)
                        which_animation_en = "idle"
                        player.noobador_punch()
                    else:
                        which_animation_en = "cure1"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        noobador1.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        which_animation_en = "cure2"
                        screen.blit(bckgr_scale, bckgr_rect)
                        player.drawing_animation()
                        noobador1.drawing_animation()
                        pg.display.update()
                        pg.time.wait(250)
                        noobador1.noobador_heal()
                        which_animation_en = "idle"
                player_turn_actions = 0
                battle_state = "player_turn_action"
        else:
            if not battle_lost_music_playd:
                tutorial_music.stop()
                downed_sfx.play()
                pg.time.wait(1500)
                battle_lost_music.play()
                battle_lost_music_playd = True
            screen.blit(lost_text1, lost_t_rect1)

    clock.tick(60)
    pg.display.update()

pg.quit
