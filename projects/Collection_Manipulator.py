print("Welcome to student data organizer!")

students=[]

while True:

    print('''\nSelect an option:
            
    1. Add student
    2. Display all student
    3. Delete student
    4. Update student information
    5. Display subjects offered
    6. Exit''')

    choice=int(input("\nEnter your choice :"))

    if choice==1:
            
            st = {
                "Id" : (len(students)+101),
                "Name" : input("Name :"),
                "Age" : int(input("Age :")),
                "Grade" : input("Grade :"),
                "Date of Birth" : input("Date of Birth (YYYY-MM-DD) :"),
                "Subject" : set(input("Subjects (comma sepreted) :").split(","))
            }

            students.append(st)

            print("\nStudent added successfully!")

    elif choice==2:
            
            for st in students:
                print(f"Id : {st["Id"]} | Name : {st["Name"]} | Age : {st["Age"]} | Grade : {st["Grade"]} | Date of Birth : {st["Date of Birth"]} | Subject : {", ".join(st["Subject"])}")

    elif choice==3:
            
            stid=int(input("Enter student id to delete :"))
            found=False

            for st in students:
                if st["Id"]==stid:
                    found=True
                    students.remove(st)
                    print("\nStudent deleted successfully!")

                if found==False:
                    print("\nStudent not found!")

    elif choice==4:
            
            stid=int(input("Enter student id to update :"))
            found=False

            for st in students:
                if st["Id"]==stid:
                    found=True
                    st["Name"] = input("Name :")
                    st["Age"] = int(input("Age :"))
                    st["Grade"] = input("Grade :")
                    st["Date of Birth"] = input("Date of Birth (YYYY-MM-DD) :")
                    st["Subject"] = set(input("Subjects (comma sepreted) :").split(","))
                    print("\nStudent updated successfully!")

                if found==False:
                    print("\nStudent not found!")

    elif choice==5:

        all_subject=set()

        for st in students:
            all_subject.update(st["Subject"])
            
        print("\nSubject offered :",",".join(all_subject))

    elif choice==6:

        print("\nThank you!")
        break
    
    else:
        print("\nInvallid choice!")
                    




