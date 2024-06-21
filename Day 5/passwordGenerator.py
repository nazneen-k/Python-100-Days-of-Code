import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=[
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', 
    "'", '"', '\\', '|', ',', '<', '.', '>', '/', '?', '`', '~'
]

print("Welcome to the Password Generator")
nrLetters=int(input("How many leters would you lime in your password?\n"))
nrSymbols=int(input("How many symbols wold you like \n"))
nrNumbers=int(input("How many numbers would you like?"))

