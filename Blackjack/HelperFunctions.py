from PlayerClass import Player
from BlackjackHandClass import BlackjackHand
from CardClass import Card
import random
import math


'''
This doesn't really need to be seperated out, but might be useful when feeding
to the Nueral Net
'''
def printWinLoss():
    for i in range(tableCount-1):
        print(tableScores[i], "Player", i+1, ":", getSoftScore(table[i]))
        
'''Easier readability of the cardShoe'''
def printShoe():
    for card in cardShoe: print(card)

'''
generate 52 cards per deck in the game (normally 6-8 decks in a shoe)
randomly shuffle the cards and insert the cut card
When the cutCard is hit, it will be time to shuffle a new deck
'''
def loadShoe(number_of_decks, cardShoe):
    cutCard = Card(0,0)
    for deck in range(0,number_of_decks):
        for suit in range(1,4):
            for rank in range(1,14):
                cardShoe.append(Card(rank,suit))
    random.shuffle(cardShoe) #shuffle the cardShoe
    #index between 70-90% of the BACK of the deck to insert the cutCard
    minIndex = math.floor((52*number_of_decks)*.1)
    maxIndex = math.floor((52*number_of_decks)*.3)
    cardShoe.insert(random.randint(minIndex,maxIndex), cutCard)


'''
help with the instantiation of a new player and hand with nothing in it
'''
def instantiatePlayer(playerName):
    player = Player(playerName)
    hand = BlackjackHand()
    player.addHand(hand)
    return [player, hand]



'''
@param list object of all person's hands
@return void

Discard's all player's hands and the dealer's hand. If we hit the cutCard
then we also discard the rest of the shoe and generate a new shoe
'''
def clearTable(table):
    for hand in table:
        hand.clearHand()
    for i in range(numberOfPlayers):
         tableScores[i] = "Null"


        
