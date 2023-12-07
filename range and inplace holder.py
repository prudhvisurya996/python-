#How to define a range and how to use inplace holder
x = list(range(1,10))
print(x)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

y = range(1,6)
print(y)
#range(1, 6)

#multiples of 5 between 1 to 30
z = list(range(0,30,5))
print(z)
#[0, 5, 10, 15, 20, 25]
"""
starting number =0 
limit =30 excluding 30
difference should be +5
"""
a = list(range(30,0,-5))
print(a)
#[30, 25, 20, 15, 10, 5] exlcudes 0

#inplace holder
i = 1
i+=2 #equals to i =i + 2
print(i)
#3