# # # even_number=[i for i in range(1,101) if i%2==0]
# # # print(even_number)


# # # square=[i*i for i in range(11)]
# # # print(square)

# # # a=['apple','banana','orange']

# # # upper=[i.upper()for i in a ]
# # # print(upper)

# # # num=[i for i in range(1,11)]
# # # print(num)

# # # square=[i*i for i in range(1,11)]
# # # print(square)

# # # cube=[i**i for i in range(1,11)]
# # # print(cube)

# # # even=[i for i in range(1,21) if i%2==0]
# # # print(even)

# # # odd=[i for i in range(1,21) if i%2!=0]
# # # print(odd)

# # # number=[1,2,3,4,5]

# # # multiply=[i*2 for i in number]
# # # print(multiply)

# # # name=["krish","vedang","dhyey","bhavo"]

# # # upper=[name.upper() for name in name]
# # # print(upper)

# # # len_s=["krish","vedang","dhyey","bhavo"]

# # # length=[len(lens) for lens in len_s]
# # # print(length)

# # # divide=[i for i in range(1,51) if i%3==0]
# # # print(divide)

# # # evensquare=[i*i for i in range (1,21) if i%2==0]
# # # print(evensquare)

# # # numbers = [5, 12, 7, 18, 25, 3]
# # # greater=[i for i in numbers if i>10]
# # # print(greater)

# # # names = ["Krish", "Raj", "Amit", "Priya"]
# # # len=[i for i in names if len(i)>4]
# # # print(len)

# # # nums = [5, -2, 8, -1, 10, -7]
# # # negative=[i for i in nums if i>0]
# # # print(negative)

# # # text = "pythonprogramming"
# # # vowels=[i for i in text if i!="a" and i!="e" and i!="i" and i!="o" and i!="u"]
# # # print("".join(vowels))

# # # words = ["apple", "banana", "mango"]
# # # first=[word[0] for word in words ]
# # # print(first)

# # # nested = [[1, 2], [3, 4], [5, 6]]
# # # flattened=[i for row in nested for i in row]
# # # print(flattened)

# # # table=[5*i for i in range(1,11)]
# # # print(table)

# # # num=int(input("Enter table number :"))
# # # for i in range(1,11):
# # #   print(f"{num} x {i} = {num*i}")

# # # words = ["apple", "banana", "kiwi", "mango"]

# # # char=[word for word in words if len(word) > 5]
# # # print(char)

# # # matrix=[12,43,34]

# # # matrix.sort()
# # # print(matrix)

# # # add=lambda x,y : x*y
# # # print(add(10,20))

# # # num=[1,2,3,4,5,6]

# # # n= list(filter(lambda x: x%2==0, num))
# # # print(n)

# # # li=[12,45,78,96,35]

# # # def number(li):
# # #    total=sum(li)
# # #    maximum=max(li)
# # #    minimum=min(li)
# # #    print("sum :",total)
# # #    print("maximum :",maximum)
# # #    print("minimum :",minimum)

# # # number(li)

# # # class Car:
# # #    brand="toyota"
# # #    model="fortuner"
# # #    year=2025
# # #    type="disel"

# # # car1=Car()
 
# # # print("\nbrand :",car1.brand)
# # # print("model :",car1.model)
# # # print("year :",car1.year)
# # # print("type :",car1.type)

# # # class Laptop:
# # #    brand="laptop"
# # #    model="ideapad"
# # #    processer="ryzen 7"
# # #    price=50000

# # # laptop1=Laptop()

# # # print("\nbrand :",laptop1.brand)
# # # print("model :",laptop1.model)
# # # print("processer :",laptop1.processer)
# # # print("price :",laptop1.price)

# # # class Mobile:
# # #    brand=None
# # #    model=None
# # #    processer=None

# # # mobile1=Mobile()

# # # mobile1.brand="poco"
# # # mobile1.model="m6 plus"
# # # mobile1.processer="snapdragon 4 gen 2 SE"

# # # mobile2=Mobile

# # # mobile2.brand="moto"
# # # mobile2.model="g 45"
# # # mobile2.processer="snapdragon 4 gen 2"


# # # print("\nBrand :",mobile1.brand)
# # # print("Model ;",mobile1.model)
# # # print("processer :",mobile1.processer)

# # # print("\nBrand :",mobile2.brand)
# # # print("Model ;",mobile2.model)
# # # print("processer :",mobile2.processer)


# # # class City:
# # #    name=None
# # #    stat=None
# # #    country=None

# # # city1=City()

# # # city1.name="rajkot"
# # # city1.stat="gujarat"
# # # city1.country="india"

# # # city2=City()

# # # city2.name="new york city"
# # # city2.stat="New york"
# # # city2.country="America"

# # # print("\nCity :",city1.name)
# # # print("Stat :",city1.stat)
# # # print("Country :",city1.country)

# # # print("\nCity :",city2.name)
# # # print("Stat :",city2.stat)
# # # print("Country :",city2.country)


# # # class Ac:
# # #    __brand=None
# # #    __type=None
# # #    __warrenty=None

# # #    def setac(self):
# # #       self.__brand=input("\nEnter Ac brand :")
# # #       self.__type=float(input("Enter Ac type (TON) :"))
# # #       self.__warrenty=int(input("Enter Ac warrenty :"))

# # #    def getac(self):
# # #       print(f"\nAc brand : {self.__brand}")
# # #       print(f"Ac type : {self.__type}")
# # #       print(f"Ac warrenty : {self.__warrenty}")

# # # AC1=Ac()

# # # AC1.setac()
# # # AC1.getac()

# # # AC2=Ac()

# # # AC1.setac()
# # # AC1.getac()


# # # class People:

# # #    __fname=None
# # #    __lname=None
# # #    __age=None

# # #    def setinfo(self):
# # #       self.__fname=input("\nEnter your first name :")
# # #       self.__lname=input("Enter your last name :")
# # #       self.__age=int(input("Enter your age :"))

# # #    def getinfo(self):
# # #       print(f"\nyour full name is :{self.__fname} {self.__lname}")
# # #       print(f"your age is :{self.__age}")

