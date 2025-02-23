import math

def calculate_area(base, height):
    return base * height

base = float(input("Enter the length of the base: "))
height = float(input("Enter the height of the parallelogram: "))

area = calculate_area(base, height)

print(f"The area of the parallelogram is: {area}")  