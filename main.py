import pygame
pygame.init()
pygame.font.init()
import sys
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Pygame Score")
    font = pygame.font.SysFont("Arial", 30, True)
    clock = pygame.time.Clock()
    score = 0
    score_increment = 100
    dt = 0
    text_position = (10, 10)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    
    # everything below is the game loop

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, text_position)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        for sprite in updatable:
            sprite.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                print(f"Your score was {score}")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    score += score_increment
                    


        milisec = clock.tick(60)
        dt = milisec/1000
        
        
        
        
        

    

    print("Starting Asteroids with pygame version: VERSION")
    print("Screen width: 1280")
    print("Screen height: 720")

if __name__ == "__main__":
    main()

