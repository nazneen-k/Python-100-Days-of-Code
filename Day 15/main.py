MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit=0
resources = {
    "water": 300,
    
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry!! There is not enough {item}.")
            return False 
        return True
    
def process_coins():
    """"Returns the total calculated from coins inserted"""
    print("Please insert coins")
    total=int(input("How many quarters?: ")) *0.25
    total+=int(input("How many dimes?: ")) *0.1
    total+=int(input("How many nickles?: ")) *0.05
    total+=int(input("How many pennies?: ")) *0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    """Return True when the Payment is accepted, or False if the money is insufficient"""


is_on= True
while is_on:
    choice = input("What would you like>? (espresso/latte/cuppuccino)")
    if choice=="off":
        is_on = False
        
    elif choice =="report":
        
        print(f"Water: {resources['water']}") 
        print(f"Milk: {resources['milk']} ")        
        print(f"Coffee: {resources['coffee']} ")
        print(f"Money: ${profit} ")
    else:
        drink = MENU[choice]
        # print(drink)
        
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()




