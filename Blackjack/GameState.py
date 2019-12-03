from PlayerClass import Player
from BlackjackHandClass import BlackjackHand
from HelperFunctions import instantiatePlayer


'''
Player Objects. This table can hold a max of 5 players.
'''
[player1, hand1] = instantiatePlayer("p1")
[player2, hand2] = instantiatePlayer("p2")
[player3, hand3] = instantiatePlayer("p3")
[player4, hand4] = instantiatePlayer("p4")
[player5, hand5] = instantiatePlayer("p5")
[dealer, hand6] = instantiatePlayer("dealer")

#Global objects
'''
table list and players list are sort of duplicates because it makes looping a
bit easier, but I should consider consolidating...

Generating tableScores list based on the number of players
'''
players = [player1]
table = [hand1, dhand]
tableScores = [] #Should be the same length as the number of hands at the table
tableCount = len(tableScores)
dealerIndex = tableCount - 1
cardShoe = []
isShuffleTime = False
num_decks = 1 #cardShoes generally have between 6-8 decks


for each in range(len(table)):
    tableScores.append("Null")
