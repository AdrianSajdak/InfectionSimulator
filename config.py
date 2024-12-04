# Simulation Constants
MAX_SPEED = 2.5  # [m/s]
TIME_STEP = 1 / 25  
INFECTION_DISTANCE = 2  # [m]
INFECTION_TIME = 3  # [s]
INFECTION_PROBABILITY_SYMPTOMATIC = 1.0  # 100%
INFECTION_PROBABILITY_ASYMPTOMATIC = 0.5  # 50%

# GUI Configurations
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)  # White

# Colors for different states
COLOR_HEALTHY = (0, 255, 0)         # Green
COLOR_SYMPTOMATIC = (255, 0, 0)     # Red
COLOR_ASYMPTOMATIC = (255, 165, 0)  # Orange
COLOR_RECOVERED = (0, 0, 255)       # Blue
COLOR_IMMUNE = (128, 0, 128)        # Purple


PERSON_RADIUS = 5  # Radius of the circle representing a person

# #SCENARIO 1
# IMMUNE_PROBABILITY = 0.0  # No initial immunity
#SCEANRIO 2
IMMUNE_PROBABILITY = 0.2  # 20% chance that an individual is immune

