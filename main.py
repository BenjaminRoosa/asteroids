# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
def main():
    pygame.init()
    clock =pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player(updateable, drawable, x= SCREEN_WIDTH/2, y= SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        for thing in updateable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
            
        
        pygame.display.flip()
        
        dt = (clock.tick(FRAME_RATE))/1000 
        
if __name__ == "__main__":
    main()