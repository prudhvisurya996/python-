'''
How to add two strings-concatination
'''

a = "PRUDHVI"
b = "SURYA"
#expected output PRUDHVISURYA
print(a + b)
# we use + for adding two strings
#can we add string to a integer --no
#can we add two integers which are strings
c = '10'
d = '20'
e = c + d
print(e)
#output -1020
#c and d are considered as strings hence result is 1020 not 30
#what if we want to add the numbers in the string
c = int(c)
d = int(d)
print(c + d )
#now the output is 30 here
#as we used int function to pick the integer part from the string
#take below example
"""
f = 'abc123'
g = 'def456'
h = int(f)
i = int(g)
print(i, h)---this wont work 
int function only works if the value in the string is numeric not alphanumeric
"""