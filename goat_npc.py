import pygame
import random
from spritesheet_functions import SpriteSheet


class GoatNPC(pygame.sprite.Sprite):

    def __init__(self):

        #calls the parent's constructor
        super().__init__()

        self.next_move = pygame.time.get_ticks() + 2000
        self.random_movement = ""

        #speed vector
        self.change_x = 0
        self.change_y = 0

        #direction
        self.direction = ""

        self.frame = 0
        self.step = 0

        #holds walking animation images
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_up = []
        self.walking_frames_down = []

        #holds eating animation images

        sprite_sheet = SpriteSheet("goat.png")

        #loads up facing images onto the list
        image = sprite_sheet.get_image(30, 36, 72, 72)
        self.walking_frames_up.append(image)
        image = sprite_sheet.get_image(158, 36, 72, 72)
        self.walking_frames_up.append(image)
        image = sprite_sheet.get_image(286, 36, 72, 72)
        self.walking_frames_up.append(image)
        image = sprite_sheet.get_image(414, 36, 72, 72)
        self.walking_frames_up.append(image)

        #loads left facing images onto the list
        image = sprite_sheet.get_image(414, 172, 72, 72)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(286, 172, 72, 72)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(158, 172, 72, 72)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(30, 172, 72, 72)
        self.walking_frames_l.append(image)

        #loads down facing images onto the list
        image = sprite_sheet.get_image(30, 292, 72, 72)
        self.walking_frames_down.append(image)
        image = sprite_sheet.get_image(158, 292, 72, 72)
        self.walking_frames_down.append(image)
        image = sprite_sheet.get_image(286, 292, 72, 72)
        self.walking_frames_down.append(image)
        image = sprite_sheet.get_image(414, 292, 72, 72)
        self.walking_frames_down.append(image)

        #loads right facing images onto the list
        image = sprite_sheet.get_image(414, 424, 72, 72)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(286, 424, 72, 72)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(158, 424, 72, 72)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(30, 424, 72, 72)
        self.walking_frames_r.append(image)

        #sets the starting image of the player
        self.image = self.walking_frames_r[0]

    def update(self):

        self.x_coord += self.change_x
        self.y_coord += self.change_y

        self.movements = ['go_right', 'go_left', 'go_up', 'go_down']

        if pygame.time.get_ticks() >= self.next_move:
            self.next_move = pygame.time.get_ticks() + 1000
            self.random_movement = random.choice(self.movements)

        if self.random_movement == 'go_right':
            self.change_x = 1
            self.frame = ((self.step + 1)//15) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[self.frame]

        elif self.random_movement == 'go_left':
            self.change_x = -1
            self.frame = ((self.step + 1)//15) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[self.frame]


        elif self.random_movement == 'go_up':
            self.change_y = -1
            self.frame = ((self.step + 1)//15) % len(self.walking_frames_up)
            self.image = self.walking_frames_up[self.frame]

        elif self.random_movement == 'go_down':
            self.change_y = 1
            self.frame = ((self.step + 1)//15) % len(self.walking_frames_down)
            self.image = self.walking_frames_down[self.frame]

        self.step += 1
