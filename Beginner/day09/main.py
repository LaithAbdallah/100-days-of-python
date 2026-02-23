import art

def get_winner(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    if highest_bid.is_integer():
        highest_bid = int(highest_bid)
    print(f"The winner is {winner} with a bid of ${highest_bid}")

def secret_auction(auction):
    while True:
        name = input("What is your name?: ")
        bid_amount = float(input("What is your bid?: $"))
        while bid_amount <= 0:
            bid_amount = float(input("Bid can't be lower than $1\n Please enter a valid amount: $"))
        auction[name] = bid_amount
        add_more = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        while add_more not in ["yes", "no"]:
            add_more = input("Please type either 'yes' or 'no'\n").lower()
        if add_more == "yes":
            print("\n" * 100)
        else:
            get_winner(auction)
            break

def main():
    print(art.logo)
    bids_dictionary = {}
    secret_auction(bids_dictionary)

if __name__ == "__main__":
    main()