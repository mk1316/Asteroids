import pygame
from constants import *

def main():
    pygame.init()  #initailize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     #set screen size

    clock = pygame.time.Clock()                                         #setup game clock
    dt = 0


    while True:                                                         #Setting up game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()

        dt = clock.tick(60) /1000                                       #framerate to 60 FPS

        





    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()