# # # people1=People()

# # # people1.setinfo()
# # # people1.getinfo()


# # # class Bank:
# # #    __accnum=None
# # #    __balance=None
# # #    __ifsccode=None

# # #    def setbank(self):
# # #       self.__accnum=int(input("\nEnter your acc. no. :"))
# # #       self.__balance=int(input("Enter your acc. balance :"))
# # #       self.__ifsccode=str(input("Enter your acc. IFSC code :"))

# # #    def getbank(self):
# # #       print(f"\nyour acc. no. is : {self.__accnum}")
# # #       print(f"your acc. balance is : {self.__balance}")
# # #       print(f"your acc. IFSC code is : {self.__ifsccode}")
   
# # # bank1=Bank()

# # # bank1.setbank()
# # # bank1.getbank()

# # # class Car:
    
# # #    def __init__(self,brand,year,type="petrol"):
# # #         self.brand=brand
# # #         self.__year=year
# # #         self.type=type

# # #    def getcar(self):
# # #        print(f"Brand : {self.brand}")
# # #        print(f"Year : {self.__year}")
# # #        print(f"Type : {self.type}")
       
# # #    def __del__(self):
# # #       print("Task is over")

# # # car1=Car("ford",2026,)
# # # car2=Car("toyota",2025,"disel")

# # # car1.getcar()
# # # car2.getcar()

# # # print(car1.__year)    


# # # multiple obj 

# # # class Bank:

# # #     def __init__(self,name,account,branch,balance=10000):
# # #         self.name=name
# # #         self.__account=account
# # #         self.__balance=balance
# # #         self.branch=branch

# # #     def getbank(self):
# # #         print("\nHere is your account details !")
# # #         print(f"Bank name : {self.name}")    
# # #         print(f"Bank account no. : {self.__account}")
# # #         print(f"Bank balance : {self.__balance}")
# # #         print(f"Bank branch : {self.branch}")        

# # # bank_name=input("\nEnter your bank name :")
# # # bank_account=int(input("Enter your bank account no. :"))
# # # bank_branch=input("Enter your bank branch :")
# # # balance=input("Enter balance :")

# # # if len(balance)>=1:
# # #     bank1=Bank(bank_name,bank_account,bank_branch,balance)
# # # else:
# # #     bank1=Bank(bank_name,bank_account,bank_branch)


# # # bank1.getbank()

# # # class Laptop:

# # #     def __init__(self,brand,ROM,processer):
# # #       self.brand=brand
# # #       self.ROM=ROM
# # #       self.processer=processer

# # #     def getlaptop(self):
# # #        print("\nHere is your information !")
# # #        print(f"your  laptop brand is : {self.brand}")
# # #        print(f"your  laptop ROM is : {self.ROM}")
# # #        print(f"your  laptop processer is : {self.processer}")

# # # laptop_Brand=input("\nEnter your laptop brand :")
# # # rom=input("Enter your laptop RAM :")
# # # processer=input("Enter your laptop processer :")


# # # obj=Laptop(laptop_Brand,rom,processer)
# # # obj.getlaptop()

# # # class Mobile:

# # #     def __init__(self,brand,model,price,warrenty="5"):
# # #         self.brand=brand
# # #         self.model=model
# # #         self.__price=price
# # #         self.warrenty=warrenty

# # #     def getmobile(self):
# # #         print(f"your mobile brand : {self.brand}")
# # #         print(f"your mobile model is : {self.model}")
# # #         print(f"your mobile price is : {self.__price}")
# # #         print(f"your mobile warrenty is : {self.warrenty}")

# # # Brand=input("Enter your mobile brand :")
# # # model=input("Enter your mobile model :")
# # # price=int(input("Enter your mobile price :"))
# # # warrenty=input("Enter your mobile warrenty :")

# # # if len(warrenty)>=1:    
# # #     mobile=Mobile(Brand,model,price,warrenty)
# # # else:
# # #     mobile=Mobile(Brand,model,price,)

# # # mobile.getmobile()

# # # print(mobile.__price)
# # # print(mobile.model)

# # # class Car:

# # #     def __init__(self,brand,year,model,type="petrol"):
# # #         self.brand=brand
# # #         self.year=year
# # #         self.model=model
# # #         self.type=type

# # #     def getcar(self):
# # #         print(f"\nBrand : {self.brand}\nYear : {self.year}\nModel : {self.model}\nType : {self.type}")

# # #     def __del__(self):
# # #         print("\nTask is over")

# # # car1=Car('ford',1969,"mustang")

# # # car1.getcar()

# # # class Fruits:

# # #     def __init__(self,name,colour,price):
# # #         self.name=name
# # #         self.colour=colour
# # #         self.__price=price

# # #     def getfruits(self):
# # #         print(f"name : {self.name}")
# # #         print(f"colour : {self.colour}")
# # #         print(f"price : {self.__price}")

# # #     def __del__(self):
# # #         print("\nTask is over")

# # # fruit=input("Enter fruit name :")
# # # colour=input("Enter fruit colour :")
# # # price=int(input("Enter fruit price :"))

# # # fruit1=Fruits(fruit,colour,price)
# # # fruit1.getfruits()


# # # class Self:
# # #     def __init__(self,name,work):
# # #         self.name=name
# # #         self.work=work

# # #     def getself(self):
# # #         print(f"name:{self.name}")
# # #         print(f"work:{self.work}")

# # # obj=Self("keyword","current instance")
# # # obj.getself()
# # # del  obj
# # # print(obj.name)


# # # class private:
# # #     def __init__(self,name,age,gender):
# # #         self.name=name
# # #         self.age=age
# # #         self.gender=gender
    
# # #     def setprivate(self,gender):
# # #         self.gender=gender

# # #     def getdata(self):
# # #         print(f"name:{self.name}")
# # #         print(f"age:{self.age}")
# # #         print(f"gender :{self.gender}")

# # # obj=private("krish",17,"male")
# # # obj.getdata()
# # # obj.setprivate("female")
# # # print(obj.setprivate())

# # # li=[]

# # # a=input("Enter 7 fruits names :")
# # # li.append(a)
# # # print(li)

