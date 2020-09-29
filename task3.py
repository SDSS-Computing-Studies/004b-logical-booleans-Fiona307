#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""

number = input("Enter a number of any type")
x = float(number)

if x % 1 == 0 and x > 0:
    print(number + " is a positive integer.")
else:
    print(number + " is not a positive integer.")