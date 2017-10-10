#https://www.youtube.com/watch?v=ZFo4mtLJEWs&index=2&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
import pygame

pygame.init()   #calls init function

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height)) #Sets the size of our display

pygame.display.set_caption('A bit Racey')   #Game's name, window's title

clock = pygame.time.Clock() #It's our specific game clock

carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

#x = (display_width * 0.45)
x = (display_width * 0.5 - 30)
#y = (display_height * 0.8)
y = (display_height - 69)

crashed = False #Car isn't crashed.

#   GAME LOOP

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #If the player wants to quit the game
            crashed = True

    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)  #FPS

pygame.quit()
quit()
