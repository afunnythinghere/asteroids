import pygame
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    
    # everything below is the game loop

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        for sprite in updatable:
            sprite.update(dt)
        milisec = clock.tick(60)
        dt = milisec/1000
        
        
        
        
        

    

    print("Starting Asteroids with pygame version: VERSION")
    print("Screen width: 1280")
    print("Screen height: 720")

if __name__ == "__main__":
    main()

