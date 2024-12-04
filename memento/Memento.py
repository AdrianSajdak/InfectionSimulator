from memento.IMemento import IMemento

class Memento(IMemento):
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state