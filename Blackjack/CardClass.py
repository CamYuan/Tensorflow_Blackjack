'''
"Value" is a customization for blackjack or other card games
'''

class Card:    
    def __init__(self, rank, stringRank, suit):
        self.rank = rank  #1-13
        self.stringRank = stringRank
        self.suit = suit #Spade,Diamond,Heart,Club
        
    def __repr__(self):
        return self.stringRank + "_of_"+self.suit

    def __str__(self):
        return self.stringRank + "_of_"+self.suit
    



