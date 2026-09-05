import datetime

file_name="D:\\Python\\projects\\journal.txt"

try:
    with open(file_name,"x") as data:
        pass
    
except FileExistsError:
    print("\nJournal file already exists !")

class JournalManager:

    def addentry(self):

        try:
            entry=input("\nEnter your journal entry : ")

            t=datetime.datetime.now()

            with open(file_name,"a") as file:
                file.write(f"[{str(t)}]\n{entry}\n\n")

            print("Entry added successfully !")

        except FileNotFoundError:
            print("\nError : The journal file could not be found !")

    def viewentries(self):

        try:
            with open(file_name,"r") as file:
                print("\n-----Your Journal Entries-----")
                print(file.read())

        except FileNotFoundError:
            print("\nError : The journal file could not be found !")


    def searchentry(self):

        try:
            with open(file_name,"r") as file:

                searchE=input("\nEnter a keyword or date to search your entry : ")

                data=file.read()
                entries=data.strip().split("\n\n")
                found=False

                print("\n----Search Results-----")
                for search in entries:
                    if searchE.lower() in search.lower():
                        found=True
                        print(search)
                        print()

                if not found:
                    print("\nNo entries found !")

        except FileNotFoundError:
            print("\nError : The journal file could not be found !")


    def delete_entry(self):

        try:
            permission=input("\nAre you sure you want to delete your Personal Entries (Yes/No): ")


            if permission.lower()=="yes":
                with open(file_name,"w") as file:
                    file.write("")
                    print("\nAll journal entries have been deleted !")

            else:
                pass

        except FileNotFoundError:
            print("\nError : The journal file could not be found !")


    def main(self):

            while True:
                print('''\n=====Welcome to Personal Journal Manager=====
                    
                Option:
                    1. Add a New Entry
                    2. View All Entries
                    3. Search for an Entry
                    4. Delete All Entries
                    5. Exit''')

                try:
                    choice=int(input("\nEnter your choice : "))

                except ValueError:
                    print("\nPlease enter only number for choice !")
                    continue

                if choice==1:
                    self.addentry()

                elif choice==2:
                    self.viewentries()

                elif choice==3:
                    self.searchentry()

                elif choice==4:
                    self.delete_entry()

                elif choice==5:
                    print("\nThank you for using Personal Journal Manager , Goodbye !")
                    break

                else:
                    print("\nPlease enter a valid choice !")

journal=JournalManager()
journal.main()