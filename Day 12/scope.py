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