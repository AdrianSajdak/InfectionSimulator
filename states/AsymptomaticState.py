from states.IState import State

class AsymptomaticState(State):
    def handle(self, person, environment):
        # Check if recovery time is over
        if person.infection_duration >= person.recovery_time:
            person.recover()
