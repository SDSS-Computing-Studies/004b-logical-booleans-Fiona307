#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

a = input("Enter an integer")
b = input("Enter an integer")
c = input("Enter an integer")
x = float(a)
y = float(b)
z = float(c)

if x <= y and x <= z:
    if y <= z:
        if x**2 + y**2 == z**2:
            print(a+ "," + b + "," + c + " form a Pythagorean triple")
        else:
            print(a+ "," + b + "," + c + " do not form a Pythagorean triple")
    else:
        if x**2 + z**2 == y**2:
            print(a+ "," + c + "," + b + " form a Pythagorean triple")
        else:
            print(a+ "," + c + "," + b + " do not form a Pythagorean triple")
elif y <= x and y <= z:
    if x <= z:
        if x**2 + y**2 == z**2:
            print(b+ "," + a + "," + c + " form a Pythagorean triple")
        else:
            print(b+ "," + a + "," + c + " do not form a Pythagorean triple")
    else:
        if y**2 + z**2 == x**2:
            print(b+ "," + c + "," + a + " form a Pythagorean triple")
        else:
            print(b+ "," + c + "," + a + " do not form a Pythagorean triple")
else:
    if x <= y:
        if x**2 + z**2 == y**2:
            print(c+ "," + a + "," + b + " form a Pythagorean triple")
        else:
            print(c+ "," + a + "," + b + " do not form a Pythagorean triple")
    else:
        if y**2 + z**2 == x**2:
            print(c+ "," + b + "," + a + " form a Pythagorean triple")
        else:
            print(c+ "," + b + "," + a + " do not form a Pythagorean triple")