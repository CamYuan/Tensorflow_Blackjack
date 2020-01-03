from CardClass import Card
from HelperFunctions import *
from GameState import *
import numpy as np

def betBeforeHand(players):
    for player in players:
        validBet = False
        while(not validBet):
            try:
                betAmount = 5
                # betAmount = int(input("How much do you want to bet? "))
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

'''
@param list object of a single player
@return void

Pops 1 card off the cardShoe and adds it to a hand
If the cutCard is dealt, this will be the last hand. Set isShuffleTime to true
'''
def hit(hand):
    card = cardShoe.pop()
    if(card.rank == 0):
        print("----------------------CUT CARD----------------------")
        global isShuffleTime
        isShuffleTime = True
        card = cardShoe.pop()
    #card count here I think
    hand.addCard(card)

'''
@param list of all players
@return void

Gives 2 cards to all players.
Dealer should be the last index of the players
'''
def deal(table):
    for i in range(0,2):
        for player in table:
            for hand in player.hands:
                hit(hand)

def playHand(player):
    global dealer
    for hand in player.hands:
        if len(hand.cards) < 2:
            print()
            hit(hand)
        hand.checkBlackjack()
        print(player, hand.getSoftScore(), hand.getHardScore(), hand)
        choice = ''
        while choice != 's' and hand.getSoftScore() != 21:
            print()
            options = "[H]it or [S]tand"
            doubleDownEnabled = False
            splitEnabled = False
            if hand.canSplit and player.hasEnoughFunds():
                options +=  " or Spli[T]"
                splitEnabled = True
            if hand.canDoubleDown and player.hasEnoughFunds():
                options +=  " or [D]oubledown"
                doubleDownEnabled = True
            options += ": "
            # choice = input(options).lower()
            choice = getModelPrediction(dealerUpCard(dealer).rank, hand.getSoftScore(), hand.getHardScore(), hand.cards[0].rank, hand.cards[1].rank)
            print(dealerUpCard(dealer).rank, hand.getSoftScore(), hand.getHardScore(), hand.cards[0].rank, hand.cards[1].rank, choice)
            if(choice == 'd' and doubleDownEnabled == False): #correct decisions that are not game legal
                choice = 'h'
                print("switching to hit")
            if(choice == 't' and hand.canSplit == False): #correct decisions that are not game legal
                choice = 'h'
                print("switching to hit")
            if choice == 's':
                pass
            elif choice == 'h':
                hit(hand)
                print(player, hand.getSoftScore(), hand.getHardScore(), hand)
                if hand.getHardScore() >= 21:
                    choice = 's'
            elif choice == 'd' and doubleDownEnabled:
                player.doubleDown(hand)
                hit(hand)
                print(player, hand.getSoftScore(), hand.getHardScore(), hand)
                choice = 's'
            elif choice == 't' and splitEnabled:
                player.splitHand(hand)
                hit(hand)
                print(player, hand.getSoftScore(), hand.getHardScore(), hand)
            else:
                print("Invalid Input")
'''
If all players have busted or have blackjack, the hand is over.
Don't deal any cards for the dealer
'''
def deadHand(players):
    deadHand = True #allBustOrBlackjack
    for player in players:
        for hand in player.hands:
            if hand.hasBlackjack or not hand.bust:
                deadHand = False
    return deadHand

'''
@param list object of players
@param dealer hand
@return void

First confirm the dealer's score and whether or not they busted.
If the player busted first, they lose.
If the dealer busted, all remaining players should win
If the players hand is higher than the dealers, they should win
If the players hand is the same as the dealers, they PUSH
If the players hand is less than the dealers, they lose

Players' hands and dealer's should not be higher than 21
as it should have been caught by BUST logic

Also give an easier readout for the print object



'''
def scoreTable(players, dealer):
    dealerScore = dealer.hands[0].getSoftScore()
    print()
    print("DEALER : ", dealerScore, dealer.hands[0])
    '''
    Check if the dealer has blackjack. If true, all players lose immediately
    UNLESS a player also has blackjack, then they PUSH.
    '''
    if dealer.hands[0].hasBlackjack:
        for player in players:
            for hand in player.hands:
                if hand.hasBlackjack:
                    currHand = "PUSH"
                    player.pushes += 1
                else:
                    currHand = "LOSS"
                    player.losses += 1
                print(player, currHand, hand)
                payout(player, hand, currHand)
    else:
        for player in players:
            for hand in player.hands:
                handScore = hand.getSoftScore()
                if not hand.bust:
                    if hand.hasBlackjack:
                        currHand = "BLACKJACK"#implement 1.5x
                        player.wins += 1
                    elif dealer.hands[0].bust:
                        currHand = "WIN"
                        player.wins += 1
                    elif handScore > dealerScore:
                        currHand = "WIN"
                        player.wins += 1
                    elif handScore == dealerScore:
                        currHand = "PUSH"
                        player.pushes += 1
                    else:
                        currHand = "LOSS"
                        player.losses += 1
                else:
                    currHand = "BUST"
                    player.losses += 1
                print(player, currHand, handScore, hand)
                payout(player, hand, currHand)


'''
Runs through the hand:
1) TODO: Bet
2) Deal the hand
3) Check for blackjacks -> Not offering insurance
4) Let each player make hit/stand/split/doubledown decisions
5) Play out the dealer hand
6) Calculate scores
7) TODO: Payout
8) Clear the hands/table

If the dealer gets a blackjack, the whole table loses automatically UNLESS
the player also has blackjack, then they PUSH
If a player has blackjack, they win immediately 1.5x the amount they bet

Each player makes a series of decisions. For now it is only [Hit] and [S]tand
Hitting gives the player a new card and they can then make the same decision
When they choose to stand, they will not get any more cards
If they BUST, they lose immediately
After the players make their choices, the dealer then hits based on
predetermined rules. In this case, they will stay on a Soft 17 or higher

After the dealer makes all their choices, score the table to determine winners
Discard all the cards and get ready for the next hand

'''
totalHands = 0
def playRound(table, players):
    global totalHands
    betBeforeHand(players) #1
    totalHands += 1
    deal(table) #2
    '''if the dealer has blackjack, the hand is over. No insurance (currently?)
    Move to scoring/payout
    '''
    if not dealer.hands[0].checkBlackjack(): #3
        print("Dealer's up Card: " , dealerUpCard(dealer))
        for player in players: #4
            playHand(player)

        if not deadHand(players):
            while dealer.hands[0].getSoftScore() < 17: #5 #dealer stays on soft 17
                hit(dealer.hands[0])
                print("DealerHand", dealer.hands[0])
    scoreTable(players, dealer) #6 #7
    resetTable(table) #8
    print("--------------------------------")

alldecisions = []
def getModelPrediction(dealerCard, softScore, hardScore, card1, card2):
    output = model.predict(np.expand_dims([(dealerCard-1)/13, softScore/21, hardScore/21, (card1-1)/13, (card2-1)/13], axis=0))
    choice = choices[np.argmax(output)].lower()
    alldecisions.append([dealerCard, softScore, hardScore, card1, card2, choice])
    return choice
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


game(100)

print(player1.wins, "-", player1.losses, "-", player1.pushes, "/", totalHands )
print("{:.3%}".format(player1.wins/totalHands), "-", "{:.3%}".format(player1.losses/totalHands), "-", "{:.3%}".format(player1.pushes/totalHands) )
print("Good Games!")
