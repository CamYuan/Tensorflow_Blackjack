'''
"Value" is a customization for blackjack or other card games
'''

class Card:    
    def __init__(self, rank, stringRank, suit):
        self.rank = rank  
        self.stringRank = stringRank
        self.suit = suit
        
    def __repr__(self):
        return self.stringRank + "_of_"+self.suit

    def __str__(self):
        return self.stringRank + "_of_"+self.suit
    



