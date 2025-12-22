class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def compare_age(self, other) -> str:
        if self.age > other.age:
            return f"{other.name} is younger than me"
        elif other.age > self.age:
            return f"{other.name} is older than me"
        elif self.age == other.age:
            return f"{other.name} is the same age as me."
        else:
            return "Error!"


p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

print(p1.compare_age(p2))
print(p2.compare_age(p1))
print(p1.compare_age(p3))
