import math

class Circle:
    def __init__(self, radius: int | float) -> None:
        self.radius: int | float = radius

    def getArea(self) -> int | float:
        return math.pi * (self.radius**2)

    def getPerimeter(self) -> int | float:
        return 2 * math.pi * self.radius


circy1 = Circle(11)
print(circy1.getArea())

circy2 = Circle(4.44)
print(circy2.getPerimeter())
