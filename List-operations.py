"""
How to create,append insert  find length and find specific value in a list
"""
x = [1,2,3,4,5]
y = ["a","b","c"]
z = [1,"a",2,"b"]

#How to dispaly a list
print(x)  # output [1, 2, 3, 4, 5]
print(y[0]) # output --a--this is slicing
print(z)  # [1, 'a', 2, 'b']

#How to add data at the end
x.append(6)
print(x)  # [1, 2, 3, 4, 5, 6]

#how to insert at specific positiom
y.insert(2,4)
print(y) #output['a', 'b', 4, 'c']

#how to find the legth of the string
print(len(z)) #output 4

#How to combine two strings
w = x + y
print(w) #output [1, 2, 3, 4, 5, 6, 'a', 'b', 4, 'c']

#can we mulitply a string in display:yes
print(z*3) #output [1, 'a', 2, 'b', 1, 'a', 2, 'b', 1, 'a', 2, 'b']


#How to find specific value in a string: we use "in" function
print(1 in x ) #output true indicates 1 is present in the list
print('k' in  y) #output false
print('$' in z) # output false

#How to substitute a a value in list
r = [1,2]
r[1] = 0
print(r) #output [1,0]