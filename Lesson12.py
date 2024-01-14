from art import logo

import os

print(logo)

def find_highest_score(players_info):
    max=0
    winner_name=""
    for name in players_info:
        if players_info[name]> max:
            max=players_info[name]
            winner_name = name
    print(f"The winner is {winner_name} with bidding of ${max}")

bidding_finished= False

players_info={}

while not bidding_finished:
    name=input("Bidder's name:")
    bid_price=int(input("How much would you like to bid?"))
    more_bidders=input("Are there any more bidders? Yes or No?")
    players_info[name]=bid_price
    if more_bidders== "No":
        bidding_finished= True
        find_highest_score(players_info)
    elif more_bidders== "Yes":
        os.system('cls')
