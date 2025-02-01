from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def subtract(self, a, b):
        pass

    @abstractmethod
    def multiply(self, a, b):
        pass

    @abstractmethod
    def divide(self, a, b):
        pass

class BasicCalculator(ICalculator):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else "Cannot divide by zero"

b=BasicCalculator()
print(b.add(9,3))
print(b.add(6,2))
print(b.multiply(5,8))
print(b.subtract(60,4))
