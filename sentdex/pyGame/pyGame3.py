#https://www.youtube.com/watch?v=xh4SV3kF-zk&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=3
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

x_change = 0

crashed = False #Car isn't crashed.

#   GAME LOOP

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #If the player wants to quit the game
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    #x += x_change
    x = min(max(x + x_change, 0), display_width - 46)

    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)  #FPS

pygame.quit()
quit()
