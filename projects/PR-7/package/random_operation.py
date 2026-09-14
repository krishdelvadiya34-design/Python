import random

def numbers():

    while True:
        
        print('''\nRandom  Data Generation :
            1. Generate Random Number
            2. Generate Random List
            3. Create Random Password
            4. Generate Random OTP
            5. Back to Main Menu''')

        choice=int(input("\nEnter your choice :"))

        if choice==1:

            print("========================\n")

            print("---Give me the range of number---")

            number1 = int(input("Enter range 1 :"))
            number2 = int(input("Enter range 2 :"))

            data=random.randint(number1,number2)
            print(f"\nRandom Number :{data}")

            print("\n========================")

        elif choice==2:

            print("========================\n")

            data=[]
            list=int(input("Enter number of Elements :"))

            for i in range(list):
                result = random.randint(1000,10000)
                data.append(result)

            print(f"\nRandom List of {list} Elements:{data}")

            print("\n========================")

        elif choice==3:

            print("========================\n")

            character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            length = int(input("Enter password length :"))

            print("\nPassword :",end="")
            for i in range(length):
                data = random.choice(character)
                print(data,end="")

            print("\n========================")

        elif choice==4:

            print("========================\n")

            print(f"OTP :{random.randint(1000,9999)}")

            print("\n========================")

        elif choice==5:

            print("========================\n")

            print("Returning to main menu. Goodbye !")

            print("\n========================")
            break

        else:
            print("\nInvalid choice !")