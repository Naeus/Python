#https://www.youtube.com/watch?v=zMN9kRLD1DA&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=6
import pygame
import time
import random

pygame.init()   #calls init function

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 45

gameDisplay = pygame.display.set_mode((display_width, display_height)) #Sets the size of our display

pygame.display.set_caption('A bit Racey')   #Game's name, window's title

clock = pygame.time.Clock() #It's our specific game clock

carImg = pygame.image.load('racecar.png')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))   #puts the center of text rectange in the middle
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():

    #x = (display_width * 0.45)
    x = (display_width * 0.5 - 30)
    #y = (display_height * 0.8)
    y = (display_height - 69)

    x_change = 0

    thing_startx = random.randr ange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False #Car isn't crashed.

    #   GAME LOOP

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #If the player wants to quit the game
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        #x = min(max(x + x_change, 0), display_width - car_width)

        gameDisplay.fill(white)

        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)

        if (x > display_width - car_width) or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = -thing_height
            thing_startx = random.randrange(0, display_width)

        pygame.display.update()
        clock.tick(60)  #FPS

game_loop()
pygame.quit()
quit()
