import pickle
import pygame
from environment import Environment
from memento import Caretaker
from config import TIME_STEP, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR

class Simulation:
    def __init__(self, width, height, initial_population, scenario):
        self.environment = Environment(width, height, initial_population, scenario)
        self.time = 0
        self.caretaker = Caretaker(self.environment)
        self.running = True

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Infection Simulation")

        self.scale_x = SCREEN_WIDTH / width
        self.scale_y = SCREEN_HEIGHT / height

        self.font = pygame.font.SysFont(None, 24)

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.update_simulation()
            self.draw()
            pygame.display.flip()
            clock.tick(25)  # 25 frames per second

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.save('simulation_state.pkl')
                    print("Simulation state saved.")
                elif event.key == pygame.K_l:
                    self.load('simulation_state.pkl')
                    print("Simulation state loaded.")

    def update_simulation(self):
        self.environment.update()
        self.time += TIME_STEP

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        for person in self.environment.people:
            person.draw(self.screen, self.scale_x, self.scale_y)

        status_text = self.get_status_text()
        text_surface = self.font.render(status_text, True, (0, 0, 0))
        self.screen.blit(text_surface, (10, 10))

    def get_status_text(self):
        healthy = sum(1 for person in self.environment.people if person.is_healthy())
        symptomatic = sum(1 for person in self.environment.people if person.is_symptomatic())
        asymptomatic = sum(1 for person in self.environment.people if person.is_asymptomatic())
        recovered = sum(1 for person in self.environment.people if person.is_recovered())
        immune = sum(1 for person in self.environment.people if person.is_immune())

        return (f"Time: {int(self.time)}s | Healthy: {healthy} | "
                f"Symptomatic: {symptomatic} | Asymptomatic: {asymptomatic} | "
                f"Recovered: {recovered} | Immune: {immune} | Options: S|L")

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.environment, self.time), f)

    def load(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.environment, self.time = pickle.load(f)
                self.scale_x = SCREEN_WIDTH / self.environment.width
                self.scale_y = SCREEN_HEIGHT / self.environment.height
        except FileNotFoundError:
            print("Save file not found.")

    def quit(self):
        pygame.quit()
