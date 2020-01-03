from BlackjackHandClass import BlackjackHand
'''
{
    name: string,
    hands: list,
    bankroll: int,
    sideBetBottomThree: int,
    sideBetTopThree: int
}
'''
class Player:
    ''' Initialize a player with a name, and an inital empty hand'''
    def __init__(self, name, bankroll=0):
        self.name = name  #1-13
        self.hands = []
        self.addHand(BlackjackHand())
        self.bankroll = bankroll
        self.sideBetBottomThree = 0 #side bets tied to the player?
        self.sideBetTopThree = 0
        self.wins = 0
        self.losses = 0
        self.pushes = 0

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
    def bet(self, amount, hand):
        if self.bankroll >= amount:
            hand.addBet(amount)
            self.bankroll -= amount
            return True
        else:
            print("not enough bankroll roll")
            return False

    def addHand(self, hand):
        self.hands.append(hand)

    def hasEnoughFunds(self):
        if self.hands[0].getBet() <= self.bankroll:
            return True
        else:
            return False

    def doubleDown(self, hand):
        self.bet(hand.getBet(), hand)


    def splitHand(self, hand):
        extraHand = BlackjackHand()
        extraHand.alreadySplit = True
        card = hand.splitHand()
        if card.rank == 1:
            extraHand.splitAces = True
        extraHand.addCard(card)
        self.bet(hand.getBet(), extraHand)
        self.addHand(extraHand)

    '''clear all hands and reinitialize with 1 empty hand'''
    def clearHands(self):
        self.hands.clear()
        hand = BlackjackHand()
        self.addHand(hand)

    def recievePayout(self, hand, multiplier):
        self.bankroll += hand.getBet() #Give the player the initial bet back first
        self.bankroll += hand.getBet()*multiplier
