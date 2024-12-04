from states.IState import State

class SymptomaticState(State):
    def handle(self, person, environment):
        if person.infection_duration >= person.recovery_time:
            person.recover()