# # # a = (1,2,3,4,6,4,68,78,57,4)
# # # b=a.count(4)
# # # print(b)

# # # a=set()

# # # num1=int(input("Enter number :"))
# # # a.add(int(num1))

# # # num2=int(input("Enter number :"))
# # # a.add(int(num2))

# # # num3=int(input("Enter number :"))
# # # a.add(int(num3))

# # # num4=int(input("Enter number :"))
# # # a.add(int(num4))

# # # print(a)


# # # dict={}

# # # name=input("Enter friends name :")
# # # lan=input("Enter his language :")
# # # dict.update({name : lan})

# # # name=input("Enter friends name :")
# # # lan=input("Enter his language :")
# # # dict.update({name : lan})

# # # name=input("Enter friends name :")
# # # lan=input("Enter his language :")
# # # dict.update({name : lan})


# # # print(dict)

# # # a=int(input("Enter number A's value :"))
# # # b=int(input("Enter number B's value :"))

# # # if a>b:
# # #     print("A is grater than B")

# # # elif a<b:
# # #     print("B is grater than A")

# # # else:
# # #     print("Both value is euqueal! ")

# # # list = [1,23,34,6,7,8,78]
# # # list.append(100)
# # # list.pop(4)
# # # list.remove(23)
# # # print(list)

# # # for i in list:
# # #     print(i)

# # # dict = {
# # #     "krish" : 95,
# # #     "vedang": 78,
# # #     "dhyey" : 80,
# # #     "aayush": 79
# # #     }

# # # for keys,value in dict.items():
# # #     print(f"{keys} => {value}")

# # # print(dict["krish"])
# # # print(dict.items())

# # # for i in range(6):
# # #     for j in range(i-1):
# # #         print("*",end=" ")
# # #     print()


# # # num1=int(input("Enter number 1:"))
# # # num2=int(input("Enter number 2:"))
# # # num3=int(input("Enter number 3:"))
# # # num4=int(input("Enter number 4:"))

# # # if (num1>num2 and num1>num3 and num1>num4) :
# # #     print(f"Number 1 is greatest : {num1}")

# # # elif (num2>num1 and num2>num3 and num2>num4):
# # #     print(f"Number 2 is greatest : {num2}")

# # # elif (num3>num1 and num3>num2 and num3>num4):
# # #     print(f"Number 3 is graetest : {num3}")

# # # elif (num4>num1 and num4>num2 and num4>num3):
# # #     print(f"Number 4 is graetest : {num4}")
    
# # # else:
# # #     print("Invalid input")


# # # maths=int(input("Enter your Maths marks :"))
# # # sci=int(input("Enter your Science marks :"))
# # # eng=int(input("Enter your English marks :"))

# # # total_percentage= (maths + sci + eng)/3

# # # if (total_percentage>=40 and maths>=33 and sci>=33 and eng>=33):
# # #     print("Congratulations! you passed")

# # # else:
# # #     print("you have failed !")

# # # character=input("Enter your comment :")

# # # if (len(character))<=10:
# # #     print("Your comment have less than 10 character")

# # # else:
# # #     print("Your comment have more than 10 character")


# # # name=input("Enter your name :")
# # # list = ["krish","vedang","dhyey","bhavy","aayush"]

# # # if name in list:
# # #     print("Your name is in list")
# # # else:
# # #     print("Your name is not in list")

# # # marks=int(input("Enter your marks :"))

# # # if (marks<=100) and (marks>90):
# # #     grade="Ex"
# # # elif (marks<=90) and (marks>80):
# # #     grade="A"
# # # elif (marks<=80) and (marks>70):
# # #     grade="B"
# # # elif (marks<=70) and (marks>60):
# # #     grade="C"
# # # elif (marks<=60) and (marks>50):
# # #     grade="D"
# # # elif (marks<=50) and (marks>=00):
# # #     grade="F"

# # # print("Your grade is :",grade)

# # # i=1

# # # while (i < 51):
# # #     print(i)
# # #     i += 1

# # # i=1

# # # while (i<6):
# # #     print("harry")
# # #     i += 1

# # # list = [34,35,67,89,24,87]

# # # # for i in list:
# # # #     print(i)
# # # i=0

# # # while i<len(list):
# # #     print(list[i])
# # #     i += 1

# # # # 
# # # for i in range(100):
# # #      print(i)
# # #      if( i==50):
# # #        break

# # # i=0
      
# # # while i<=100:
# # #     i += 1
# # #     if i==50:
# # #         continue
# # #     print(i)

# # # for i in range(101):
# # #     if i==50:
# # #         continue
# # #     print(i)


# # # name="i am krish and i am 18 years old"
# # # count=0

# # # for i in name:
# # #     if i in "aeiouAEIOU":
# # #         count+=1

# # # print("Vowels :",count)

# # # count=0
# # # for i in range(101):
# # #     if i%3==0 or i%7==0:
# # #         count+=1

# # # print("count :",count)


# # # def fact(n):
# # #     if n==0:
# # #         return 0
# # #     elif n==1:
# # #         return 1
# # #     return fact(n-1)+fact(n-2)

# # # print(fact(10))

# # # def fact(n):
# # #     if n==1:
# # #         return 1
# # #     return n*fact(n-1)

# # # print(fact(5))
# # # rows=7
# # # for i in range(0,rows-1): 
# # #         for j in range(i):
# # #             print("*",end=" ")
# # #         print()

# # # number =int(input("Enter a number for creat a table :"))

# # # for i in range(1,11):
# # #     print(f"{number} x {i} = {number * i}")

# # # list=["krish","vedang","krishna","dhyey"]

# # # for name in list:
# # #     if name.startswith("k"):
# # #         print(f"hello {name}")

# # # num=int(input("Enter a number to creat a table :"))
# # # i=1

# # # while i<11:
# # #     print(f"{num} x {i} = {num*i}")
# # #     i+=1
        
# # # n=int(input("Enter a number to sum :"))
# # # sum=0
# # # i=0
# # # while i<n:
# # #     i+=1
# # #     sum+=i

# # # print(sum)

