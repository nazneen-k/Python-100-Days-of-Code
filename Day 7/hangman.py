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

guess=input("Guess a letter:").lower()

for position in range(word_length):
    letter=chose_word[position]
    if letter  == guess:
        display[position]=letter

print(display)