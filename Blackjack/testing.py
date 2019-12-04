from CardClass import Card
from PlayerClass  import Player
from BlackjackHandClass import BlackjackHand
c1 = Card(1,1) #Ace
c2 = Card(13,1) #King

p1 = Player("test")
h1 = BlackjackHand()
p1.addHand(h1)
h1.addCard(c1)
h1.addCard(c2)

print("Hand 1: ")
print(h1.cards)
print("Hard: " + str(h1.getHardScore())) #11
print("Soft: " + str(h1.getSoftScore())) #Blackjack!

h2 = BlackjackHand()
c1 = Card(1,1) #Ace
c2 = Card(4,1) #4
c3 = Card(6,3) #6
h2.addCard(c1)
h2.addCard(c2)
h2.addCard(c3)
p1.addHand(h2)
print("Hand 2")
print(h2.cards)
print("Hard: " + str(h2.getHardScore())) #11
print("Soft: " + str(h2.getSoftScore())) #21

c4 = Card(5,4) #6
h2.addCard(c4)
print(h2.cards)
print("Hard: " + str(h2.getHardScore())) #16
print("Soft: " + str(h2.getSoftScore())) #16

c5 = Card(8,4) #6
h2.addCard(c5)
print(h2.cards)
print(str(h2.getHardScore())) #BUST
print(str(h2.getSoftScore())) #BUST

print("Player 1: ")
print(p1.hands)
p1.clearHands()
print(p1.hands)
