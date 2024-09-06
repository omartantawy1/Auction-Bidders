
from art import logo
print(logo)

bidding_finished=False
bids={}

while not bidding_finished:
    name=input("what's your name ? : ")
    price=int(input("what's your bid ? : ")) 
    check=input('do u have any other bidder yes or no ?')
    bids[name]=price 
    if check == 'no':
        bidding_finished=True
        
def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=''
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f'the winner is {winner} with the highest bid of {highest_bid}')  
    
find_highest_bidder(bids)    
      