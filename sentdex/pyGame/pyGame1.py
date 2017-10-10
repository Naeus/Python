#https://www.youtube.com/watch?v=ujOTNg17LjI&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
import pygame

pygame.init()   #calls init function

gameDisplay = pygame.display.set_mode((800, 600)) #Sets the size of our display

pygame.display.set_caption('A bit Racey')   #Game's name, window's title

clock = pygame.time.Clock() #It's our specific game clock

crashed = False #Car isn't crashed.

#   GAME LOOP

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #If the player wants to quit the game
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)  #FPS

pygame.quit()
quit()
