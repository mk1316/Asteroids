import pygame
from constants import *
from player import *

def main():
    pygame.init()  #initailize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     #set screen size

    clock = pygame.time.Clock()                                         #setup game clock

    
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    dt = 0

    while True:                                                         #Setting up game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        for item in updateable:
            item.update(dt)

        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        

        dt = clock.tick(60) /1000                                       #framerate to 60 FPS

        

        
if __name__ == "__main__":
    main()