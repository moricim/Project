import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

class SpriteSheet(object):
    """Grabs images from a sprite sheet"""

    def __init__(self, file_name):
        """Constructor"""

        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """Grabs single image from sprite sheet"""

        #creates a new blank image
        image = pygame.Surface([width, height]).convert()

        #copies the sprite from the sheet onto the smaller image
        image.blit(self.sprite_sheet, (0,0), (x, y, width, height))

        #makes the background transparent
        image.set_colorkey(BLACK)

        return image
