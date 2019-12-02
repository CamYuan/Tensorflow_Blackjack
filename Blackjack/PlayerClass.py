'''
"Value" is a customization for blackjack or other card games
'''

class Player:    
    def __init__(self, name):
        self.name = name  #1-13
        self.hand = []

        
    def __repr__(self):
        return str(self.getHardScore())

    def __str__(self):
        return self.getHardScore()
    
    '''
    @param card object to be added
    @return void
    '''
    def hitHand(self, card):
        self.hand.append(card)

    '''
    @return int score of player's hard hand value

    Also could be considered lowest possible hand
    i.e.: hand(A,5,A) has a "hard value" of 7
    '''
    def getHardScore(self):
        hardScore = 0
        for card in self.hand:
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
        for card in self.hand:
            if card.rank == 1:
                if softScore > 11: return softScore
                else:
                    softScore += 10
                    if len(self.hand) == 2 and softScore == 21: softScore = "Blackjack!"
                    return softScore
        return softScore

    '''
    Clear the player's hand to get ready for the next one
    '''
    def clearHand(self):
        self.hand.clear()
