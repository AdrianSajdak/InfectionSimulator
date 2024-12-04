import random
from position import Position
from person import Person
from config import IMMUNE_PROBABILITY

class Environment:
    def __init__(self, width, height, initial_population, scenario):
        self.width = width
        self.height = height
        self.people = []
        if scenario == 1:
            self.immune_probability = 0.0  # Scenario 1: No initial immunity
        elif scenario == 2:
            self.immune_probability = IMMUNE_PROBABILITY  # Scenario 2: Some have immunity

        # Create initial population
        for _ in range(initial_population):
            position = self.random_position_on_boundary()
            immune = random.random() < self.immune_probability
            infected = random.random() < 0.1
            person = Person(position, self, immune=immune, infected=infected)
            self.people.append(person)

    def random_position_on_boundary(self):
        if random.random() < 0.5:
            # On horizontal edges
            x = random.uniform(0, self.width)
            y = 0 if random.random() < 0.5 else self.height
        else:
            # On vertical edges
            x = 0 if random.random() < 0.5 else self.width
            y = random.uniform(0, self.height)
        return Position(x, y)

    def update(self):
        self.add_new_people()
        for person in list(self.people):
            person.update()
            person.update_close_contacts()

    def add_new_people(self):
        if random.random() < 0.1:
            position = self.random_position_on_boundary()
            immune = random.random() < self.immune_probability
            infected = random.random() < 0.1
            person = Person(position, self, immune=immune, infected=infected)
            self.people.append(person)

    def remove_person(self, person):
        self.people.remove(person)
