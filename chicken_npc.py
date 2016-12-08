import pygame
import random
from spritesheet_functions import SpriteSheet


class ChickenNPC(pygame.sprite.Sprite):

    def __init__(self):

        #calls the parent's constructor
        super().__init__()

        self.frame = 0
        self.step = 0

        self.next_move = pygame.time.get_ticks() + 3500
        self.random_movement = ""

        #holds eating animation images
        self.eating_r = []
        self.eating_l = []

        sprite_sheet = SpriteSheet("chicken_eat.png")

        #loads right facing images
        image = sprite_sheet.get_image(0, 96, 32, 32)
        self.eating_r.append(image)
        image = sprite_sheet.get_image(32, 96, 32, 32)
        self.eating_r.append(image)
        image = sprite_sheet.get_image(64, 96, 32, 32)
        self.eating_r.append(image)
        image = sprite_sheet.get_image(96, 96, 32, 32)
        self.eating_r.append(image)

        #loads left facing images
        image = sprite_sheet.get_image(0, 32, 32, 32)
        self.eating_l.append(image)
        image = sprite_sheet.get_image(32, 32, 32, 32)
        self.eating_l.append(image)
        image = sprite_sheet.get_image(64, 32, 32, 32)
        self.eating_l.append(image)
        image = sprite_sheet.get_image(96, 32, 32, 32)
        self.eating_l.append(image)

        self.image = self.eating_r[0]

    def update(self):

        self.movements = ['go_right', 'go_left']

        if pygame.time.get_ticks() >= self.next_move:
            self.next_move = pygame.time.get_ticks() + 3500
            self.random_movement = random.choice(self.movements)

        if self.random_movement == 'go_right':
            self.frame = ((self.step + 1)//10) % len(self.eating_r)
            self.image = self.eating_r[self.frame]

        if self.random_movement == 'go_left':
            self.frame = ((self.step + 1)//10) % len(self.eating_l)
            self.image = self.eating_l[self.frame]

        self.step += 1