# # # n=int(input("Enter a number to sum :"))
# # # fact=1

# # # for i in range(1,n+1):
# # #     fact = fact * i

# # # print(fact)

# # # n=int(input("Enter a number :"))

# # # for i in range(1,n+1):
# # #     print(" " * (n-i),end="")
# # #     print("*" * (2*i-1),end="")
# # #     print()

# # # n=int(input("Enter a number :"))

# # # for i in range(1,n+1):
# # #     print(" "*(n-i),end="")
# # #     print("*"*(2*i-1),end="")
# # #     print()

# # # n=int(input("Enter a number :"))

# # # for i in range(1,n+1):
# # #     print(" "*(n-i),end="")
# # #     print("*"*(i),end="")
# # #     print()

# # # n=int(input("Enter a number :"))

# # # for i in range(1,n+1):
# # #     if (i==1) or (i==n):
# # #         print("*"*n,end="")
# # #     else:
# # #         print("*",end="")
# # #         print(" "*(n-2),end="")
# # #         print("*",end="")
# # #     print()
# # # n=int(input("Enter a number :"))

# # # for i in range(1,11):
# # #     print(f"{n} x {11-i} = {n*(11-i)}") 

# # # def factorial(n):
# # #     if n==1 or n==0:
# # #         return 1
# # #     return n * factorial(n-1)

# # # n=int(input("Enter a number :"))

# # # print(f"this number's factorial is : {factorial(n)}")

# # # n=int(input("Enter a number :"))
# # # factorial=1
# # # for i in range(n,0,-1):
# # #     factorial*=i

# # # print(factorial)

# # # import datetime

# # # now = datetime.datetime.now()
# # # print("Current Date & Time:", now)

# # # print(now.year)
# # # print(now.day)
# # # print(now.month)
# # # print(now.second)

# # # import datetime

# # # date_time=datetime.datetime.now()

# # # # print("now time is:", date_time)
# # # print(f"Now time is => {date_time.hour}:{date_time.minute}:{date_time.second}")
# # # *
# # # import random

# # # print('''Write s for Snake
# # # Write g for Gun
# # # Write w for Water
# # # ''')
# # # random_number=random.choice([0,-1,1])
# # # computer=random_number

# # # ask=input("Enter your choice :")

# # # dict={"s":-1, "w":1, "g":0}
# # # reverse_dict={1:"water" ,-1:"snake" ,0:"gun"}

# # # result=dict[ask]

# # # print(f"\nComputer chose {reverse_dict[random_number]}")
# # # print(f"You chose {reverse_dict[result]}\n")


# # # if(computer==result):
# # #         print("It's a Draw!")

# # # else:
    
# # #     if(computer==-1 and result==0):
# # #         print("You Win!")

# # #     elif (computer==-1 and result==1):
# # #         print("You Lose!")

# # #     elif (computer==1 and result==0):
# # #         print("You Lose!")

# # #     elif (computer==1 and result==-1):
# # #         print("You Win!")

# # #     elif (computer==0 and result==1):
# # #         print("You Win!")

# # #     elif (computer==0 and result==-1):
# # #         print("You Lose!")

# # # p=open("pra.txt")
# # # data=p.read()
# # # print(data)
# # # p.close()


# # # p=open("pra.txt")
# # # data=p.read()
# # # print(data)
# # # p.close()


# # # st="my name is krish "
# # # f=open("write.txt","w")
# # # f.write(st)
# # # f.close()

# # # string="i am Batman!"
# # # f=open("myfile.txt","w")
# # # f.write(string)
# # # f.close()

# # # f=open("pra.txt")
# # # line=f.readline()


# # # while line != "":
# # #     line=f.readline()
# # #     print(line)

# # # f.close()

# # # string="i am batman"
# # # f=open("batman.txt","w")
# # # f.write(string)
# # # f.close()

# # # f=open("write.txt","r")
# # # data=f.read()
# # # print(data)
# # # f.close()

# # # st="\nTell me do you Bleed!"
# # # f=open("write.txt","a")
# # # f.write(st)
# # # f.close()

# # # f=open("pra.txt","rb")
# # # data=f.read()
# # # print(data)
# # # f.close()

# # # with open("write.txt") as f:
# # #     data=f.read()
# # #     print(data)

# # # f=open("write.txt","r")
# # # data=f.read()
# # # print(data)
# # # f.close()

# # # string="Well here i am !"
# # # f=open("write.txt","a")
# # # f.write(string)
# # # f.close()

# # # st="you should thanking christ to give you me because you all need me,\nyou are nothing without me!"
# # # f= open("xyz.txt","w")
# # # f.write(st)
# # # f.close()

# # # f=open("xyz.txt")
# # # data=f.read()
# # # if ("christ" in data):
# # #     print("there is christ")

# # # else:
# # #     print("christ is not here")

# # # f.close()

# # # word="donkey"

# # # with open("xyz.txt","r") as f:
# # #     content=f.read()

# # # newcontent=content.replace("donkey","******")

# # # with open("xyz.txt","w") as f:
# # #     f.write(newcontent)

# # # words=["odyssey","home"]

# # # st="odyssey were not come for 20 years,and they forget their home"
# # # with open("xyz.txt","a") as f:
# # #     f.write(st)

# # # with open("xyz.txt","r") as f:
# # #     content=f.read()


# # # for word in words:
# # #     content=content.replace(word,"fahh")

# # # with open("xyz.txt","w") as f:
# # #     f.write(content)

# # # with open("pra.txt","r") as f:
# # #     content=f.read()

# # # if ("fight" in content ):
# # #     print("Yes, there is fight word")

# # # else:
# # #     print("No, there is not fight word")


# # # with open("pra.txt","r") as f:
# # #     lines=f.readlines()

# # # lineno=1
# # # for line in lines:
# # #     if "fight" in line:
# # #         print(f"yes, that word at line no.=>{lineno}")
# # #         break
# # #     lineno+=1

# # # else:
# # #     print("no, there is not such a word like this")

# # # with open("pra.txt","r") as f:
# # #     content=f.read()
    
# # # with open("write.txt","w") as f:
# # #     f.write(content)

