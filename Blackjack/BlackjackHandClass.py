

class BlackjackHand:

    def __init__(self):
        self.cards = []


    def __repr__(self):
        string = ""
        return string.join(str(self.cards))

    def __str__(self):
        string = ""
        return string.join(str(self.cards))
    
    '''
    @param card object to be added
    @return void
    '''
    def addCard(self, card):
        self.cards.append(card)

    '''
    Clear the player's hand to get ready for the next one
    '''
    def clearHand(self):
        self.cards.clear()

        
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
        if hardScore > 21: hardScore = "BUST"
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
        if softScore == "BUST": return softScore
        for card in self.cards:
            if card.rank == 1:
                if softScore > 11: return softScore
                else:
                    softScore += 10
                    if len(self.cards) == 2 and softScore == 21: softScore = "Blackjack!"
                    return softScore
        return softScore
