from turtle import clear


print("Welcome to Blind Bidding Program ")

blind_bid = {}
bidding_finnish = False

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finnish:
    name = input("What is your name?: ")
    bid = int(input("Enter your bid amount: $"))

    blind_bid[name] = bid
    yes_no = input("Are there any other bidders? type 'yes' or 'no'.\n" )

    if yes_no == "no":
        bidding_finnish = True
        find_highest_bid(blind_bid)
    elif yes_no == "yes":
        clear()


