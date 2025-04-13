from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20,50)
        new_vector1 = self.velocity.rotate(-rand_angle)
        new_vector2 = self.velocity.rotate(rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position[0],self.position[1],new_radius)
        new_asteroid1.velocity = new_vector1 * 1.2

        new_asteroid2 = Asteroid(self.position[0],self.position[1],new_radius)
        new_asteroid2.velocity = new_vector2 * 1.2