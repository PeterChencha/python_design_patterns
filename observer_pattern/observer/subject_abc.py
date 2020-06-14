from abc import ABCMeta, abstractmethod
from observer_abc import AbsObserver

class AbcSubject(metaclass = ABCMeta):
    """docstring for AbcSubject."""
    def __init__(self):
        self.observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        self.observers.add(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, value=None):
        for observer in self.observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)
