import random
import math
from vector import Vector
from position import Position
from config import MAX_SPEED, TIME_STEP

# Import states
from states.IState import State
from states.HealthyState import HealthyState
from states.SymptomaticState import SymptomaticState
from states.AsymptomaticState import AsymptomaticState
from states.RecoveredState import RecoveredState
from states.ImmuneState import ImmuneState

# Colors (make sure to import colors from config.py)
from config import (
    COLOR_HEALTHY,
    COLOR_SYMPTOMATIC,
    COLOR_ASYMPTOMATIC,
    COLOR_RECOVERED,
    COLOR_IMMUNE,
    PERSON_RADIUS,
    INFECTION_DISTANCE,
)

class Person:
    def __init__(self, position, environment, immune=False, infected=False):
        self.position = position
        self.environment = environment
        self.velocity = self.random_velocity()
        self.infection_duration = 0
        self.recovery_time = random.uniform(20, 30)
        self.close_contacts = {}
    
        if immune:
            self.state = ImmuneState()
        elif infected:
            self.become_infected()
        else:
            self.state = HealthyState()

    def random_velocity(self):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(0, MAX_SPEED)
        return Vector(math.cos(angle) * speed, math.sin(angle) * speed)

    def update(self):
        # Update position
        self.position = self.position.move(self.velocity)
        # Handle boundary conditions
        self.handle_boundaries()
        # Update state
        self.state.handle(self, self.environment)
        # Update infection duration if infected
        if isinstance(self.state, (SymptomaticState, AsymptomaticState)):
            self.infection_duration += TIME_STEP

    def handle_boundaries(self):
        x, y = self.position.x, self.position.y
        width, height = self.environment.width, self.environment.height

        if x <= 0 or x >= width or y <= 0 or y >= height:
            if random.random() < 0.5:
                self.velocity.x *= -1
                self.velocity.y *= -1
            else:
                self.environment.remove_person(self)

    def time_close_to(self, other):
        return self.close_contacts.get(other, 0)

    def update_close_contacts(self):
        for other in self.environment.people:
            if other is not self:
                distance = self.position.distance_to(other.position)
                if distance <= INFECTION_DISTANCE:
                    self.close_contacts[other] = self.close_contacts.get(other, 0) + TIME_STEP
                else:
                    self.close_contacts.pop(other, None)

    def become_infected(self):
        if random.random() < 0.5:
            self.state = SymptomaticState()
        else:
            self.state = AsymptomaticState()
        self.infection_duration = 0

    def recover(self):
        self.state = RecoveredState()

    def draw(self, screen, scale_x, scale_y):
        import pygame
        if self.is_healthy():
            color = COLOR_HEALTHY
        elif self.is_symptomatic():
            color = COLOR_SYMPTOMATIC
        elif self.is_asymptomatic():
            color = COLOR_ASYMPTOMATIC
        elif self.is_recovered():
            color = COLOR_RECOVERED
        elif self.is_immune():
            color = COLOR_IMMUNE
        else:
            color = (0, 0, 0)

        screen_x = int(self.position.x * scale_x)
        screen_y = int(self.position.y * scale_y)
        pygame.draw.circle(screen, color, (screen_x, screen_y), PERSON_RADIUS)

    def is_healthy(self):
        return isinstance(self.state, HealthyState)

    def is_symptomatic(self):
        return isinstance(self.state, SymptomaticState)

    def is_asymptomatic(self):
        return isinstance(self.state, AsymptomaticState)

    def is_recovered(self):
        return isinstance(self.state, RecoveredState)

    def is_immune(self):
        return isinstance(self.state, ImmuneState)
