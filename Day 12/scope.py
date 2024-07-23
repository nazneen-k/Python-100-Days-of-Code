enemies=1
def increase_enemies():
    enemies=2
    print(f"Enemies inside the function are {enemies}")

increase_enemies()
print(f"Enemies ouside the function are {enemies}")

# Local Scope ---> Within a function

# Global Scope ---> Can be used inside and outside 

def game():
    def drink_potion():
        position_strength=2
        print("inside function")
    drink_potion()

print("Outside function")
game()



# There is no Block Scope in python, i.e variables inside the if for block are still global variables

game_level=3
enemies=["Skeleton","Zoombie","Alien"]
if game_level<5:
    new_enemy=enemies[0]
print(new_enemy) #---> Doesnt throw any error 


# Modifying Global Scope
# We can even use global word and use it but its not preferred, you can use instead use Return

enemies=1

def increase_enemies():
    # enemies+=1   ---> This throws Error 
    print(f"Enemies inside function {enemies}")
    return enemies+1

increase_enemies()
print(f"Enemies outside function: {enemies}")


# Global Constants
PI= 3.14159
URL= "https://www.google.com"