# # # class Car:

# # #     def __init__(self,brand,model,type):
# # #         self.brand=brand
# # #         self.model=model
# # #         self.type=type

# # #     def setinfo(self,engine):
# # #         self.engine=engine

# # #     def getinfo(self):
# # #         print(f"Brand : {self.brand}")
# # #         print(f"Model : {self.model}")
# # #         print(f"Type : {self.type}")

# # # car=Car("toyota","2019","petrol")
# # # car.type="disel"

# # # car.getinfo()

# # # class Self:

# # #     def __init__(self,name,salary,language):
# # #         self.name = name
# # #         self.salary = salary
# # #         self.language = language

# # #     def getinfo(self):
# # #         print(f"Name : {self.name}")
# # #         print(f"Salary : {self.salary}")
        
# # # my=Self("krish","100000","python")

# # # my.getinfo()

# # class Programmer:
# #     company="Microsoft"

# #     def __init__(self,name,salary,pin):
# #         self.name=name
# #         self.salary=salary
# #         self.pin=pin

# #     def getinfo(self):
# #         print(f"Company :",self.company)
# #         print(f"Name : {self.name}")
# #         print(f"Salary : {self.salary}")
# #         print(f"PIN : {self.pin}")

# # mic=Programmer("krish","100000","360022")

# # mic.getinfo()

# # class calculator:

# #     def __init__(self,num):
# #         self.num=num

# #     def square(self):
# #         print(f"the Square of number : {self.num*self.num}")

# #     def cube(self):
# #         print(f"the Cube of the number : {self.num*self.num*self.num}")

# #     def root(self):
# #         print(f"the root of the number : {self.num**1/2}")


# # result=calculator(25)
# # result.square()
# # result.cube()
# # result.root()

# # from random import randint
# # class Railway:

# #     def __init__(self,fr,to):
        
# #         self.fr=fr
# #         self.to=to

# #     def getinfo(self):
# #         print(f"Train No. : {randint(111,11111)}")
# #         print(f"your Ticket is from {self.fr} to {self.to}")

# # train=Railway("rajkot","ahemdabad")
# # train.getinfo()

# # l = [1,2,3,4,5,6,7]

# # first , *all , last = l

# # print(first)
# # print(all)
# # print(last)


# # class Number:

# #     def __init__(self,n):
# #         self.n=n

# #     def __add__(self,b):
# #         return self.n + b.n


# # a=Number(1)
# # b=Number(2)

# # print(a+b)
        

# # class Twodvector:

# #     def __init__(self,i,j):
# #         self.i=i
# #         self.j=j

# #     def show(self):
# #         print(f"this is twoD vector => {self.i}+{self.j}")

# # class Threedvector(Twodvector):

# #     def __init__(self,i,j,k):
# #        super().__init__(i,j)
# #        self.k=k

# #     def show(self):
# #         print(f"this is threeD vector => {self.i}+{self.j}+{self.k}")

# # a=Twodvector(1,2)
# # a.show()

# # b=Threedvector(1,2,3)
# # b.show()

# # list=[1,2,3,4,5]

# # if len(list)>3:
# #     print("list has more than 3 elements")
# # else:
# #     print("list has less than 3 elements")

# # if(list:=len([1,2,3,4,5]))>3:
# #     print("list has more than 3 elements")
# # else:
# #     print("list has less than 3 elements")

# # age=int(input("enter your age =>"))

# # match age:
# #     case age if age>=18:
# #         print("you are an adult")
# #     case _:
# #         print("you are teenager")

# # a=int(input("Enter a number1 :"))
# # b=int(input("Enter a number2 :"))
# # choice=input("Enter your choice :")
# # match choice:
# #     case "+":
# #         print(a+b)
# #     case "-":
# #         print(a-b)
# #     case "*":
# #         print(a*b)
# #     case "/":
# #         print(a/b)
# #     case _:
# #         print("invalid choice!")


# # print(b" hello ")

# # try :
# #     for i in range (1,101):
# #         print("number",i)
# # except:
# #     print("Somthing is wrong!")

# # try :
# #     num=int(input("Enter your name :"))

# # except:
# #     print("Somthing is wrong!")

# # try:
# #     a=int(input("Enter a number 1 :"))
# #     b=int(input("Enter a number 2 :"))

# #     print(a*b)

# # except ValueError:
# #     print("Enter only numbers")

# # else:
# #     print("Calculation successfully completed!")

# # finally:
# #     print("Thank You!")

# # try:
# #     age=int(input("Enter your age : "))

# # except ValueError:
# #     print("Please enter only number!")

# # else:
# #     print(f"Your age is => {age}")

# # finally :
# #     print("Thank you!")

# # try:
# #     print("---Calculator---")
# #     a=int(input("Enter a number1 :"))
# #     b=int(input("Enter a number2 :"))

# #     c=input("Enter your operation you want to do:")

# #     if c=="+":
# #         print(a+b)

# #     elif c=="-":
# #         print(a-b)

# #     elif c=="*":
# #         print(a*b)

# #     elif c=="/":
# #         print(a/b)

# #     else:
# #         print("Invalid syntax!")

# # except ValueError:
# #     print("Enter only numbers!")

# # except ZeroDivisionError:
# #     print("Error:Zero division")

# # finally:
# #     print("Thank you!")

# # try:
# #     age=int(input("Enter your age:"))
# #     if age>=18:
# #         print("you are eligable!")
# #     else:
# #         print("sorry!,you are not eligable!")

# # except ValueError:
# #     print("please enter only number!")

# # else:
# #     print(f"your age is => {age}")

# # finally:
# #     print("Thank you !")

# # file=open("pra.txt","r")
# # data=file.read()
# # print(data)
# # file.close()

# # st="hello!"
# # with open("write.txt","w") as file:
# #     file.write(st)
    
# # string="world"
# # with open("write.txt","a") as file2:
#     # file2.write(string)

# # file=open("pra2.txt","x")
# # data=file.read()
# # print(data)
# # file.close()

# # with open("pra2.txt","w") as file:
# #     file.write("hello world!")

