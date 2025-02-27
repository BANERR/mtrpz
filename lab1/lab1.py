import math

# ax2+bx +c = 0

def solve_quadratic(a: float, b: float, c: float):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0.")
    
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant > 0:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        return ()

print(solve_quadratic(2, 1, -3))  # (-1.5, 1)
print(solve_quadratic(2, 4, 2))   # (-1)
print(solve_quadratic(1, 0, 9))   # ()
