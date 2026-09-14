from datetime import datetime
import time

def dateandtime():

    while True:
        
        print('''\nDatetime and Time Operations :
            1. Display current Date and Time 
            2. Calculate difference between two dates/times
            3. Format date into custom format
            4. Stopwatch
            5. Countdown Timer
            6. Back to main menu''')

        choice=int(input("\nEnter your choice :"))

        if choice==1:
            print("========================")

            t = datetime.now().replace(microsecond=0)
            print(f"\nCurrent Date and Time : {t}")

            print("\n========================")


        elif choice==2:

            print("========================\n")

            date1=input("\nEnter first date (YYYY-MM-DD) :")
            date2=input("Enter second date (YYYY-MM-DD) :")

            date1=datetime.strptime(date1,"%Y-%m-%d")
            date2=datetime.strptime(date2,"%Y-%m-%d")

            difference=date2-date1

            print(f"\nDifference : {difference.days} days")

            print("\n========================")

        elif choice==3:

            print("========================\n")

            format = input("Enter date to custom (YYYY-MM-DD):")

            formatdata=datetime.strptime(format,"%Y-%m-%d")

            custom=formatdata.strftime("%d / %m / %Y")

            print("\nCustomized Date :",custom)

            print("\n========================")

        elif choice==4:

            print("========================\n")

            stopwatch = int(input("Enter stopwatch time (in Seconds):"))

            print(f"\n---- stopwatch will over in {stopwatch} seconds ----")
            for i in range(1,stopwatch+1):
                time.sleep(1)
                print(i)

            print("Time is over!")

            print("\n========================")

        elif choice==5:

            print("========================\n")

            countdown = int(input("Enter countdown time (in Seconds):"))

            print(f"\n---- countdown will over in {countdown} seconds ----")

            for i in range(countdown,0,-1):
                time.sleep(1)
                print(i)
                
            print("Time is over !")

            print("\n========================")

        elif choice==6:

            print("========================\n")

            print("Returning to main menu. Goodbye !")

            print("\n========================")
            break


        else:
            print("\nInvalid choice !")
