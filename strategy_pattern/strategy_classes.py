from abc import ABCMeta, abstractmethod

class AbsStrategy(metaclass=ABCMeta):

    @abstractmethod
    def calculate(self, order):
        pass

class FedexStrategy(AbsStrategy):
    """docstring for FedexStrategy."""

    def calculate(self, order):
        return 3.00

class PostalStrategy(AbsStrategy):
    """docstring for PostalStrategy."""

    def calculate(self, order):
        return 5.00

class UPSStrategy(AbsStrategy):
    """docstring for UPSStrategy."""

    def calculate(self, order):
        return 4.00
