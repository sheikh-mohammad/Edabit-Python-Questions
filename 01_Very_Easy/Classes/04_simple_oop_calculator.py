class Calculator:
    def add(self, num_1: int, num_2: int) -> int:
        return num_1 + num_2

    def subtract(self, num_1: int, num_2: int) -> int:
        return num_1 - num_2

    def multiply(self, num_1: int, num_2: int) -> int:
        return num_1 * num_2

    def divide(self, num_1: int, num_2: int) -> int:
        return num_1 // num_2
    
calculator = Calculator()

print(calculator.add(10, 5))

print(calculator.subtract(10, 5))

print(calculator.multiply(10, 5))

print(calculator.divide(10, 5))