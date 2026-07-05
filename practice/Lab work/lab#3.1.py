#question 1:

firstname=input("Enter your first name:")
lastname=input("Enter your last name:")

print(f"Hello,{lastname},{firstname}!")

#question 2:

item="Apple"
price=5.50

print(f"\nthe price of {item} is {price} dollars")

#question 3:

name="\nlevel\n"

print(name[::-1])

#question 4:





#question 5:

sentence=("\nMachine learning and AI are trending")
position=sentence.find("AI")
print(position)


new_sentence=sentence.replace("AI","Artificial Intelligence")
print(new_sentence)


li2=("\ndata data mining and big data")
print(li2)
count=li2.count("data")
print("number of times data appears:",count)

#question 6:

li=["apple","banana","grapes"]
li2=["python","is","awesome"]

li3=li+li2
print(li3)

re=" ".join(li2)
print(re)

for i in li3:
    print(i)

#question 7:

sen="hello new world!"
sen2=sen.startswith("hello") and sen.endswith("world!")
print(sen2)
