# even_number=[i for i in range(1,101) if i%2==0]
# print(even_number)


# square=[i*i for i in range(11)]
# print(square)

# a=['apple','banana','orange']

# upper=[i.upper()for i in a ]
# print(upper)

# num=[i for i in range(1,11)]
# print(num)

# square=[i*i for i in range(1,11)]
# print(square)

# cube=[i**i for i in range(1,11)]
# print(cube)

# even=[i for i in range(1,21) if i%2==0]
# print(even)

# odd=[i for i in range(1,21) if i%2!=0]
# print(odd)

# number=[1,2,3,4,5]

# multiply=[i*2 for i in number]
# print(multiply)

# name=["krish","vedang","dhyey","bhavo"]

# upper=[name.upper() for name in name]
# print(upper)

# len_s=["krish","vedang","dhyey","bhavo"]

# length=[len(lens) for lens in len_s]
# print(length)

# divide=[i for i in range(1,51) if i%3==0]
# print(divide)

# evensquare=[i*i for i in range (1,21) if i%2==0]
# print(evensquare)

# numbers = [5, 12, 7, 18, 25, 3]
# greater=[i for i in numbers if i>10]
# print(greater)

# names = ["Krish", "Raj", "Amit", "Priya"]
# len=[i for i in names if len(i)>4]
# print(len)

# nums = [5, -2, 8, -1, 10, -7]
# negative=[i for i in nums if i>0]
# print(negative)

# text = "pythonprogramming"
# vowels=[i for i in text if i!="a" and i!="e" and i!="i" and i!="o" and i!="u"]
# print("".join(vowels))

# words = ["apple", "banana", "mango"]
# first=[word[0] for word in words ]
# print(first)

# nested = [[1, 2], [3, 4], [5, 6]]
# flattened=[i for row in nested for i in row]
# print(flattened)

# table=[5*i for i in range(1,11)]
# print(table)

# num=int(input("Enter table number :"))
# for i in range(1,11):
#   print(f"{num} x {i} = {num*i}")

# words = ["apple", "banana", "kiwi", "mango"]

# char=[word for word in words if len(word) > 5]
# print(char)

# matrix=[12,43,34]

# matrix.sort()
# print(matrix)

# add=lambda x,y : x*y
# print(add(10,20))

# num=[1,2,3,4,5,6]

# n= list(filter(lambda x: x%2==0, num))
# print(n)

# li=[12,45,78,96,35]

# def number(li):
#    total=sum(li)
#    maximum=max(li)
#    minimum=min(li)
#    print("sum :",total)
#    print("maximum :",maximum)
#    print("minimum :",minimum)

# number(li)

# class Car:
#    brand="toyota"
#    model="fortuner"
#    year=2025
#    type="disel"

# car1=Car()
 
# print("\nbrand :",car1.brand)
# print("model :",car1.model)
# print("year :",car1.year)
# print("type :",car1.type)

# class Laptop:
#    brand="laptop"
#    model="ideapad"
#    processer="ryzen 7"
#    price=50000

# laptop1=Laptop()

# print("\nbrand :",laptop1.brand)
# print("model :",laptop1.model)
# print("processer :",laptop1.processer)
# print("price :",laptop1.price)

# class Mobile:
#    brand=None
#    model=None
#    processer=None

# mobile1=Mobile()

# mobile1.brand="poco"
# mobile1.model="m6 plus"
# mobile1.processer="snapdragon 4 gen 2 SE"

# mobile2=Mobile

# mobile2.brand="moto"
# mobile2.model="g 45"
# mobile2.processer="snapdragon 4 gen 2"


# print("\nBrand :",mobile1.brand)
# print("Model ;",mobile1.model)
# print("processer :",mobile1.processer)

# print("\nBrand :",mobile2.brand)
# print("Model ;",mobile2.model)
# print("processer :",mobile2.processer)


# class City:
#    name=None
#    stat=None
#    country=None

# city1=City()

# city1.name="rajkot"
# city1.stat="gujarat"
# city1.country="india"

# city2=City()

# city2.name="new york city"
# city2.stat="New york"
# city2.country="America"

# print("\nCity :",city1.name)
# print("Stat :",city1.stat)
# print("Country :",city1.country)

# print("\nCity :",city2.name)
# print("Stat :",city2.stat)
# print("Country :",city2.country)


# class Ac:
#    __brand=None
#    __type=None
#    __warrenty=None

#    def setac(self):
#       self.__brand=input("\nEnter Ac brand :")
#       self.__type=float(input("Enter Ac type (TON) :"))
#       self.__warrenty=int(input("Enter Ac warrenty :"))

#    def getac(self):
#       print(f"\nAc brand : {self.__brand}")
#       print(f"Ac type : {self.__type}")
#       print(f"Ac warrenty : {self.__warrenty}")

# AC1=Ac()

# AC1.setac()
# AC1.getac()

# AC2=Ac()

# AC1.setac()
# AC1.getac()


# class People:

#    __fname=None
#    __lname=None
#    __age=None

#    def setinfo(self):
#       self.__fname=input("\nEnter your first name :")
#       self.__lname=input("Enter your last name :")
#       self.__age=int(input("Enter your age :"))

