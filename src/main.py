import sys
import os

# Dynamically add the parent directory (Python_Practice/) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from include.shapes import *


def main():
    print("Circle area (r=3):", area_of_circle(3))
    print("Rectangle area (4x5):", area_of_rectangle(4, 5))
    print("Square area (side=6):", area_of_square(6))

if __name__ == "__main__":
    main()

