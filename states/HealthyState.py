import random
from states.IState import State
from states.SymptomaticState import SymptomaticState
from states.AsymptomaticState import AsymptomaticState
from config import (
    INFECTION_DISTANCE,
    INFECTION_TIME,
    INFECTION_PROBABILITY_SYMPTOMATIC,
    INFECTION_PROBABILITY_ASYMPTOMATIC,
)

class HealthyState(State):
    def handle(self, person, environment):
        # Check for infection
        for other in environment.people:
            if other is not person and isinstance(other.state, (SymptomaticState, AsymptomaticState)):
                distance = person.position.distance_to(other.position)
                if distance <= INFECTION_DISTANCE:
                    if person.time_close_to(other) >= INFECTION_TIME:
                        infection_probability = (
                            INFECTION_PROBABILITY_SYMPTOMATIC
                            if isinstance(other.state, SymptomaticState)
                            else INFECTION_PROBABILITY_ASYMPTOMATIC
                        )
                        if random.random() <= infection_probability:
                            person.become_infected()
                            break
