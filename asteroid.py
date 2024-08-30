import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius,):
        super().__init__(x, y, radius)
        self.velocity = 0
        self.containers = (asteroids, updateable, drawable)
        for group in self.containers:
            group.add(self)
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)
    def update(self, dt):
        
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            ran_angle = random.uniform(20,50)
            vct1 = self.velocity.rotate(ran_angle)
            vct2 = self.velocity.rotate(-ran_angle)
            child_radius = self.radius - ASTEROID_MIN_RADIUS
            child_1 = Asteroid(self.position.x, self.position.y, child_radius)
            child_2 = Asteroid(self.position.x, self.position.y, child_radius)
            child_1.velocity = vct1 * 1.2
            child_2.velocity = vct2 * 1.2