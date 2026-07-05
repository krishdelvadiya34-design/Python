#question 1:

for i in range(1,21):
    if i%4==0:
        continue
    print(i)

#question 2:

i=0

while i<=10:
    if i==7:
        break
    i+=1
    print(i)


#question 3:

name=input("Enter your name:")

for i in name:
    if i in "AEIOUaeiou":
        continue
    print(i)
 

#question 4:

num=int(input("\nEnter a number of your choice:"))

for i in range(1,11,):
    print(num,"x",i,"=",num*i)


#question 5:

choice=int(input("Enter your choice number for pattern:"))

for i in range(1,choice+1):
    for j in range(i):
        print(i,end="")
    print()


#question 6:

choice=int(input("Enter your choice number for reverse pattern:"))

for i in range(choice,0,-1):
    for j in range(i):
        print(i,end="")
    print()

#question 7:

raws=int(input("Enter the number of raws:"))

for i in range(raws):
    for j in range(i+1):
        print(j+1,end="")
    print()