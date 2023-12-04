"""
how to muliply a string
"""
a = "P"

print(a * 3)
#output:PPP

#what is structure of if else in python
"""
if condition:
    statement
else 
    statement
"""
#find whether adult or not an adult adult age >=18
age = int(input("ENTER YOUR AGE\n"))
if age >= 18:
    print("you are an adult")
else:
    print("you are not an adult")

#output ;26 you are an adult
#12 you are not an adult
"""
How to create a nested if in python
if condition:
    statement
elif condition:
     statement
elif  condition:
     statement
else condition:
     statement
"""
"""
A GRADE - 90 -100
B GRADE - 75 -89.9
C GRADE - 60 -74.9
"""
Percentage = int(input("ENTER YOUR MARKS PERCENTAGE\n"))
if Percentage >= 90:
    print("Passed with A Grade")
elif 75 <= Percentage <= 89:
    print("Passed with B Grade")
elif 60 <= Percentage <= 74:
    print("Passed with C Grade")
else:
    print("Failed")


