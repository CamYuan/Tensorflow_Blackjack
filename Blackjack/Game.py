from Blackjack import *

'''
Clear out the rest of the shoe. Reset isShuffleTime to False. This can be
used for continuous gaming or set a game count.

Run the game. Put this in a for loop if you want to run the game
X times in a row
'''
def game(numSessions):
    for i in range(0, numSessions):
        cardShoe.clear()
        global isShuffleTime
        isShuffleTime = False
        loadShoe(num_decks, cardShoe)
        while not isShuffleTime:
            playRound(table, players)
        #print(isShuffleTime)


game(1)
print("Good Games!")
