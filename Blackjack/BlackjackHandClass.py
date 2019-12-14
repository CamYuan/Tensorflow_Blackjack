'''
{
    bet: int,
    cards: list,
    bust: boolean,
    blackjack: boolean,
    canSplit: boolean,
    alreadySplit: boolean
}
'''
class BlackjackHand:

    def __init__(self):
        self.bet = 0
        self.cards = []
        self.bust = False
        self.hasBlackjack = False
        self.canDoubleDown = False
        self.canSplit = False
        self.alreadySplit = False
        self.splitAces = False


    def __repr__(self):
        string = ""
        return string.join(str(self.cards))

    def __str__(self):
        string = ""
        return string.join(str(self.cards))

    '''
    @param card object to be added
    @return void
    Players must have enough money to add their initial bet again
    If this is the first two cards of the hand and they are the same
    AND you did not previously split to get this hand, set canSplit to true
    If there are more than 2 cards in the hand already
    AND you did not split Aces, set canDoubleDown to True
    '''
    def addCard(self, card):
        self.cards.append(card)
        if len(self.cards) == 2 and self.cards[0].rank == self.cards[1].rank and self.alreadySplit == False:
            self.canSplit = True
        else:
            self.canSplit = False
        if len(self.cards) == 2 and not self.splitAces:
            self.canDoubleDown = True
        else:
            self.canDoubleDown = False

    '''
    @param card object to be added
    @return void
    '''
    def addBet(self, bet):
        self.bet += bet

    def getBet(self):
        return self.bet

    '''
    double the bet. We should get just one card
    '''
    def doubleDown(self):
        self.bet += self.bet

    def splitHand(self):
        self.canSplit = False
        self.alreadySplit = True
        if self.cards[0].rank == 1:
            self.splitAces = True
        return self.cards.pop()

    '''
    Clear the player's hand to get ready for the next one
    '''
    def clearHand(self):
        self.cards.clear()
        self.bet = 0
        self.bust = False
        self.hasBlackjack = False

    def checkBlackjack(self):
        if len(self.cards) == 2 and self.getSoftScore == 21 and self.alreadySplit == False:
            self.hasBlackjack = True

    '''
    @return int score of player's hard hand value
    Also could be considered lowest possible hand
    i.e.: hand(A,5,A) has a "hard value" of 7
    '''
    def getHardScore(self):
        hardScore = 0
        for card in self.cards:
            if card.rank > 10: hardScore += 10
            else: hardScore += card.rank
        if hardScore > 21: self.bust = True
        return hardScore

    '''
    @return int score of player's soft hand value
    Also could be considered highest possible hand
    Soft value will return the hard value if over 10
    Soft hands should always contain an Ace
    i.e.: hand(A,5,A) has a "soft value" of 17
    '''
    def getSoftScore(self):
        softScore = self.getHardScore()
        if self.bust: return softScore
        for card in self.cards:
            if card.rank == 1:
                if softScore > 11: return softScore
                else:
                    softScore += 10
                    return softScore
        return softScore
