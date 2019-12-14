from PlayerClass import Player
from BlackjackHandClass import BlackjackHand
from CardClass import Card
import random
import math

'''Easier readability of the cardShoe'''
def printShoe():
    for card in cardShoe: print(card)

'''
generate 52 cards per deck in the game (normally 6-8 decks in a shoe)
randomly shuffle the cards and insert the cut card
When the cutCard is hit, it will be time to shuffle a new deck
'''
def loadShoe(numberOfDecks, cardShoe):
    cutCard = Card(0,0)
    for deck in range(0,numberOfDecks):
        for suit in range(1,4):
            for rank in range(1,14):
                cardShoe.append(Card(rank,suit))
    random.shuffle(cardShoe) #shuffle the cardShoe
    #index between 70-90% of the BACK of the deck to insert the cutCard
    minIndex = math.floor((52*numberOfDecks)*.1)
    maxIndex = math.floor((52*numberOfDecks)*.3)
    cardShoe.insert(random.randint(minIndex,maxIndex), cutCard)

'''
@param list object of all person's hands
@return void

Discard's all player's hands and the dealer's hand. If we hit the cutCard
then we also discard the rest of the shoe and generate a new shoe
'''
def resetTable(table):
    for player in table:
        player.clearHands()

#2nd card is the dealers up card
def dealerUpCard(dealer):
    return dealer.hands[0].cards[1]


def betBeforeHand(players):
    for player in players:
        validBet = False
        while(not validBet):
            try:
                betAmount = int(input("How much do you want to bet? "))
                print("Betting: " + str(betAmount))
                validBet = player.bet(betAmount, player.hands[0])
            except:
                print("Invalid Bet. Please enter a number")
                validBet = False

def payout(player, hand, position):
    print(player.bankroll)
    if position == 'WIN':
        player.recievePayout(hand, 1)
    elif position == 'PUSH':
        player.recievePayout(hand, 0)
    elif position == 'BLACKJACK':
        player.recievePayout(hand, 1.5)
    print(player.bankroll)
    #else we have lost. The bet was already removed from the our bankroll
