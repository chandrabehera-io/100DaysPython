#

print("Welcome to the blind auction program!")

bid = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? "))
    bid[name] = price
    yesorno = input("Are there any other bidders? (y/n) ")
    if yesorno == "n":
        bidding_finished = True
        break

# function to find highest bidder


def find_highest_bidder(bid):
    highest_bidder = ""
    highest_bid = 0
    for name, price in bid.items():
        if price > highest_bid:
            highest_bidder = name
            highest_bid = price
    return highest_bidder


print("The highest bidder is", find_highest_bidder(bid))
