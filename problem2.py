#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""

a = input("Enter a number")
b = input("Enter another number")

if float(a) % float(b) == 0 or float(b) % float(a) == 0:
    if float(a) >= float(b):
        print(b.strip() + " is a factor of " + a)
    else:
        print(a + " is a factor of " + b)
else:
    if float(a) >= float(b):
        print(b.strip() + " is not a factor of " + a)
    else:
        print(a.strip() + " is not a factor of " + b)
