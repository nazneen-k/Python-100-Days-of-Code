import os
from turtle import clear

from art import logo
print(logo)

bids={} #Empty Dictionary
bidding_finishes=False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner = bidder
        print(f"The winner is {winner} with a bid of ₹{highest_bid}")
        

while not bidding_finishes:
    name=input("What is your Name? ")
    price= int(input("What is your bid? ₹"))
    bids[name]=price
    should_contiue=input("Are there any other bidders? Type 'yes' or 'no' ") 
    if should_contiue == "no":
        bidding_finishes=True
        find_highest_bidder(bids)
    elif should_contiue=="yes":
        clear()