#question 1:

# li=["apple","banana","chery","grapsh","watermelon"]

# li.append("mango")

# print(li)

# li.reverse()

# print("\nreverse the list:",li)

#question 2:

# t=(1,2,3,4,5)
# access=t.index(3)
# print(access)

# t(3)=7 typing error

#question 3:

# tu=(1,2,3)
# li=[1,2,3]

# tu(0)=7 because tuple is immutable
# li[0]=7
# print(li)

#question 4:

# li=[1,2,3,4,5,6,7,8,9,10]

# li2=[]

# for i in li:
#     li2.append(i**2)

# print(li2)

li=[]

for i in range(1,21):
    li.append(i)

print(li)
li2=[]

for i in li:
      if i%2==0:
       li2.append(i)
       
print(li2)

       