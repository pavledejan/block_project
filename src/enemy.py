import random
import time
import pygame as pg


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
        self.which_animation_en = "idle"
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
            if self.which_animation_en == "idle":
                original_image = pg.image.load(
                    "assets/images/nooblet/nooblet_idle.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "walk1":
                original_image = pg.image.load(
                    "assets/images/nooblet/nooblet_walk1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "walk2":
                original_image = pg.image.load(
                    "assets/images/nooblet/nooblet_walk2.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "sword1":
                original_image = pg.image.load(
                    "assets/images/nooblet/nooblet_sword1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "sword2":
                original_image = pg.image.load(
                    "assets/images/nooblet/nooblet_sword2.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
        elif self.enemy_type == "noobador":
            if self.which_animation_en == "idle":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_idle.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "walk1":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_walk1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "walk2":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_walk2.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "punch1":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_punch1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "punch2":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_punch2.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "slam1":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_slam1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "slam2":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_slam2.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "cure1":
                original_image = pg.image.load(
                    "assets/images/noobador/noobador_cure1.png").convert_alpha()
                self.image = pg.transform.scale_by(original_image, 3.5)
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))
                screen.blit(self.image, self.rect)
            elif self.which_animation_en == "cure2":
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
font_small = pg.font.Font("assets/fonts/Pixeltype.ttf", 30)
font = pg.font.Font("assets/fonts/Pixeltype.ttf", 75)
font_big = pg.font.Font("assets/fonts/Pixeltype.ttf", 125)