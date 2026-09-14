from package import dateandtime,file_handling,mathemetics,numbers,data,id

while True:

    print('''\n====Welcome to the Multi-Utility Toolkit====

    Options :
        1. Datetime and Time Operations
        2. Mathematical Operations
        3. Random Data Generation
        4. Generate Unique Indentifiers (UUID)
        5. File Operations (Custom Module)
        6. Explore Module Attributes (dir())
        7. Exit''')

    choice=int(input("\nEnter your choice :"))

    if choice==1:

        dateandtime()
        
    elif choice==2:

        mathemetics()

    elif choice==3:

        numbers()

    elif choice==4:

        id()

    elif choice==5:

        file_handling()

    elif choice==6:

        data()

    elif choice==7:

        print("========================")
        print("\nThank you for Multi-Utility Toolkit, goodbye !\n")
        print("========================")
        break

    else:
        print("Invalid choice !")
