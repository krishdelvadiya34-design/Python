#question 1:

def fact(num):
    if num ==1:
        return 1
    return num*fact(num-1)

print(fact(5))

#question 2:

def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    return fib(num-1)+fib(num-2)

print(fib(5))

#question 3:




#question 4:

def squre(num):
    if num>1:
        return num*num
    else:
        return num
    
print(squre(0))