#    def getinfo(self):
#       print(f"\nyour full name is :{self.__fname} {self.__lname}")
#       print(f"your age is :{self.__age}")

# people1=People()

# people1.setinfo()
# people1.getinfo()


# class Bank:
#    __accnum=None
#    __balance=None
#    __ifsccode=None

#    def setbank(self):
#       self.__accnum=int(input("\nEnter your acc. no. :"))
#       self.__balance=int(input("Enter your acc. balance :"))
#       self.__ifsccode=str(input("Enter your acc. IFSC code :"))

#    def getbank(self):
#       print(f"\nyour acc. no. is : {self.__accnum}")
#       print(f"your acc. balance is : {self.__balance}")
#       print(f"your acc. IFSC code is : {self.__ifsccode}")
   
# bank1=Bank()

# bank1.setbank()
# bank1.getbank()

# class Car:
    
#    def __init__(self,brand,year,type="petrol"):
#         self.brand=brand
#         self.__year=year
#         self.type=type

#    def getcar(self):
#        print(f"Brand : {self.brand}")
#        print(f"Year : {self.__year}")
#        print(f"Type : {self.type}")
       
#    def __del__(self):
#       print("Task is over")

# car1=Car("ford",2026,)
# car2=Car("toyota",2025,"disel")

# car1.getcar()
# car2.getcar()

# print(car1.__year)    


# multiple obj 

# class Bank:

#     def __init__(self,name,account,branch,balance=10000):
#         self.name=name
#         self.__account=account
#         self.__balance=balance
#         self.branch=branch

#     def getbank(self):
#         print("\nHere is your account details !")
#         print(f"Bank name : {self.name}")    
#         print(f"Bank account no. : {self.__account}")
#         print(f"Bank balance : {self.__balance}")
#         print(f"Bank branch : {self.branch}")        

# bank_name=input("\nEnter your bank name :")
# bank_account=int(input("Enter your bank account no. :"))
# bank_branch=input("Enter your bank branch :")
# balance=input("Enter balance :")

# if len(balance)>=1:
#     bank1=Bank(bank_name,bank_account,bank_branch,balance)
# else:
#     bank1=Bank(bank_name,bank_account,bank_branch)


# bank1.getbank()

# class Laptop:

#     def __init__(self,brand,ROM,processer):
#       self.brand=brand
#       self.ROM=ROM
#       self.processer=processer

#     def getlaptop(self):
#        print("\nHere is your information !")
#        print(f"your  laptop brand is : {self.brand}")
#        print(f"your  laptop ROM is : {self.ROM}")
#        print(f"your  laptop processer is : {self.processer}")

# laptop_Brand=input("\nEnter your laptop brand :")
# rom=input("Enter your laptop RAM :")
# processer=input("Enter your laptop processer :")


# obj=Laptop(laptop_Brand,rom,processer)
# obj.getlaptop()

# class Mobile:

#     def __init__(self,brand,model,price,warrenty="5"):
#         self.brand=brand
#         self.model=model
#         self.__price=price
#         self.warrenty=warrenty

#     def getmobile(self):
#         print(f"your mobile brand : {self.brand}")
#         print(f"your mobile model is : {self.model}")
#         print(f"your mobile price is : {self.__price}")
#         print(f"your mobile warrenty is : {self.warrenty}")

# Brand=input("Enter your mobile brand :")
# model=input("Enter your mobile model :")
# price=int(input("Enter your mobile price :"))
# warrenty=input("Enter your mobile warrenty :")

# if len(warrenty)>=1:    
#     mobile=Mobile(Brand,model,price,warrenty)
# else:
#     mobile=Mobile(Brand,model,price,)

# mobile.getmobile()

# print(mobile.__price)
# print(mobile.model)

# class Car:

#     def __init__(self,brand,year,model,type="petrol"):
#         self.brand=brand
#         self.year=year
#         self.model=model
#         self.type=type

#     def getcar(self):
#         print(f"\nBrand : {self.brand}\nYear : {self.year}\nModel : {self.model}\nType : {self.type}")

#     def __del__(self):
#         print("\nTask is over")

# car1=Car('ford',1969,"mustang")

# car1.getcar()

# class Fruits:

#     def __init__(self,name,colour,price):
#         self.name=name
#         self.colour=colour
#         self.__price=price

#     def getfruits(self):
#         print(f"name : {self.name}")
#         print(f"colour : {self.colour}")
#         print(f"price : {self.__price}")

#     def __del__(self):
#         print("\nTask is over")

# fruit=input("Enter fruit name :")
# colour=input("Enter fruit colour :")
# price=int(input("Enter fruit price :"))

# fruit1=Fruits(fruit,colour,price)
# fruit1.getfruits()


# class Self:
#     def __init__(self,name,work):
#         self.name=name
#         self.work=work

#     def getself(self):
#         print(f"name:{self.name}")
#         print(f"work:{self.work}")

# obj=Self("keyword","current instance")
# obj.getself()
# del  obj
# print(obj.name)


class private:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def setprivate(self,gender):
        self.gender=gender

    def getdata(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"gender :{self.gender}")

obj=private("krish",17,"male")
obj.getdata()
obj.setprivate("female")
print(obj.setprivate())