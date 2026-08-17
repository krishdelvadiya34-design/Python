from random import randint

n=randint(1,1000)
num=0
guesses=0

while (n!=num):
    num=int(input("Guess a number =>"))
    guesses+=1

    if (num>n):
        print("Lower number please!")
    else:
        print("Higher number please!")

print(f"You guess the right number {n} in {guesses} attempt")