from math import sqrt

def quadratic_equation(a, b, c):
    x = int((-b + sqrt((b**2) - (4 * a * c))) / (2 * a))
    quad = (a * (x**2)) + b * x + c
    
    if (quad == 0):
        return x
    
print(quadratic_equation(1, 2, -3))
print(quadratic_equation(2, -7, 3))
print(quadratic_equation(1, -12, -28))
