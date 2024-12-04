from abc import ABC, abstractmethod

class IMemento(ABC):
    @abstractmethod
    def get_state(self):
        pass
