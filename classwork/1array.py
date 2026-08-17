print("Welcome to our programme !")

li=[]

while True:
    print('''\nselect your choice :
    Enter 1 to create an array
    Enter 2 to find sum of all elements of an array
    Enter 3 to find the largest element of an array
    Enter 4 to find the smallest element of an array
    Enter 5 to count even and odd elements of an array
    Enter 6 to reverse an array
    Enter 7 to check if an element exists
    Enter 8 to count frequency of an element
    ''')

    choice=int(input("\nEnter your choice :"))

    if choice==1:
       
        n=int(input("Enter the number of elements in the array :"))

        for i in range(n):
            a=int(input(f"Enter element {i+1} :"))
            li.append(a)

        print("\nArray is created !")

    elif choice==2:

        total=0
        for i in li:
            total+=i
        print(f"\nSum of all elements in the array is : {total}")

    elif choice==3:

        largest=li[0]
        for i in li:
            if i>largest:
                largest=i

        print(f"\nLargest element in the array is : {largest}")

    elif choice==4:

        smallest=li[0]
        for i in li:
            if smallest>i:
                smallest=i

        print(f"\nsmallest element of an array is : {smallest}")

    elif choice==5:
        Even=0
        Odd=0

        for i in li:

            if i%2==0:
                Even+=1
            else:
                Odd+=1

        print(f"\nNumber of even elements  : {Even}")
        print(f"Number of odd elements  : {Odd}")

    elif choice==6:

        a=li[::-1]
        print(f"Reversed array is : {a}")

    elif choice==7:

        ele=int(input("Enter the element to check :" ))

        for i in li:
            if i==ele:
                print("Element exists in the array !")
                break

            else:
                print("Element does not exists in the array !")

    elif choice==8:

        ele=int(input("Enter the element to count frequency :"))

        count=0
        for i in li:
            if i==ele:
                count+=1

        print(f"Frequency of the element is : {count}")
        