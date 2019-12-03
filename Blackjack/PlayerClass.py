'''
"Value" is a customization for blackjack or other card games
'''

class Player:
    def __init__(self, name):
        self.name = name  #1-13
        self.hands = []


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


    def clearHands(self):
        self.hands.clear()
