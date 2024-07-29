from art import logo, vs
from data import data
import random

# Display Art 
print(logo)


def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]

    return (f"{account_name}, a {account_desc} from {account_country}")

def check_answer(guess, a_followers,b_followers):
    """Take the user guess and  follower counts and returns if they got it right"""

# Generate a random acccount from the game data
account_a= random.choice(data)
account_b= random.choice(data)
if account_a ==  account_b:
    account_b=random.choice(data)

print(f"Compare A : {format_data(account_a)}")
print(vs)
print(f"Companre B : {format_data(account_b)}")

guess=input("Who has more followers? Type  'A' or 'B': ").lower()

a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]







