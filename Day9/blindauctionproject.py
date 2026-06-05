# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from time import time

import art
print(art.logo)

should_continue = True


def find_highest_bidder(dictionary):
    winner = ""
    highest_bid = 0
    for bid in dictionary:
        if dictionary[bid] > highest_bid:
            highest_bid = dictionary[bid]
            winner = bid
    print(f"{winner} has the highest bid $ {highest_bid} and therefore is the Winner!")


bids = {}


while should_continue:
    name = input("Please enter your name: \n")
    price = float(input("Please enter your price: \n $ "))
    bids[name] = price
    more_bids_required = input("Are there more bidders? (y/n) \n").lower()
    if more_bids_required == "n":
        should_continue = False
        find_highest_bidder(bids)
    elif more_bids_required == "y":
        print("\n" * 20)









