print("Welcome to the Pattern Generator and Number Analyzer!\n")
print("Select an option:")
print("1. Right-angled Triangle")
print("2. Pyramid")
print("3. Left-angled Triangle")
print("4. Analyze a Range of Numbers")

choice=int(input("\nEnter your choice :"))

if choice==1:

    pattern =int(input("\nEnter how many line do you want to design:"))
    for i in range(pattern+1):
        print("*"*i)

elif choice==2:

    num=int(input("\nEnter how many line do you want to design:"))

    for i in range(1, num + 1):
        
        for j in range(num - i):
            print(" ", end="")

        for j in range(2 * i - 1):
            print("*", end="")

        print()

elif choice==3:

    num = int(input("\nEnter how many line do you want to design:"))

    for i in range(1, num + 1):

        for j in range(num - i):
            print(" ", end="")

        for j in range(i):
            print("*", end="")

        print()

elif choice==4:
    start = int(input("\nEnter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    total = 0

    for i in range(start, end + 1):

        if i % 2 == 0:
            print("Number",i,"is even")
        else:
            print("Number",i,"is odd")

        total = total + i

    print(f"\nSum of all numbers from {start} to {end} is: {total}")






