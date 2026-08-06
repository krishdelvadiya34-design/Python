import random

def game():
    score=random.randint(1,100)
    print("Welcome to the game\n")

    with open("hiscore_game.txt") as f:
        hiscore=f.read()
        if (hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    print(f"Your score is =>{score}")

    if (score>hiscore):
        with open("hiscore_game.txt","w") as f:
            f.write(str(score))

    return score

game()