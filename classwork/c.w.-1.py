li=[]

print("Welcome to our programme !")

while True:
       print('''\nSelect your choice :
       Enter 1 to create an array
       Enter 2 to read an array
       Enter 3 to delete an element of an array
       Enter 4 to update an element of an array
       Enter 0 to exit''')

       choice=int(input("\nEnter your choice  :"))

       if choice==1:
              num=int(input("\nEnter how many element you want to add :"))
              for i in range(num):
                   a=int(input(f"Enter the element no. {i+1} =>"))
                   li.append(a)

              print("\nArray is created !")

       elif choice==2:
              print()
              for i in li:
                   print(i,end=" ")
              print()

       elif choice==3:
              idx=int(input("\nEnter the index to remove the element :"))
              if idx>=0 and idx<len(li):
                    li.pop(idx)
                    print("\nElement removed !")
              else:
                    print("\ninvalid index !")

       elif choice==4:
              idx=int(input("\nEnter the index to remove the element :"))
              val=int(input("Enter the new value :"))
              if idx>=0 and idx<len(li):
                    li[idx]=val
                    print("\nElement updated !")
              else:
                    print("\ninvalid index !")

       elif choice==0:
             print("\nThank you !")
             break

       else:
             print("\ninvalid choice !")