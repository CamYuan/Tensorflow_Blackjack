from BlackjackHandClass import BlackjackHand

class Player:
    ''' Initialize a player with a name, and an inital empty hand'''
    def __init__(self, name, bank=0):
        self.name = name  #1-13
        self.hands = []
        self.addHand(BlackjackHand())
        self.bank = bank
        self.sideBetBottomThree = 0 #side bets tied to the player?
        self.sideBetTopThree = 0

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def printHands(self):
        string = ""
        for i in range(len(self.hands)):
            string += "Hand " + str(i) + " : " + str(self.hands[i]) + "\n"
        #return string
        print(string)

    '''
    Players should only be making a bet on the initial hand.
    Splitting or doubling down will match the bet already placed.
    This implementation does not allow 'Up-to-current-bet'
    '''
    def bet(self, amount):
        if self.bank >= amount:
            self.hands[0].addBet(amount)
            self.bank -= amount
        else:
            print("not enough bank roll")

    def addHand(self, hand):
        self.hands.append(hand)


    def splitHand(self, hand):
        extraHand = BlackjackHand()
        card = hand.splitHand()
        extraHand.addCard(card)
        extraHand.addBet(hand.getBet())
        player.addHand(extraHand)

    def getAllScores(self):
        handScores = []
        for i in range(len(self.hands)):
            #implement return value?
            print("Hand " + str(i) + " : " + str(hands[i].getSoftScore))
            handScores.append(hands[i].getSoftScore)
        return handScores

    '''clear all hands and reinitialize with 1 empty hand'''
    def clearHands(self):
        self.hands.clear()
        hand = BlackjackHand()
        self.addHand(hand)

    def recievePayout(self, hand, multiplier):
        self.bank += hand.getBet() #Give the player the initial bet back first
        self.bank += hand.getBet()*multiplier
