print("welcome to the Interactive Personal Data Collecter! \n")

name=input("Please enter your name:")
age=input("Please enter your age:")
height=input("Please your height in meters:")
number=input("Please enter your favourite number:")

print("\nThank you! Here is the information We collected:")

year=2026 - int(age)

print("\nName:",name,"(type:",type(name),",memory address:", id(name),")")
print("Age:",age,"(type:",type(age),",memory address:",id(age),")")
print("Height::",height,"(type:",type(height),",memory address:",id(height),")")
print("Favourite Number:",number,"(type:",type(number),",memory address:",id(number),")\n")

print("your birth year is approximately:",year,"(based on your age of",age,")\n")

print("Thank you for using the personal Data Collecter.Goodbye!")

