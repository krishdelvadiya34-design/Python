class Employee:

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def showinfo(self):
        print(f"\nname : {self.name}")
        print(f"age : {self.age}")
        print(f"salary : {self.salary}")

    def __del__(self):
        pass

class Manager(Employee):

    def __init__(self,name,age,salary,department):
        super().__init__(name,age,salary)
        self.department=department

    def showinfo(self):
        super().showinfo()
        print(f"department : {self.department}")

    def __del__(self):
        pass

class Developer(Employee): 

    def __init__(self,name,age,salary,programming):
        super().__init__(name,age,salary)
        self.programming=programming

    def showinfo(self):
        super().showinfo()
        print(f"programming : {self.programming}")

    def __del__(self):
        pass



emp = []
man = []
dev = []

while True:
    print('''\nChoose an  option:
1. Create a Employee 
2. Create a Manager
3. Create a Developer
4. Show Details
5. Exit''')
    
    choice=int(input("\nChoose an option :" ))

    if choice==1:

        name=input("\nEnter Employee name :")
        age=int(input("Enter Employee's age :"))
        salary=int(input("Enter Employee's salary :"))

        eobj=Employee(name,age,salary)

        emp.append(eobj)

        print("\nEmployee is added successfully !")

        
    elif choice==2:

        name=input("\nEnter Manager name :")
        age=int(input("Enter Manager's age :"))
        salary=int(input("Enter Manager's salary :"))
        department=input("Enter Manager's department :")

        mobj=Manager(name,age,salary,department)

        man.append(mobj)

        print("\nManager added successfully !")

    elif choice==3:

        name=input("\nEnter Devloper name :")
        age=int(input("Enter Devloper's age :"))
        salary=int(input("Enter Devloper's salary :"))
        pro=input("Enter Devloper's programming :")

        dobj=Developer(name,age,salary,pro)

        dev.append(dobj)

        print("\nDeveloper added successfully !")

    elif choice==4:

        info=int(input("\nEnter 1/2/3 to show Emp/Mana/Dev =>"))

        if info==1:
            for em in emp:
                em.showinfo()

        elif info==2:
            for mana in man:
                mana.showinfo()

        elif info==3:
            for deve in dev:
                deve.showinfo()

        elif choice==4:
            print("\nInvalid choice !")

    elif choice==5:
        print("\nThank you !")
        break

    else:
        print("\nInvalid choice !")
