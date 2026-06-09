#question: 1
num=int(input("enter your number:"))

if num%2 == 0:
    print("even")
else:
    print("odd")

#question: 2

age=int(input("enter your age:"))

if age<=12:
    print("child")
elif age<=19:
    print("teenager")    
elif age<=59:
    print("adult")
else:
    print("senior")

#question: 3

a=int(input("enter num 1: "))
b=int(input("enter num 2: "))
c=int(input("enter num 3: "))

if a>b:
    if a>c:
        print("a")
    else:
        print("c")

else:
    if b>c:
        print("b")
    else:
        print("c")
    

#question: 4


number=int(input("enter a number:"))

if number<0:
     if number>1:
         print("this is an whole number")
else:
    print("this is a nuetral number")

    