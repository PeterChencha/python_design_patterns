rom abc import ABCMeta, abstractmethod

class AbsObserver(metaclass = ABCMeta):
    """docstring for AbsObserver."""
    @abstractmethod
    def update(self, value):
        pass
