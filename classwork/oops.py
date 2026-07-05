# class father:

#     def __init__(self,name,age,):
#         self.name=name
#         self.age=age

#     def getinfo(self):
#         print("hello from father !")
        
# class Son(father):

#     def __init__(self,name,age,school):
#         super().__init__(name,age)
#         self.school=school

#     def getinfo2(self):
#         print("hello from son !")

# family=Son("krish",17,"raw")
# family.getinfo()
# family.getinfo2()

# class Father:
#     name="vijaybhai"

#     def greet(self):
#         print("Hello from father")

# class Son(Father):
#     pass
 
# obj=Son()
# print(obj.name)
# obj.greet()

# class Friend1:

#     def __init__(self,name,age):
#       self.name=name
#       self.age=age

#     def greet1(self):
#         print(f"Hi from {self.name}")
#         print(f"My age is {self.age}")
        
# class Friend2(Friend1):

#     def __init__(self,name,age,school):
#         super().__init__(name,age)
#         self.school=school

#     def greet2(self):
#         super().greet1()
#         print(f"I am studing in {self.school}")

# obj=Friend2("krish",17,"raw")
# obj.greet1()        
# obj.greet2()

# class Mobile:

#     def mobile1(self):
#         print("Hello from mobile 1")


# class Mobile2(Mobile):

#     def real(self):
#         print("Hello from mobile 2")

# obj=Mobile2()
# print(obj.mobile1())
# print(obj.real())

# class Father:
#     def greet1(self):
#         print("Hello from father")

# class Mother:
#     def greet2(self):
#         print("Hello from mother")

# class Child(Father,Mother):
#     def greet3(self):
#         print("Hello from son")

# c=Child()
# c.greet1()
# c.greet2()
# c.greet3()

# class Grandfather:
#     def greet1(self):
#         return "Hello from grandfather"
    
# class Father(Grandfather):
#     def greet2(self):
#         return "Hello from father"
    
# class Child(Father):
#     def greet3(self):
#         return "Hello from child"
    
# obj=Child()
# print(obj.greet1())
# print(obj.greet2())
# print(obj.greet3()) 

# class Grandfather:
#       def gr_method(self):
#             print("Hello from grandfather")

# class father(Grandfather):
#       def ft_method(self):
#             print("Hello from father")

# class Son(Grandfather):
#       def son_method(self):
#             print("Hello from son")

# family=Son()
# family2=father()

# family.gr_method()
# family.son_method()
# family2.ft_method()
# family2.gr_method()


# class A:
#       def __init__(self,name,rank):
#             self.name=name
#             self.rank=rank

#       def getdata1(self):
#             print("This is from A")

# class C(A):
#       def __init__(self,name,rank):
#             super().__init__(name,rank)

#       def getdata3(self):
#             print("This is from C")

# obj=C("cat",3)
# obj2=A("apple",1)

# obj.getdata3()
# obj2.getdata1()

# print("name :",obj2.name,"Rank :",obj2.rank)
# print("name :",obj.name,"Rank :",obj.rank)

