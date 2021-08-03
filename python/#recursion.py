#recursion
#finding factorial of a given number

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
     #print(fact(5))


#write a recursive python function that returns the sum of the first n integers
def Sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+Sum(n-1)
print(Sum(10))
