

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import hangman_words
end_of_game=False
chose_word= random.choice(hangman_words.word_list)
word_length=len(chose_word)

lives=6

from hangman_art import logo
print(logo)



# print(chose_word)

display=[]
# for letter in chose_word:

for _ in range(word_length):
    display+="_"
# print(display)



while end_of_game==False:
    guess=input("Guess a letter:").lower()

    if guess in display:
        print(f"You've already guessed {guess}")



    for position in range(word_length):
        letter=chose_word[position]
        # print(f"Current position:{position}\n Current letter: {letter}\n Guessed Letter:{guess}")
        if letter  == guess:
            display[position]=letter
    
    if guess not in chose_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -=1
        if lives == 0:
            end_of_game=True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("You win!")

from hangman_art import stages
print(stages[lives])