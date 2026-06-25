import random
import time
import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, x, y, health, max_health, stamina, max_stamina):
        super().__init__()
        global font_small
        global font
        global font_big
        global which_animation_pl

        self.x = x
        self.y = y
        original_image = pg.image.load(
            "assets/images/player/player_idle.png").convert_alpha()
        self.image = pg.transform.scale_by(original_image, 3.5)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

        self.health = health
        self.max_health = max_health
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.which_animation_pl = "idle"

    def drawing_animation(self):
        if self.which_animation_pl == "idle":
            original_image = pg.image.load(
                "assets/images/player/player_idle.png").convert_alpha()
            self.image = pg.transform.scale_by(original_image, 3.5)
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))
            screen.blit(self.image, self.rect)

        elif self.which_animation_pl == "cure1":
            original_image = pg.image.load(
                "assets/images/player/player_cure1.png").convert_alpha()
            self.image = pg.transform.scale_by(original_image, 3.5)
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))
            screen.blit(self.image, self.rect)

        elif self.which_animation_pl == "cure2":
            original_image = pg.image.load(
                "assets/images/player/player_cure2.png").convert_alpha()
            self.image = pg.transform.scale_by(original_image, 3.5)
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))
            screen.blit(self.image, self.rect)

        elif self.which_animation_pl == "pass1":
            original_image = pg.image.load(
                "assets/images/player/player_pass1.png").convert_alpha()
            self.image = pg.transform.scale_by(original_image, 3.5)
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))
            screen.blit(self.image, self.rect)

        elif self.which_animation_pl == "pass2":
            original_image = pg.image.load(
                "assets/images/player/player_pass2.png").convert_alpha()
            self.image = pg.transform.scale_by(original_image, 3.5)
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))
            screen.blit(self.image, self.rect)

        elif self.which_animation_pl == "walk1":
            original_image = pg.image.load(
                "assets/images/player/player_walk1.png").convert_alpha()
            self.image = pg.transform.scale_by(original_image, 3.5)
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))
            screen.blit(self.image, self.rect)

        elif self.which_animation_pl == "walk2":
            original_image = pg.image.load(
                "assets/images/player/player_walk2.png").convert_alpha()
            self.image = pg.transform.scale_by(original_image, 3.5)
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))
            screen.blit(self.image, self.rect)

        elif self.which_animation_pl == "sword1":
            original_image = pg.image.load(
                "assets/images/player/player_sword1.png").convert_alpha()
            self.image = pg.transform.scale_by(original_image, 3.5)
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))
            screen.blit(self.image, self.rect)

        elif self.which_animation_pl == "sword2":
            original_image = pg.image.load(
                "assets/images/player/player_sword2.png").convert_alpha()
            self.image = pg.transform.scale_by(original_image, 3.5)
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))
            screen.blit(self.image, self.rect)

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
        self.health -= 4
        print(self.health)

    def noobador_punch(self):
        self.health -= 3

    def cure(self):
        self.stamina -= 2
        self.health += 5

    def pass_(self):
        self.stamina += 2

    def cheezeburger(self):  # gonna add this later
        chezeburger = 1
        if chezeburger > 0:
            chezeburger -= 1
            self.health += 8
            return True
        else:
            return False

    def bloxy_cola(self):
        bloxy_cola = 1
        if bloxy_cola > 0:
            bloxy_cola -= 1
            self.stamina += 5
            return True
        else:
            return False

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
        hp_sp_info_max = font_small.render(
            hp_sp_text_current, False, (77, 101, 180))
        hp_sp_i_rect_max = hp_sp_info_max.get_rect(
            midbottom=(self.x, self.y + 25))
        hp_sp_text = f"{str_max_health} HP MAX / {str_max_stamina} SP MAX"
        hp_sp_info = font_small.render(hp_sp_text, False, (77, 101, 180))
        hp_sp_i_rect = hp_sp_info.get_rect(midbottom=(self.x, self.y + 50))

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

    def if_not_dead(self):
        if self.health > 0:
            return True
        else:
            self.health = 0
            return False

    def go_back(self):
        self.x -= 50
        if self.x >= 140:
            return True
        else:
            return False

    def is_close_to_forth(self):
        self.x += 50
        if self.x <= 840:
            return True
        else:
            return False

    def is_close_to_third(self):
        self.x += 50
        if self.x <= 690:
            return True
        else:
            return False

pg.init()
pg.mixer.init()
pg.display.set_caption("Block Tales 2D")
WIDTH, HEIGHT = 1000, 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill((143, 211, 255))
font_small = pg.font.Font("assets/fonts/Pixeltype.ttf", 30)
font = pg.font.Font("assets/fonts/Pixeltype.ttf", 75)
font_big = pg.font.Font("assets/fonts/Pixeltype.ttf", 125)