# # pip install numpy

# # import numpy as np

# import numpy as np

# # arr=np.array([10,20,30])
# # print(arr*10)

# # arr=np.arange(1,21)
# # print(arr)
# # print(sum(arr))
# # print(max(arr))
# # print(min(arr))
# # print((arr))

# # arr=np.array([
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ])
# # print(arr)
# # print(sum(arr))
# # print("shape :",arr.shape)
# # print("data type :",arr.dtype)
# # print("array dimension :",arr.ndim)
# # print("size :",arr.size)

# # marks = np.array([75, 82, 91, 68, 88])

# # print("Total marks:",sum(marks))
# # print("Average :",404/5)
# # print("Highest mark :",max(marks))
# # print("Lowest mark :",min(marks))

# # import math
# # # num=[10,20,30,40,50]
# # print(math.sqrt(25))
# # print(math.pi)


# # import oops

# # print(oops.add(10,20))

# # from random import randint
# # # num=randint(1,100)
# # numbers=[]
# # for i in range(10):
# #     numbers.append(randint(1,100))
# # print(numbers)

# # class Bike:
# #     company="Hero"
# #     name="Splendor"


# # bike1=Bike()
# # print(bike1.company,end=" ")
# # print(bike1.name)

# # class Person:

# #     def __init__(self,name,age,gender):
# #         self.name=name
# #         self.age=age
# #         self.gender=gender

# #     def get_data(self):
# #         print(f"Name : {self.name}")
# #         print(f"Age : {self.age}")
# #         print(f"Gender : {self.gender}")

# # person1=Person("krish",18,"Male")
# # person1.get_data()

# # class Mobile:

# #     # constractor
# #     def __init__(self,brand,name,battery):
# #         self.brand=brand
# #         self.name=name
# #         self.battery=battery

# #     def get_data(self):
# #         print(f"\nBrand : {self.brand}")
# #         print(f"Name : {self.name}")
# #         print(f"Battery : {self.battery}")

# # mobile1=Mobile("POCO","M6 Plus","5000 Mah")
# # mobile1.get_data()

# # class Movie:

# #     def __init__(self,name,writer):
# #         self.name=name
# #         self.writer=writer

# #     def get_data(self):
# #         print(f"\nMovie name : {self.name}")
# #         print(f"Movie writer : {self.writer}")

# # movie1=Movie("Game of Thrones","George R.R. martine")
# # movie1.get_data()


# # # constractor
# # class Story:

# #     def __init__(self):
# #         print("\nhello i am krish!")

# # story1=Story()

# # # class 1:
# # class College:

# #     collegename="S.v.virani"

# #     def __init__(self,fname,lname,course):
# #         self.fname=fname
# #         self.lname=lname
# #         self.course=course

# #     def display_data(self):
# #         print(f"College name : {self.collegename}")
# #         print(f"First name :{self.fname}")
# #         print(f"Last name :{self.lname}")
# #         print(f"Course name :{self.course}\n")

# # c1=College("Krish","Delvadiya","B.C.A")
# # c2=College("Alay","Sakhiya","B.C.A")

# # c1.display_data()
# # c2.display_data()


# # # class 2:
# # class Employee:

# #     company="Google"

# #     def __init__(self,name,age,salary,department):
# #         self.name=name
# #         self.age=age
# #         self.salary=salary
# #         self.department=department

# #     def display(self):
# #         print("\n---Here is the Details of Employee---")
# #         print(f"Company :{self.company}")
# #         print(f"Name :{self.name}")
# #         print(f"Age :{self.age}")
# #         print(f"Salary :{self.salary}")
# #         print(f"Department :{self.department}")

# # # name=input("Enter your name :")
# # # age=int(input("Enter your age :"))
# # # salary=int(input("Enter your salary :"))
# # # department=input("Enter your department :")
   

# # # e1=Employee(name,age,salary,department)
# # # e1.display()

# # e2=Employee("krish",18,25000,"hr")
# # e2.display()


# # # class 3:
# # class Laptop:

# #     def __init__(self,brand,model,ram,storage):
# #         self.brand=brand
# #         self.model=model
# #         self.ram=ram
# #         self.storage=storage

# #     def display(self):
# #         print(f"\nBrnad :{self.brand}")
# #         print(f"Model :{self.model}")
# #         print(f"RAM :{self.ram}")
# #         print(f"Storage :{self.storage}")

# # lap1=Laptop("Lenovo","ideapad","16gb","512gb")
# # lap1.display()

# # # class 4:

# # class Bank:

# #     def __init__(self,account_holder,account_number,balance):
# #         self.acc_holder=account_holder
# #         self.acc_number=account_number
# #         self.balance=balance

# #     def display(self):
# #         print(f"\nAccount Holder : {self.acc_holder}")
# #         print(f"Account Number : {self.acc_number}")
# #         print(f"Balance : {self.balance}")

# #     def deposite(self,amount):
# #         self.balance=self.balance + amount

# #     def withdraw(self,amount):
# #         self.balance=self.balance - amount

# # bank1=Bank("Krish","154445411",1000)
# # bank1.deposite(2000)
# # bank1.withdraw(500)
# # bank1.display()

# # # class 5:

# # class Mobile:

# #     brand="Samsung"

# #     def __init__(self,model,price,storage):
# #         self.model=model
# #         self.price=price
# #         self.storage=storage

# #     def display(self):
# #         print(f"\nModel :{self.model}")
# #         print(f"Price :{self.price}")
# #         print(f"Storage :{self.storage}")

# #     def display_price(self):
# #         print(f"\nPrice :{self.price}")

# #     def discount(self,percentage):
# #         discount=self.price * percentage/100
# #         self.price=self.price-discount

# # mobile1=Mobile("s24",90000,"256gb")
# # mobile1.display_price()
# # mobile1.discount(5)
# # mobile1.display()


# # # class 6:

# # class Car:

# #     def __init__(self,model,color,price):
# #         self.model=model
# #         self.color=color
# #         self.price=price

# #     def display_data(self):
# #         print(f"Model :{self.model}")
# #         print(f"Color :{self.color}")
# #         print(f"Price :{self.price}")

