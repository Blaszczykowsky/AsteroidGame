import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            rnd_angle = random.uniform(20, 50)
            new_velocity = self.velocity.rotate(rnd_angle)
            scnd_velocity = self.velocity.rotate(-rnd_angle)
            first_ast = Asteroid(self.position.x, self.position.y, new_radius)
            scnd_ast = Asteroid(self.position.x, self.position.y, new_radius)
            first_ast.velocity = new_velocity * 1.2
            scnd_ast.velocity = scnd_velocity * 1.2
