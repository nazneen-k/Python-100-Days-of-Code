word_list=["ardvark","baboon","camel"]

import random
chose_word= random.choice(word_list)

# print(chose_word)

display=[]
# for letter in chose_word:
word_length=len(chose_word)
for _ in range(word_length):
    display+="_"
print(display)


end_of_game=False
while end_of_game==False:
    guess=input("Guess a letter:").lower()

    for position in range(word_length):
        letter=chose_word[position]
        # print(f"Current position:{position}\n Current letter: {letter}\n Guessed Letter:{guess}")
        if letter  == guess:
            display[position]=letter

    print(display)

    if "_" not in display:
        end_of_game=True
        print("End of Game")