# #     def start(self):
# #         print("\nCar is starting!")

# #     def stop(self):
# #         print("Car is stopping!")

# # car1=Car("Toyota","black",5000000)

# # car1.display_data()
# # car1.start()
# # car1.stop()

# # # class 7:

# # class Store:

# #     def __init__(self,name,price,quantity):
# #         self.name=name
# #         self.price=price
# #         self.quantity=quantity

# #     def display_data(self):
# #         print(f'''\nName: {self.name}
# # Price :{self.price}
# # Quantity :{self.quantity}''')

# #     def total_price(self):
# #         total=self.price*self.quantity
# #         print("Total amount :",total)

# # store1=Store("Krish",200,5)
# # store1.display_data()
# # store1.total_price()


# # # class 8:

# # class Student:

# #     def __init__(self,name,maths,science,english):
# #         self.name=name
# #         self.maths=maths
# #         self.science=science
# #         self.english=english

# #     def display(self):
# #         print(f"\nName :{self.name}")
# #         print(f"Maths :{self.maths}")
# #         print(f"Science :{self.science}")
# #         print(f"English :{self.english}")

# #     def total_marks(self):
# #         total=self.maths+self.science+self.english
# #         print("\nTotal marks :",total)

# #     def percentage(self):
# #         per=(self.maths+self.science+self.english)/3
# #         print("Percentage :",per,"%")

# # st1=Student("Krish",90,47,98)

# # st1.display()
# # st1.total_marks()
# # st1.percentage()


# # # class 9:

# # class Movie:

# #     def __init__(self,name,genre,rating):
# #         self.name=name
# #         self.genre=genre
# #         self.rating=rating

# #     def display(self):
# #         print(f"\nName :{self.name}")
# #         print(f"Genre :{self.genre}")
# #         print(f"Rating :{self.rating}")

# #     def is_hit(self):
# #         if self.rating>7:
# #             print("\nThis movie is hit!")
# #         else:
# #             print("\nThis movie is flop!")

# # movie1=Movie("Krish","Adventure",6)
# # movie1.display()
# # movie1.is_hit()


# # # class 10:

# # class College:

# #     collegename="S.V.virani"

# #     def __init__(self,name,id,course,sem,maths,english,science):
# #         self.name=name
# #         self.id=id
# #         self.course=course
# #         self.sem=sem
# #         self.maths=maths
# #         self.english=english
# #         self.science=science

# #     def display(self):
# #         print(f"\nCollege name :{self.collegename}")
# #         print(f"Student name :{self.name}")
# #         print(f"Student ID :{self.id}")
# #         print(f"Course :{self.course}")
# #         print(f"Semester :{self.sem}")
# #         print(f"Maths :{self.maths}")
# #         print(f"English :{self.english}")
# #         print(f"Science :{self.science}")

# #     def calculate_per(self):
# #         total=self.maths+self.science+self.english
# #         per=(total)/3
# #         print(f"\nPercentage :{per}")

# #     def result(self):
# #         if self.maths+self.science+self.english>40:
# #             print("\nYou are passed!")
# #         else:
# #             print("\nyou are failed!")
            

# # college1=College("Krish",2513,"b.c.a.","sem=1",50,90,79)
# # college1.display()
# # college1.calculate_per()
# # college1.result()


# # class Student:

# #     def __init__(self,name,age,marks):
# #         self.name=name
# #         self.age=age
# #         self.set_marks(marks)

# #     def set_marks(self,marks):
# #         if marks>100 or marks<0:
# #             print("Invalid marks!")
# #         else:
# #             self.marks=marks

# #     def display(self):
# #         print(f"Name :{self.name}")
# #         print(f"Age :{self.age}")
# #         print(f"Marks :{self.marks}")

# # st1=Student("Krish",18,101)
# # st2=Student("Doom",18,99)

# # st1.display()
# # st2.display()

# # class Student:

# #     def __init__(self, name, age, marks):
# #         self.name = name
# #         self.age = age
# #         self.set_marks(marks)

# #     def set_marks(self, marks):
# #         if marks > 100 or marks < 0:
# #             print("Invalid marks!")
# #         else:
# #             self.marks = marks

# #     def display(self):
# #         print(f"Name : {self.name}")
# #         print(f"Age : {self.age}")
# #         print(f"Marks : {self.marks}")


# # st1 = Student("Krish", 18, 101)
# # st2 = Student("Doom", 18, 99)

# # st1.display()
# # st2.display()

# # class Student:

# #     def __init__(self, name, age, marks):
# #         self.name = name
# #         self.age = age
# #         # self.marks = 0
# #         self.set_marks(marks)

# #     def set_marks(self, marks):
# #         if 0 <= marks <= 100:
# #             self.marks = marks
# #         else:
# #             print("Invalid marks!")

# #     def display(self):
# #         print(f"Name : {self.name}")
# #         print(f"Age : {self.age}")
# #         print(f"Marks : {self.marks}")

# # st1 = Student("Krish", 18, 101)
# # st2 = Student("Doom", 18, 99)

# # st1.display()
# # st2.display()

# # class Student:

# #     def __init__(self, name, marks):
# #         self.name = name
# #         self.set_marks(marks)

# #     def set_marks(self, marks):
# #         if 0 <= marks <= 100:
# #             self.marks = marks
# #         else:
# #             print("Invalid marks")

# #     def display(self):
# #         print(f"Name : {self.name}")
# #         print(f"Marks : {self.marks}")


# # s1 = Student("Krish", 80)
# # s1.display()

# # # s1.set_marks(90)
# # print(s1.marks)

# # s1.set_marks(150)

# # class Student:

# #     def __init__(self, marks):
# #         self._marks = marks

# #     def get_marks(self):
# #         return self._marks


# # st1 = Student(90)
# # print(st1.get_marks())

# # class Student:

# #     def __init__(self, marks):
# #         self._marks = marks

# #     def marks(self):
# #         return self._marks


# # st1 = Student(90)

# # print(st1.marks())

# # class School:

# #     def __init__(self,name,marks):
# #         self.name=name
# #         self.marks=marks

