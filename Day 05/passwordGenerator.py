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

# Easy Level
password=""

for char in range(1,nrLetters+1):
    randomChar=random.choice(letters)
    password+=randomChar
    print(password)

for char in range(1,nrSymbols+1):
    password+=random.choice(symbols)

for char in range(1,nrNumbers):
    password+=random.choice(numbers)

print("Your Password is:",password)


# Hard Level

passwordList=[]

for char in range(1,nrLetters+1):
    randomChar=random.choice(letters)
    passwordList+=randomChar
    

for char in range(1,nrSymbols+1):
    passwordList+=random.choice(symbols)

for char in range(1,nrNumbers+1):
    passwordList+=random.choice(numbers)

print("Your Password is:",passwordList)

random.shuffle(passwordList)
print(passwordList)

finalPassword=''
for char in passwordList:
    finalPassword+=char
print("Your Password Generated is:",finalPassword)
