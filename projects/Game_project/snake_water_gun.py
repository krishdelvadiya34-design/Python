import random

def game():
    print('''Write s for Snake
Write g for Gun
Write w for Water
    ''')
    random_number=random.choice([0,-1,1])
    computer=random_number

    ask=input("Enter your choice :")

    dict={"s":-1, "w":1, "g":0}
    reverse_dict={1:"water" ,-1:"snake" ,0:"gun"}

    result=dict[ask]

    print(f"\nComputer chose {reverse_dict[random_number]}")
    print(f"You chose {reverse_dict[result]}\n")


    if(computer==result):
            print("It's a Draw!\n")

    else:
        
        if(computer==-1 and result==0):
            print("You Win!\n")

        elif (computer==-1 and result==1):
            print("You Lose!\n")

        elif (computer==1 and result==0):
            print("You Lose!\n")

        elif (computer==1 and result==-1):
            print("You Win!\n")

        elif (computer==0 and result==1):
            print("You Win!\n")

        elif (computer==0 and result==-1):
            print("You Lose!\n")

game()
game()
game()
game()
game()
