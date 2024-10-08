# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *
def main():
    pygame.init()
    clock =pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_obj = Player( x= SCREEN_WIDTH/2, y= SCREEN_HEIGHT/2)
    AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        for thing in updateable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for i in asteroids:
            if i.collision(player_obj):
                print("Game over!")
                return
            for j in shots:
                if j.collision(i):
                    i.split()
        pygame.display.flip()
        
        dt = (clock.tick(FRAME_RATE))/1000 
        
if __name__ == "__main__":
    main()