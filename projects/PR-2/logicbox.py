print("welcome to the pattern generator and number analyzer!")

while True:
    print("\nSelect an Option:")
    print("\n1. Generate a Pattern")
    print("2. Analyze a Range of Number")
    print("3. Exit")
   

    choice=int(input("\nEnter your choice:"))

    match choice:
        case 1:

            print("\nEnter 1 for {*} pattern")
            print("Enter 2 for {1,2,3} pattern")

            sub_choice=int(input("\nEnter your choice:"))

            if choice==1:
             
                raw=int(input("\nEnter the number of raw for the pattern:"))
                print("\nThis is {*} pattern:")
                for i in range(1,raw+1):
                  for j in range(i):
                    print("*",end=(""))
                  print()
<<<<<<< HEAD

=======
        
>>>>>>> 52927d6 (project 3 complete)
            elif choice==2:
               
                raw=int(input("\nEnter the number of raw for the pattern:"))
                print("\nThis is {1,2,3} pattern:")
                for i in range(1,raw+1):
                  for j in range(i):
                    print(i,end=(""))
<<<<<<< HEAD
                  print()
=======
                print()
>>>>>>> 52927d6 (project 3 complete)

            else:
                print("Invalid choice")

        case 2:

            sum=0
            num1=int(input("\nEnter the start of the range:"))
            num2=int(input("Enter the end of the range:"))

            
            if num1>num2:
                for i in range(num1,num2-1,-1):
                    if i%2==0:
                        print(i,"is Even")
                    elif i%2!=0:
                        print(i,"is Odd")
                    elif i==0:
                        print(i,"is Neutral")
                    else:
                        print("Invalid")
<<<<<<< HEAD
                        
                    sum=sum+i
                    
=======

                    sum=sum+i

>>>>>>> 52927d6 (project 3 complete)
                print("\nSum of all numbers from",num1,"to",num2,"is:",sum) 
                

            else:
                for i in range(num1,num2+1):
                    if i%2==0:
                        print(i,"is Even")
                    elif i%2!=0:
                        print(i,"is Odd")
                    elif i==0:
                        print(i,"is Neutral")
                    else:
                        print("Invalid")
<<<<<<< HEAD
                        
                    sum=sum+i
                    
=======

                    sum=sum+i

>>>>>>> 52927d6 (project 3 complete)
                print("\nSum of all numbers from",num1,"to",num2,"is:",sum) 

        case 3:
            
            print("\nExiting the program.Goodbye!")
            break
                
