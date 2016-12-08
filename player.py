import pygame
from spritesheet_functions import SpriteSheet


class Player(pygame.sprite.Sprite):

    def __init__(self):

        #calls the parent's constructor
        super().__init__()

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

        sprite_sheet = SpriteSheet("turkey.png")

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
        image = sprite_sheet.get_image(30, 172, 72, 72)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(158, 172, 72, 72)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(286, 172, 72, 72)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(414, 172, 72, 72)
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
        image = sprite_sheet.get_image(30, 424, 72, 72)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(158, 424, 72, 72)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(286, 424, 72, 72)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(414, 424, 72, 72)
        self.walking_frames_r.append(image)

        #sets the starting image of the player
        self.image = self.walking_frames_down[0]

    def update(self):
        """Moves the player (this is where object collisions go)"""

        #moves left/right
        self.x_coord += self.change_x

        if self.direction == "R":
            self.frame = ((self.step + 1)//6) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[self.frame]

        elif self.direction == "L":
            self.frame = ((self.step + 1)//6) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[self.frame]

        #moves up/down
        self.y_coord += self.change_y

        if self.direction == "UP":
            self.frame = ((self.step + 1)//6) % len(self.walking_frames_up)
            self.image = self.walking_frames_up[self.frame]

        elif self.direction == "DOWN":
            self.frame = ((self.step + 1)//6) % len(self.walking_frames_down)
            self.image = self.walking_frames_down[self.frame]

        self.step += 1

    def go_left(self):
        self.change_x = -2
        self.direction = "L"

    def go_right(self):
        self.change_x = 2
        self.direction = "R"

    def go_up(self):
        self.change_y = -2
        self.direction = "UP"

    def go_down(self):
        self.change_y = 2
        self.direction = "DOWN"

    def stop(self):
        self.change_x = 0
        self.change_y = 0
        self.direction = ""
