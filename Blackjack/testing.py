from CardClass import Card
from PlayerClass  import Player
c1 = Card(1,1) #Ace
c2 = Card(13,1) #King

p1 = Player("test")
p1.hitHand(c1)
p1.hitHand(c2)

print(p1.hand)
print(str(p1.getHardScore())) #Blackjack!
print(str(p1.getSoftScore())) #Blackjack!

p1.clearHand()
print(p1.hand)

c1 = Card(1,1) #Ace
c2 = Card(4,1) #4
c3 = Card(6,3) #6

p1.hitHand(c1)
p1.hitHand(c2)
p1.hitHand(c3)
print(p1.hand)
print(str(p1.getHardScore())) #11
print(str(p1.getSoftScore())) #21

c4 = Card(5,4) #6
p1.hitHand(c4)
print(p1.hand)
print(str(p1.getHardScore())) #16
print(str(p1.getSoftScore())) #16

c5 = Card(8,4) #6
p1.hitHand(c5)
print(p1.hand)
print(str(p1.getHardScore())) #BUST
print(str(p1.getSoftScore())) #BUST

p1.clearHand()
print(p1.hand)
