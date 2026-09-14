def file_handling():

    while True :

        print('''\nFile Operation :
        1. Create a new file
        2. Write to a file
        3. Read from a file
        4. Append to a file
        5. Back to main file''')

        choice=int(input("\nEnter a choice :"))

        if choice==1:

            print("========================\n")

            name=input("Enter file name :") 
            with open(name,"x") as file:
                pass

            print("\nFile created successfully !")

            print("\n========================")

        elif choice==2:

            print("========================\n")

            name=input("Enter file name :")
            write=input("Enter data to write :")

            with open(name,"w") as file:
                file.write(write)

            print("\nData written successfully !")

            print("\n========================")

        elif choice==3:

            print("========================\n")

            name=input("Enter File name :")
            print("File contant :")

            with open(name,"r") as file:
                data = file.read()
                print(data)

            print("\n========================")

        elif choice==4:

            print("========================\n")

            name=input("Enter file name :")
            append=input("Enter data to append :")

            with open(name,"a") as file:
                file.write(append)

            print("\nData appended successfully !")

            print("\n========================")

        elif choice==5:

            print("========================\n")

            print("Thank you for using file operations !")

            print("\n========================")
            break

        else:
            print("\nInvalid choice !")