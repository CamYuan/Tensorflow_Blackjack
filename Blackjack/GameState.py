from PlayerClass import Player
from BlackjackHandClass import BlackjackHand
from HelperFunctions import *


'''
Player Objects. This table can hold a max of 5 players.
'''
player1 = Player("p1")
player2 = Player("p2")
player3 = Player("p3")
player4 = Player("p4")
player5 = Player("p5")
dealer = Player("dealer")


#Global objects
'''
table list and players list are sort of duplicates because it makes looping a
bit easier, but I should consider consolidating...

Generating tableScores list based on the number of players
'''
players = [player1]
table = [player1, dealer]
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
