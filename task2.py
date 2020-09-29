#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math

number = input("Enter a number")
x = float(number)
if (x**float(1.0/3)) % 1 == 0 and math.sqrt(x) % 1 == 0:
    print(number + " is both a perfect square and a perfect cube.")
elif math.sqrt(x) % 1 == 0:
    print(number + " is only a perfect square.")
elif (x**float(1.0/3)) % 1 == 0:
    print(number + " is only a perfect cube.")