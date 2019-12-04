from BlackjackHandClass import BlackjackHand

class Player:
    ''' Initialize a player with a name, and an inital empty hand'''
    def __init__(self, name, bank=0):
        self.name = name  #1-13
        self.hands = []
        hand = BlackjackHand()
        self.addHand(hand)
        self.bank = bank


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

    def addHand(self, hand):
        self.hands.append(hand)

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
