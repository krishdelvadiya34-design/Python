#question 1:

while True:
    num=int(input("enter a 0 to exit:"))
    if num==0:
       break


#question 2:

for i in range(1,11):
    print(i*i)

# question 3:

i=1
while i<=49:
    i+=1
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")

#question 4:

for i in range(1,21):
    if i%2!=0:
      print(i,"is odd")


#question 5:

num=5

for i in range(1,11,1):
    print(num,"x",i,"=",num*i)

#question 6:

for i in range(10,0,-1):
    print(i)

#question 7:

for i in range(1,51):
  if i%2==0 and i%3==0:
      print(i,"\nDivisible by both 2 and 3")
  elif i%2==0:
      print(i,"\nDivisible by 2")
  elif i%2==0:
      print(i,"\nDivisible by 3")
  else:
      print(i,"\nthis is not divisible by 2 and 3")

print(i)
