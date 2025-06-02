import sys
import os

# Dynamically add the parent directory (Python_Practice/) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from include.shapes import *
from include.calculator import *


def main():
    print("Circle area (r=3):", area_of_circle(3))
    print("Rectangle area (4x5):", area_of_rectangle(4, 5))
    print("Square area (side=6):", area_of_square(6))

    Sum_result = calculator(operations[0], 3, 4)
    print("Sum_result: ", Sum_result)

    subtract_result = calculator(operations[1], 10, 4)
    print("subtract_result: " , subtract_result)

    multiply_result = calculator(operations[2], 3, 4)
    print("multiply_result: ", multiply_result)

    division_result = calculator(operations[3], 10, 2)
    print("division_result: ", division_result)

if __name__ == "__main__":
    main()

# python3 main.py
