import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()  #initailize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     #set screen size

    clock = pygame.time.Clock()                                         #setup game clock

    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    dt = 0

    while True:                                                         #Setting up game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        for item in updatable:
            item.update(dt)

        for item in asteroids:
           if item.collides_with(player):
               print("Game over!")
               sys.exit()


        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        

        dt = clock.tick(60) /1000                                       #framerate to 60 FPS

        

        
if __name__ == "__main__":
    main()