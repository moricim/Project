import pygame
import random
from spritesheet_functions import SpriteSheet


class CowNPC(pygame.sprite.Sprite):

    def __init__(self):

        #calls the parent's constructor
        super().__init__()

        self.next_move = pygame.time.get_ticks() + 2500
        self.random_movement = ""

        #direction
        self.direction = ""

        self.frame = 0
        self.step = 0

        #holds eating animation images
        self.eating_l = []
        self.eating_r = []

        sprite_sheet = SpriteSheet("cow_eat.png")

        #loads right facing images onto the list
        image = sprite_sheet.get_image(0, 384, 128, 128)
        self.eating_r.append(image)
        image = sprite_sheet.get_image(128, 384, 128, 128)
        self.eating_r.append(image)
        image = sprite_sheet.get_image(256, 384, 128, 128)
        self.eating_r.append(image)
        image = sprite_sheet.get_image(384, 384, 128, 128)
        self.eating_r.append(image)

        #loads left facing images onto the list
        image = sprite_sheet.get_image(0, 128, 128, 128)
        self.eating_l.append(image)
        image = sprite_sheet.get_image(128, 128, 128, 128)
        self.eating_l.append(image)
        image = sprite_sheet.get_image(256, 128, 128, 128)
        self.eating_l.append(image)
        image = sprite_sheet.get_image(384, 128, 128, 128)
        self.eating_l.append(image)

        self.image = self.eating_l[0]

    def update(self):

        self.movements = ['go_right', 'go_left']

        if pygame.time.get_ticks() >= self.next_move:
            self.next_move = pygame.time.get_ticks() + 2500
            self.random_movement = random.choice(self.movements)

        if self.random_movement == 'go_right':
            self.frame = ((self.step + 1)//20) % len(self.eating_r)
            self.image = self.eating_r[self.frame]

        elif self.random_movement == 'go_left':
            self.frame = ((self.step + 1)//20) % len(self.eating_l)
            self.image = self.eating_l[self.frame]

        self.step += 1
