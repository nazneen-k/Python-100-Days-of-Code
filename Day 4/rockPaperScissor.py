import random


userChoice=int(input("What do you choose? Type 0 for Rock, 1  for Paper or 2 for Scissors"))

computerChoice=random.randint(0,2)
print(f'Computer chose {computerChoice}')

if userChoice >=3 or userChoice <0:
    print("You typed an invalid number.")

elif userChoice==0 and computerChoice==2:
    print("You win!!")
elif computerChoice ==0 and userChoice ==2:
    print("You lose!!")
elif computerChoice> userChoice:
    print("You lose")
elif userChoice > computerChoice:
    print("You win")
elif computerChoice == userChoice:
    print("Its a draw!!")


