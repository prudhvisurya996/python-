def fun1():
    print("helloworld")
    print("code reuse in muliple locations")
    print("i can use this  statements anywhere in fun1")
    a = 5
    b = 6
    print(a + b)

def fun2():
        print("helloworld")
        print("this is second function which i am using ")
        print("i can use this statements anywhere of this fun2")
        c = 7
        d = 9
        print(c * d)


fun1()
fun2()
"""
helloworld
code reuse in muliple locations
i can use this  statements anywhere in fun1
11
helloworld
this is second function which i am using 
i can use this statements anywhere of this fun2
63
"""