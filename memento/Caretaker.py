import pickle
from memento.Memento import Memento

class Caretaker:
    def __init__(self, originator):
        self.originator = originator
        self.mementos = []

    def save(self):
        state = pickle.dumps(self.originator)
        self.mementos.append(Memento(state))

    def restore(self, index):
        state = self.mementos[index].get_state()
        self.originator = pickle.loads(state)
        return self.originator