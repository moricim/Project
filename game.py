import pygame
import ctypes
import spritesheet_functions
from player import Player
from goat_npc import GoatNPC
from chicken_npc import ChickenNPC
from sheep_npc import SheepNPC
from cow_npc import CowNPC
from pig_npc import PigNPC

pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

#makes the game window the specified size instead of enlarging it
ctypes.windll.user32.SetProcessDPIAware()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A Turkey's Tale")
clock = pygame.time.Clock()

player = Player()
goat = GoatNPC()
chicken = ChickenNPC()
chicken2 = ChickenNPC()
sheep = SheepNPC()
cow = CowNPC()
pig = PigNPC()

#music and sound effects
intro_music = pygame.mixer.Sound("intro_music.ogg")
moo = pygame.mixer.Sound("moo.ogg")
cluck = pygame.mixer.Sound("cluck.ogg")
gobble = pygame.mixer.Sound("gobble.ogg")
oink = pygame.mixer.Sound("oink.ogg")
baaa = pygame.mixer.Sound("baaa.ogg")

#images
intro_background1 = pygame.image.load("title_screen.png").convert()
intro_background2 = pygame.image.load("intro.png").convert()
intro_background3 = pygame.image.load("intro2.png").convert()
intro_background4 = pygame.image.load("instructions.png").convert()
sanctuary_background1 = pygame.image.load("sanctuary_background1.png").convert()
sanctuary_background2 = pygame.image.load("sanctuary_background2.png").convert()

stellabella = pygame.image.load("stella_bella.png").convert()
stellabellapic = pygame.image.load("stella_bella_pic.png").convert()
benny = pygame.image.load("benny.png").convert()
bennypic = pygame.image.load("benny_pic.png").convert()
louise = pygame.image.load("louise.png").convert()
louisepic = pygame.image.load("louise_pic.png").convert()
cameron = pygame.image.load("cameron.png").convert()
cameronpic = pygame.image.load("cameron_pic.png").convert()
belinda = pygame.image.load("belinda.png").convert()
belindapic = pygame.image.load("belinda_pic.png").convert()
weechee = pygame.image.load("weechee.png").convert() #<3

pic_position = [50, 50]
background_position = [0, 0]

pygame.mouse.set_visible(False)

#sets animals' initial positions
player.x_coord = 100
player.y_coord = 150
goat.x_coord = 600
goat.y_coord = 800
chicken.x_coord = 200
chicken.y_coord = 280
chicken2.x_coord = 250
chicken2.y_coord = 280
sheep.x_coord = 100
sheep.y_coord = 400
cow.x_coord = 640
cow.y_coord = 480
pig.x_coord = 340
pig.y_coord = 390

display_intro = True
intro_page = 1

display_dialogue = False
image_counter = 0

display_weechee = False

done = False

#---------------------Intro and instructions loop---------------------
while not done and display_intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            intro_page += 1

            if intro_page == 5:
                display_intro = False
                intro_music.fadeout(4000)

    screen.fill(BLACK)

    if intro_page == 1:
        screen.blit(intro_background1, background_position)
        intro_music.set_volume(0.3)
        intro_music.play()

    if intro_page == 2:
        screen.blit(intro_background2, background_position)

    if intro_page == 3:
        screen.blit(intro_background3, background_position)

    if intro_page == 4:
        screen.blit(intro_background4, background_position)

    clock.tick(60)
    pygame.display.flip()

#---------------------Main program loop---------------------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            elif event.key == pygame.K_RIGHT:
                player.go_right()
            elif event.key == pygame.K_UP:
                player.go_up()
            elif event.key == pygame.K_DOWN:
                player.go_down()
            elif event.key == pygame.K_g:
                gobble.play()
            elif event.key == pygame.K_w:
                display_weechee = True
                image_counter += 1
                if image_counter == 2:
                    display_weechee = False
                    image_counter = 0
            elif event.key == pygame.K_RETURN:
                display_dialogue = True
                image_counter += 1
                if image_counter == 3:
                    display_dialogue = False
                    image_counter = 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.stop()


    #-----Game Logic-----
    player.update()
    goat.update()
    chicken.update()
    chicken2.update()
    sheep.update()
    cow.update()
    pig.update()

    #player boundaries
    if 1 >= player.x_coord:
         player.x_coord = 2
    elif 736 <= player.x_coord:
        player.x_coord = 735
    if 255 >= player.y_coord:
        player.y_coord = 256
    elif 535 <= player.y_coord:
        player.y_coord = 534

    #goat NPC boundaries
    if 400 >= goat.x_coord:
         goat.x_coord = 401
    elif 500 <= goat.x_coord:
        goat.x_coord = 499
    if 300 >= goat.y_coord:
        goat.y_coord = 301
    elif 350 <= goat.y_coord:
        goat.y_coord = 349

    #sheep NPC boundaries
    if 25 >= sheep.x_coord:
        sheep.x_coord = 26
    if 250 <= sheep.x_coord:
        sheep.x_coord = 249
    if 390 >= sheep.y_coord:
        sheep.y_coord = 391
    if 500 <= sheep.y_coord:
        sheep.y_coord = 499

    #-----Drawing Code-----
    screen.fill(WHITE)
    screen.blit(sanctuary_background1, background_position)

    screen.blit(player.image, [player.x_coord, player.y_coord])
    screen.blit(goat.image, [goat.x_coord, goat.y_coord])
    screen.blit(chicken.image, [chicken.x_coord, chicken.y_coord])
    screen.blit(chicken2.image, [chicken2.x_coord, chicken2.y_coord])
    screen.blit(sheep.image, [sheep.x_coord, sheep.y_coord])
    screen.blit(cow.image, [cow.x_coord, cow.y_coord])
    screen.blit(pig.image, [pig.x_coord, pig.y_coord])

    if display_dialogue == True:
        if 190 <= player.x_coord <= 260 and 260 <= player.y_coord <= 300:
            cluck.play()
            if image_counter == 1:
                screen.blit(stellabella, pic_position)
            elif image_counter == 2:
                screen.blit(stellabellapic, pic_position)

        elif 410 <= player.x_coord <= 490 and 250 <= player.y_coord <= 380:
            baaa.play()
            if image_counter == 1:
                screen.blit(benny, pic_position)
            elif image_counter == 2:
                screen.blit(bennypic, pic_position)

        elif 30 <= player.x_coord <= 240 and 390 <= player.y_coord <= 520:
            baaa.play()
            if image_counter == 1:
                screen.blit(louise, pic_position)
            elif image_counter == 2:
                screen.blit(louisepic, pic_position)

        elif 520 <= player.x_coord <= 800 and 440 <= player.y_coord <= 535:
            moo.play()
            if image_counter == 1:
                screen.blit(belinda, pic_position)
            elif image_counter == 2:
                screen.blit(belindapic, pic_position)

        elif 340 <= player.x_coord <= 440 and 410 <= player.y_coord <= 480:
            oink.play()
            if image_counter == 1:
                screen.blit(cameron, pic_position)
            elif image_counter == 2:
                screen.blit(cameronpic, pic_position)

    if display_weechee == True:
        if image_counter == 1:
            cluck.play()
            screen.blit(weechee, [100,40])

    clock.tick(60)
    pygame.display.flip()


pygame.quit()
