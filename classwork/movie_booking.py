from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self,name,age,mobile):
        self.name=name
        self.age=age
        self.mobile=mobile
    
    @abstractmethod
    def show_details(self):
        pass

class Customer(Person):
    id_counter=10001

    def __init__(self,name,age,mobile,customer_id):
        super().__init__(name,age,mobile)
        self.customer_id=Customer.id_counter

        Customer.id_counter += 1

    def show_details(self):
        print(f"Customer Name : {self.name}")
        print(f"Customer Age : {self.age}")
        print(f"Mobile Number : {self.mobile}")
        print(f"Customer ID : {self.customer_id}")

        
