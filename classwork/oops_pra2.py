class Employee:

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def getinfo(self):
        print(f"\nName : {self.name}")
        print(f"Age : {self.age}")
        print(f"Salary : {self.salary}")

    def __del__(self):
        pass

class Manager(Employee):

    def __init__(self,name,age,salary,department):
        super().__init__(name,age,salary)
        self.department=department

    def getinfo2(self):
        super().getinfo()
        print(f"Department : {self.department}")

    def __del__(self):
        pass

class Developer(Employee):

    def __init__(self,name,age,salary,programming):
        super().__init__(name,age,salary)
        self.pro=programming

    def getinfo3(self):
        super().getinfo()
        print(f"Progamming : {self.pro}")

    def __del__(self):
        pass

emp=[]
man=[]
dev=[]

while True:
    print('''\n---main menu---
1. Add Employee
2. Add Manager
3. Add Developer
4. Show Details''')
    
    choice=int(input("\nEnter your choice :"))

    if choice==1:

        name=input("\nEnter Employee name :")
        age=int(input("Enter Employee's age :"))
        salary=int(input("Enter Employee's salary :"))
        
        emp=Employee(name,age,salary)

        emp.getinfo()

        print("\nEmployee added successfully !")

    elif choice==2:

        name=input("\nEnter  Manager name :")
        age=int(input("Enter Manager's age :"))
        salary=int(input("Enter Manager's salary :"))
        Department=input("Enter Manager's department :")
        
        man=Manager(name,age,salary,Department)

        man.getinfo2()

        print("Manager added successfully !")

    elif choice==3:

        name=input("Enter Developer name :")
        age=int(input("Enter Developer's age :"))
        salary=int(input("Enter Developer's salary :"))
        programming=input("Enter DEveloper's programming language :")

        dev=Developer(name,age,salary,programming)

        dev.getinfo3()



    


