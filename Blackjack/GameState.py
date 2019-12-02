from Player import Player

'''
Player Objects. This table can hold a max of 5 players.
We could code this more dynamically, but it just seemed like overkill...
'''
player1 = []
player2 = []
player3 = []
player4 = []
player5 = []
dealer = Player("dealer")




#Global objects
'''
table list and players list are sort of duplicates because it makes looping a
bit easier, but I should consider consolidating...

Generating tableScores list based on the number of players
'''
table = [player1, dealer]
players = [player1]

tableScores = []
for each in range(len(table)):
    tableScores.append("Null")
    
tableCount = len(tableScores)
dealerIndex = tableCount - 1
cardShoe = []
isShuffleTime = False
num_decks = 1 #cardShoes generally have between 6-8 decks
