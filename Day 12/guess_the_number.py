from art import logo
print(logo)

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
from random import randint

turns=0
# Function to check user's guess against actual answer
'''checks answer against guess. Returns the number of turns remaining'''
def check_answer(guess,answer,turns):
    if guess> answer:
        print("Too High")
        return turns -1
    elif guess < answer:
        print("Too low.")  
        return turns -1  
    else:
        (f"You got it! The answer was {answer} ")

# Make function to set difficulty
def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



#  Choosing a random Number between 1 to 100
def game():
  print("Welcome to  the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  answer=randint(1,100)
  print(f"the answer is {answer}")
  turns=set_difficulty()
  

  # Repeat the guessing functionality if they get it wrong
  guess=0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    # Let the user guess a number
    guess =int(input("Make a Guess: "))
    turns= check_answer(guess,answer,turns)
    if turns == 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        return
    elif guess !=answer:
        print("Guess Again")


# Track the number of turns and reduce by 1 if they get it wrong

game()