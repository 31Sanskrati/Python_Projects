import random

def play():
    player = input("Choose 'r' for Rock, 'p' for Paper and 's' for seciorrs\n")
    computer = random.choice(['r','p','s'])

    if player==computer:
        print("\nMatch Draw")

    elif (player=='r'):
        if computer=='p':
            print("\nComputer WINS")
        else:
            print("\nPlayer WINS")

    elif player=='p':
        if computer=='r':
            print("\nPlayer WINS")
        else:
            print("\nComputer WINS")

    elif player=='s':
        if computer=='r':
            print("\nComputer WINS")
        else:
            print("\nPlayer WINS")
    print(f"You have choosen {player} and the computer has choosen {computer} ")

play()

