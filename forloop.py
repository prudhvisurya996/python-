for x in range(1,6):
    print("helloworld")
"""
helloworld printed six times
"""
a = [1, 2, 3, 4, 5]
for y in a:
    print(y)
"""
1
2
3
4
5
"""
for z in range(1,6):
    print(z)
"""
1
2
3
4
5---------prints 1 to 5
"""
for z1 in range(1,6,2):
    print(z1)
"""
prints 1,1+2,3+2=1,3,5
"""
for z2 in range(6,1,-2):
    print(z2)
"""
6 
4 
2
"""
i = 0
while i < 10:
    print(i)
    i+=2
"""
0
2
4
6
8
"""
j = 1
while j < 20:
    print(j)
    j *=5
"""
1 
1*5=5
5*5 fails as 25 > 20
"""