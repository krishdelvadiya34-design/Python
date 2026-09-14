import math

def mathemetics():
        
    while True:

        print('''\nMathematical Operations :
            1. Calculate Factorial
            2. Solve compound Interest
            3. Trigonometric Calculations
            4. Area of Geometric Shapes
            5. Back to Main Menu''')

        choice = int(input("\nEnter your choice : "))

        if choice==1:

            print("========================\n")

            number = int(input("Enter a number : "))
            data = math.factorial(number)
            print(f"\nFactorial of {number} is :{data}")

            print("\n========================")

        elif choice==2:

            print("========================\n")

            amount = int(input("Enter principal amount : "))
            i_rate = int(input("Enter rate of interest (in %) : "))
            time = int(input("Enter time (in year) : "))

            for data in range(time):
                interest = (amount * i_rate)/100
                amount += interest 

            print(f"\nCompound Interest : {amount}")

            print("\n========================")

        elif choice==3:

            print("========================\n")

            angle_degree=int(input("Enter Angle degree (like:30,60,90) : "))
            data = math.radians(angle_degree)
            
            print(f"\nsin {angle_degree} degree : {math.sin(data)}")
            print(f"cos {angle_degree} degree : {math.cos(data)}")
            print(f"tan {angle_degree} degree : {math.tan(data)}")

            print("\n========================")

        elif choice==4:

            print("========================\n")

            print('''Options :
        1. Circle
        2. Square''')

            sub_choice = int(input("\nEnter your choice : "))

            if sub_choice==1:

                radius=int(input("\nEnter circle's radius (in cm) :"))
                result = math.pi*math.pow(radius,2)
                print(f"\nArea of Circle : {result} cm")

            elif sub_choice==2:

                size = int(input("\nEnter square's side(1) size (in cm) :"))
                result = math.pow(size,2)
                print(f"\nArea of Square :{result} cm")

            else:
                print("\nInvalid choice")

            print("\n========================")

        elif choice==5:

            print("========================\n")
            
            print("Returning to main menu. Goodbye !")

            print("\n========================")
            break

        else:
            print("\nInvalid choice !")


