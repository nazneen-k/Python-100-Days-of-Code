from art import logo
from data import data
import random

# Display Art 
print(logo)


def format_data(account):
    """Format the account data into printable format"""
    account_name = accou["name"]
    account_desc = accou["description"]
    account_country = accou["country"]

    print(f"{account_name}, a {account_desc} from {account_country}")

# Generate a random acccount from the game data
account_a= random.choice(data)
account_b= random.choice(data)
if account_a ==  account_b:
    account_b=random.choice(data)

print(f"Compare A : {format_data(account_a)}")
print(f"Companre B : {format_data(account_b)}")







