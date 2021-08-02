'''
#a function is a piece of code which runs when it is refered.
#it is used to utilize the code in more than one place in a program, in-built functions,user defined functions print(),input().

def add(x,y):
    return(x+y)
x=3
y=4
z=add(x,y)
print("z=",z)
#or else we can directly write-
#print(add(x,y)) or
print(add(30,40))

def square(x):
    return x*x
print(square(20))
'''
#Lambda function: It is an anonymous function or a function having no name.It is a small and restricted function
#having no more than one line
#lambda p1,p2:expression

'''adder=lambda x,y:x+y
print(adder(1,2))
import math
distance=lambda x,y:math.sqrt((x**2)+(y**2))
print(distance(4,5))'''

#map function-----> it is used to apply a particular operatin to every element in a sequece.

'''even_list=[2,4,6,8,10]

squared_even_list=map(lambda x:x*x,even_list )
print(list(squared_even_list))'''
