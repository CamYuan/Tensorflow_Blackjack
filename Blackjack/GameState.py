from PlayerClass import Player
from BlackjackHandClass import BlackjackHand
from HelperFunctions import *


'''
Player Objects. This table can hold a max of 5 players.
'''
[player1, hand1] = instantiatePlayer("p1")
[player2, hand2] = instantiatePlayer("p2")
[player3, hand3] = instantiatePlayer("p3")
[player4, hand4] = instantiatePlayer("p4")
[player5, hand5] = instantiatePlayer("p5")
[dealer, dhand] = instantiatePlayer("dealer")

#Global objects
'''
table list and players list are sort of duplicates because it makes looping a
bit easier, but I should consider consolidating...

Generating tableScores list based on the number of players
'''
players = [player1]
table = [hand1, dhand]
numberOfHands = len(table) #should be added to if hands are split
dealerIndex = numberOfHands - 1 #convenience
cardShoe = []
isShuffleTime = False
num_decks = 1 #cardShoes generally have between 6-8 decks

#Card Counting
RunningCount = 0
SuitCounts = [0,0,0,0]

'''
I do a pretty bad job of handling the scope of some of these objects...
Some I pass in as args, others I just reference as globals...
I need to clean this up
'''
