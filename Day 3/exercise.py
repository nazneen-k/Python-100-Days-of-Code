person1=input("Enter Person Name")
person2=input("Enter Person Name")

combinedNames=person1+person2
loweredCombinedNames=combinedNames.lower()

t=loweredCombinedNames.count('t')
r=loweredCombinedNames.count('r')
u=loweredCombinedNames.count('u')
e=loweredCombinedNames.count('e')

firstDigit=t+r+u+e

l=loweredCombinedNames.count('l')
o=loweredCombinedNames.count('o')
v=loweredCombinedNames.count('v')
e=loweredCombinedNames.count('e')

secondDigit=l+o+v+e

score=int(str(firstDigit)+str(secondDigit))
if(score<10) or (score>90):
    print(f'Your score is {score}, you go together like coke and mentos')
elif (score>=40) and (score<=50):
    print(f'Your score is {score}, you are alright together')
else:
    print("The Score is:",score)