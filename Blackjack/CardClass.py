'''
"Value" is a customization for blackjack or other card games
'''

class Card:

    #static lists
    #cardSuits = ["None","Hearts","Diamonds","Clubs","Spades"]
    cardSuits = ["\u2612","\u2665","\u2666","\u2663","\u2660"]
    cardValues = ["\u2612","A","2","3","4","5","6","7","8","9","10","J","Q","K"]


    def __init__(self, rank, suit):
        self.validateInputs(rank, suit)
        self.stringRank = Card.cardValues[rank] #string
        self.rank = rank  #int 1-13
        self.suit = Card.cardSuits[suit] #string 

    def __repr__(self):
        return self.stringRank + self.suit

    def __str__(self):
        return self.stringRank + self.suit

    def validateInputs(self, rank, suit):
        error = False
        if rank > 13 or rank < 0:
            print("Error initilizing card. Invalid rank assignment: " + str(rank))
            print("Suit should be between 1-13 [Ace,Two,Three,Four,Five,Six,Seven,Eight,Nine,Ten,Jack,Queen,King]")
            error = True
        if suit > 4 or suit < 0:
            print("Error initilizing card. Invalid suit assignment: " + str(suit))
            print("Suit should be between 1-4 [Hearts,Diamonds,Clubs,Spades]")
            error = True
        if error: exit()


#add card counting values from https://www.blackjackapprenticeship.com/card-counting-systems/
