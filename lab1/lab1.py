import sys
import math
import os

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

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"Error. Expected a valid real number.")

def read_coefficients_from_file(filename):
    if not os.path.exists(filename):
        print(f"Error. File '{filename}' does not exist.")
        sys.exit(1)

    try:
        with open(filename, "r") as file:
            line = file.readline().strip()
            parts = line.split()
            if len(parts) != 3:
                raise ValueError("Invalid file format.")
            
            a, b, c = map(float, parts)
            return a, b, c
    except ValueError:
        print("Error. Invalid file format.")
        sys.exit(1)

def interactive_mode():
    print("Quadratic Equation Solver")
    a = get_float_input("a = ")
    while a == 0:
        print("Error. Coefficient 'a' cannot be 0.")
        a = get_float_input("a = ")
    
    b = get_float_input("b = ")
    c = get_float_input("c = ")

    return a, b, c

def main():
    if len(sys.argv) == 2:
        a, b, c = read_coefficients_from_file(sys.argv[1])
    else:
        a, b, c = interactive_mode()

    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")

    roots = solve_quadratic(a, b, c)
    if len(roots) == 2:
        print(f"There are 2 roots\nx1 = {roots[0]}\nx2 = {roots[1]}")
    elif len(roots) == 1:
        print(f"There are 1 roots\nx1 = {roots[0]}")
    else:
        print("There are 0 roots")

if __name__ == "__main__":
    main()
