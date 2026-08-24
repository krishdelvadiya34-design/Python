class Vehicle:

    id_counter=1001

    def __init__(self,brand,model,rental_rate):
        self.__vehicle_id=Vehicle.id_counter
        self.brand=brand
        self.model=model

        self.new_rate(rental_rate)

        Vehicle.id_counter += 1

    def get_vehicle_id(self):
        return self.__vehicle_id
    
    def get__rental_rate(self):
        return self.__rental_rate
    
    def new_rate(self,new_rate):
        if new_rate >= 0:
            self.__rental_rate=new_rate
        
        else:
            print("Vehicle rate can not be Negative")
            self.__rental_rate=0

    def get_details_1(self):
        print(f"Vehicle ID : {self.__vehicle_id}")
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Rental rate : {self.__rental_rate}")

class Car(Vehicle):

    def __init__(self,brand,model,rental_rate,seating_capacity,fuel_type):
        super().__init__(brand,model,rental_rate)
        self.seating=seating_capacity
        self.type=fuel_type

    def get_details_2(self):
        print("\n---Car deatils---")
        super().get_details_1()
        print(f"Seating capacity : {self.seating}")
        print(f"Fuel type : {self.type}")

class Bike(Vehicle):

    def __init__(self,brand,model,rental_rate,engine_capacity,bike_type):
        super().__init__(brand,model,rental_rate)
        self.engine=engine_capacity
        self.bike=bike_type

    def get_details_3(self):
        print("\n---Bike deatils---")
        super().get_details_1()
        print(f"Engine capacity : {self.engine}")
        print(f"Bike type : {self.bike}")

cars = []
bikes = []

print("Welcome to our portal!")

while True:
    print('''\nSelect your choice:
1. add car
2. add bike
3. show details
4. delete vehicle
5. update vehicle
6. exit''')
    
    choice=int(input("\nEnter your choice :"))


    if choice==1:

        brand=input("\nEnter car brand:")
        model=int(input("Enter car model :"))
        rate=int(input("Enter car rental rate :"))
        seat=int(input("Enter car seating capacity :"))
        fuel=input("Enter car fuel type :")

        car1=Car(brand,model,rate,seat,fuel)

        cars.append(car1)

        print("\nCar added successfully !")

    elif choice==2:

        brand=input("\nEnter bike brand :")
        model=int(input("Enetr bike model :"))
        rate=int(input("Enter bike rental rate :"))
        engine=input("Enter bike engine capacity :")
        type=input("Enter bike type (Sports / Cruiser / Scooter) :")

        bike1=Bike(brand,model,rate,engine,type)

        bikes.append(bike1)

        print("\nBike added successfully !")

    elif choice==3:

        print("\nEnter 1 to show car details")
        print("Enter 2 to show bike details")

        sub_choice=int(input("\nSelect your choice :"))
      
        if sub_choice==1:

            for c in cars:
                c.get_details_2()
            
        elif sub_choice==2:

            for b in bikes:
                b.get_details_3()

    elif choice==4:

        print("\n---delete menu--- \nEnter 1 for delete car\nEnter 2 for delete bike ")

        del__choice=int(input("\nEnter your choice :"))

        if del__choice==1:
            d_id=int(input("\nEnter Vehicle ID to delete :"))
            found=False

            for car in cars:
                if car.get_vehicle_id()==d_id:
                    cars.remove(car)
                    found=True
                    print("\ncar deleted successfully !")
                    break

            if found==False:
                print("Invalid ID !")

        elif del__choice==2:
            d_id=int(input("\nEnter Vehicle ID to delete :"))
            found=False

            for b_ike in bikes:
                if b_ike.get_vehicle_id()==d_id:
                    bikes.remove(b_ike)
                    found=True
                    print("\nBike deleted successfully !")
                    break
            
            if found==False:
                print("Invalid ID !")

    elif choice==5:

        print("\n---update menu---\nEnter 1 for update car\nEnter 2 for update bike")

        up_choice=int(input("Enter your choice:"))

        if up_choice==1:
            u_id=int(input("Enter Vehicle ID to update :"))

            for b in bikes:
                if b.get_vehicle_id()==u_id:
                    bikes.update(b)

