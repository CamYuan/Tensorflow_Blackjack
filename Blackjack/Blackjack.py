from CardClass import Card
import random
import math

#static lists
cardSuits = ["Hearts","Diamonds","Clubs","Spades"]
cardValues = ["Ace","Two","Three","Four","Five","Six",
              "Seven","Eight","Nine","Ten","Jack","Queen","King"]

#Global objects
cardShoe = []
isShuffleTime = False
num_decks = 1 #cardShoes generally have between 6-8 decks

'''
generate 52 cards per deck in the game (normally 6-8 decks in a shoe)
randomly shuffle the cards and insert the cut card
When the cutCard is hit, it will be time to shuffle a new deck
'''
def loadShoe():
    cutCard = Card(0,"cutCard","None")
    for deck in range(0,num_decks):
        for suit in cardSuits:
            for rank in range(1,14):
                cardShoe.append(Card(rank, cardValues[rank-1], suit))
    random.shuffle(cardShoe) #shuffle the cardShoe
    #index between 70-90% of the BACK of the deck to insert the cutCard
    minIndex = math.floor((52*num_decks)*.1)
    maxIndex = math.floor((52*num_decks)*.3)
    cardShoe.insert(random.randint(minIndex,maxIndex), cutCard)

'''Easier readability of the cardShoe'''
def printShoe():
    for card in cardShoe: print(card)

'''
@param list object of a single player's hand
@return void

Pops 1 card off the cardShoe and adds it to the player's hand
If the cutCard is dealt, this will be the last hand. Set isShuffleTime to true
'''
def hit(hand):
    card = cardShoe.pop()
    if(card.rank == "cutCard"):
        isShuffleTime = True
        card = cardShoe.pop()
        print("----CUT CARD---")
    hand.append(card)

'''
@param list object of a all person's hands 
@return void

Gives 2 cards to all players.
Dealer should be the last index of the players
'''
def deal(table):
    for i in range(0,2):
        for player in table:
            hit(player)
    

'''
@param list object of a single player's hand
@return int score of player's hard hand value

Also could be considered lowest possible hand
i.e.: hand(A,5,A) has a "hard value" of 7
'''
def getHardScore(playerHand):
    hardScore = 0
    for card in playerHand:
        if card.rank > 10: hardScore += 10
        else: hardScore += card.rank
    return hardScore
        
'''
@param list object of a single player's hand
@return int score of player's soft hand value

Also could be considered highest possible hand
Soft value will return the hard value if over 10
Soft hands should always contain an Ace
i.e.: hand(A,5,A) has a "soft value" of 17
'''
def getSoftScore(playerHand):
    softScore = getHardScore(playerHand)
    for card in playerHand:
        if card.rank == 1:
            if softScore > 10: return softScore
            else: return softScore + 10
    return softScore

'''
@param list object of all person's hands
@return void

Discard's all player's hands and the dealer's hand. If we hit the cutCard
then we also discard the rest of the shoe and generate a new shoe
'''
def clearTable(table):
    for hand in table:
        hand.clear()
    for i in range(len(tableScores)):
         tableScores[i] = "Null"

def newDeck():
    cardShoe.clear()
    isShuffleTime = False
    printShoe() #for Debugging. Remove if working correctly
    loadShoe()

def scoreTable(players, dealer):
    dealerHand = getSoftScore(dealer)
    print("Dealerscore: ", dealerHand)
    playerIndex = 0
    for player in players:
        playerScore = getSoftScore(player)
        print("PlayerScore: ", playerScore)
        if tableScores[playerIndex] != "BUST":
            if  tableScores[len(tableScores)-1] == "BUST":
                tableScores[playerIndex] = "playerWin"
            elif playerScore > dealerHand:
                tableScores[playerIndex] = "playerWin"
            elif playerScore == dealerHand:
                tableScores[playerIndex] = "PUSH"
            else:
                tableScores[playerIndex] = 'Dealer Wins'
                
            




''''''
def playHand():
    deal(table)
    print("Dealer's up Card: " , dealer[0])
    playerIndex = 0
    for player in players:
        print(getSoftScore(player), getHardScore(player), player)
        choice = ''
        while choice != 's':
            choice = input("[H]it, [S]tand, or [M]yHand: ").lower()
            if choice == 'h':
                hit(player)
                print(getSoftScore(player), getHardScore(player), player)
                if getHardScore(player) > 21:
                    tableScores[playerIndex] = "BUST"
                    choice = 's'
            print(player)
        playerIndex += 1

        #TODO: Check BUST Logic. 
            
    while getSoftScore(dealer) < 17: #dealer stays on soft 17
        hit(dealer)
        print("DealerHand", dealer)
        if getHardScore(dealer) > 21:
            tableScores[len(tableScores)-1] = "BUST"
            
    scoreTable(players, dealer)
    clearTable(table)
    print("--------------------------------")
    
            

###########################
player1 = []
player2 = []
player3 = []
player4 = []
player5 = []
dealer = []
###########################

table = [player1, dealer]
players = [player1]

tableScores = []
for each in range(len(table)):
    tableScores.append("Null")

loadShoe()

while isShuffleTime == False:
    playHand()
newDeck()
print("Good Games!")



