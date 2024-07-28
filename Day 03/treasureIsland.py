print("Welcome to Tresure Island")
print("Your mission is to find the tressure")
choice1=input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1=='left':
        choice2=input('You\'ve come to a lake. This is an islan in the middle of the lake. Type "wait" to wait for the boat. Type "swim" to swim across.').lower()
        if choice2=='wait':
               choice3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
               if choice3=='red':
                      print("Its a room full of fire. Game Over")
               elif choice3=='yellow':
                      print("Your found the treasure! You Win!")
               elif choice3=='blue':
                      print("You enter a room of beasts. Game Over")
               else:
                      print("You chose a door that doesnt exist. Game Over!")

        else:
            print("You got attacked by an angry trout. Game Over")
else:
        print("You fell into a hole. Game Over")