# #     @property
# #     def get_marks(self):
# #         return self.marks

# #     def set_marks(self,marks):
# #         if 101>marks<=0:
# #             print(self.marks)
# #         else:
# #             print("Invalid marks !")

# # st1=School("Krish",98)
# # print(st1.get_marks)
# # # print(st1.name)


# # class Balance:

# #     def __init__(self,name,age,balance):
# #         self.name=name
# #         self.age=age
# #         self.__balance=balance

# #     @property
# #     def get_balance(self):
# #         return self.__balance

# #     @get_balance.setter
# #     def set_balance(self,amount):
# #         if self.__balance>0:
# #             self.__balance = amount
# #         else:
# #             print("Balance can't be in negative!")

# #     def display(self):
# #         print(f"\nName : {self.name}")
# #         print(f"Age : {self.age}")
# #         print(f"Balance : {self.__balance}")


# # bank=Balance("Krish",18,21212)
# # bank.display()
# # bank.amount=2156
# # print(bank.get_balance)
# from abc import ABC,abstractmethod
# from datetime import datetime

# class Person:

#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address

# class Customer(Person):

#     def __init__(self,name,age,address,customer_id):
#         super().__init__(name,age,address)
#         self.customer_id=customer_id

#     def display_data(self):
#         print(f"Name : {self.name}")
#         print(f"Age : {self.age}")
#         print(f"Address : {self.address}")
#         print(f"Customer ID : {self.customer_id}")

# class Account(ABC):
#     __totalaccount=0

#     def __init__(self,account_number,account_holder,balance=0):
#         self.account_number=account_number
#         self.account_holder=account_holder
#         self.__balance=balance
#         self.transaction = []
#         Account.__totalaccount += 1

#     @property
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self,amount):
        
#         if self.__balance<0:
#             print("Balance can not be Negative")

#         else:
#             self.__balance = amount

#     def deposite(self,amount):

#         if self.balance<0 and self.balance+amount<0:
#             print("Insufficient Balance")

#         else:
#             self.balance += amount

#         self.transaction.append({
#             "Type" : "Deposite",
#             "Amount" : amount,
#             "Time" : datetime.now()
#         })

#     def withdraw(self,amount):

#         if amount>self.balance:
#             print("Insufficient Balance")

#         else:
#             self.balance -= amount

#         self.transaction.apprnd({
#             "Type" : "Withdraw",
#             "Amount" : amount,
#             "Time" : datetime.now()
#         })

# class Savingsaccount(Account):

#     def __init__(self,account_number,account_holder,interest_rate,balance=0):
#         super().__init__(account_number,account_holder,balance,)
#         self.interest_rate=interest_rate


#     def add_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         self.balance += interest



# class Currentaccount(Account):


#     def __init__(self,account_number,account_holder,overdraft_limit,balance=0):
#         super().__init__(account_number,account_holder,balance)
#         self.overdraft_limit=overdraft_limit

#     def overdraft(self):
#         pass






    


       


#     '''
# print("===== BANK MANAGEMENT SYSTEM =====")
# print("1. Create New Account")
# print("2. Deposit Money")
# print("3. Withdraw Money")
# print("4. Transfer Money")
# print("5. Check Balance")
# print("6. Print Statement")
# print("7. View Total Accounts (classmethod)")
# print("8. Exit")

# choice=int(input("Enter your choice :"))

# if 
    
    
#     '''

# file=open("D:\\Python\\practice\\file.txt","r")
# print(file.read())
# file.close()

# file=open("D:\\Python\\practice\\file.txt","r")

# data=file.readline()
# data2=file.readline()

# print(data2)
# print(data)

# file.close()

# file=open("D:\\Python\\practice\\file.txt","r")
# data=file.readlines()
# for i in data:
#     print(i,end="")
# file.close()

# with open("sample.txt","r+") as file:
#     print(file.read())

# with open("sample.txt","w+") as file2:
#     print(file2.write("hello last"))

# try:
#     # data="raj"+10
#     # list=[0,1,2,3,4]
#     # print(list[73])
#     # student={
#     #     "name" : "krish",
#     #     "age" : 18
#     # }
#     # print(student["std"])
#     # data="krish"
#     print(dt)

# except ValueError:
#     print("incorrect value")
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except TypeError:
#     print("that's a type error")
# except IndexError:
#     print("Wrong indexing")
# except KeyError:
#     print("that key doesn't exists")
# except NameError:
#     print("that's name error")
# else:
#     pass

# print(int("raj"))


# class Age(Exception):

#     def __init__(self,age):
#         super().__init__(f"Age {age} is too young")


# num=int(input("Enter your age :"))

# if num<=18:
#     raise Age(num)
# else:
#     print("Access granted!")

# class AgeTooYoungError(Exception): 
#     def __init__(self, age):
#         super().__init__(f"Age {age} is too young! Minimum age is 18.")


# age = int(input("Enter your age: "))

# if age < 18:
#     raise AgeTooYoungError(age)
# else:
#     print("Access granted!")

# class Agelimit(Exception):
#     pass


# try:

#     age = int(input("Enter your age :"))

#     if age<18:
#         raise Agelimit("your age is too young")
#     else:
#         print("you are eligible!")

# except ValueError:

#     print("Please enter valid age")

# else:

#     print(f"Your age is {age}")

# finally:

#     print("Thank you!")

# try:
#     num1=int(input("Enter Number 1 :"))
#     num2=int(input("Enter Number 2 :"))

# except ZeroDivisionError:
#     print("can not divided by zero!")

# else:
#     print(num1/num2)

# finally:
#     print("operation executed")

# try:
#     number=[10,20,30,40,50]

#     index=int(input("Enter index to print number :"))

#     print(number[index])

# except IndexError:
#     print("Enter valid index!")

# else:
#     print(f"{index} is {print(number[index])}")

# finally:
#     print("Thank you!")


try:
    dict={"name":"krish",
          "age" : 18,
          "course" : "BCA"}

    key=input("Enter a key to print value :")

    print(dict[key])

except KeyError:
    print("Please enter a valid key")

finally:
    print("Thank you")


