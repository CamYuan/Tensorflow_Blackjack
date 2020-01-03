import pickle
import random
from CardClass import Card
from BlackjackHandClass import BlackjackHand
import numpy as np
from Labeler import *


'''
Datapoints needed
{
    SoftScore:
    HardScore:
    dealerUpCard.rank:
    Card1.rank: This should only be relevant for splitting
    canSplit:
    canDoubleDown:
    numberOfCards: Probably don't need this if we know canSplit and canDoubleDown, but we will include it anyway
}
TODO: In the future it would be good if we can just pass the card (52 card deck) so we can also detect suits

'''
TwoCardDatapoints = 50000
ThreeCardDatapoints = 50000
AceThreshhold = 5000 #make sure there are plenty of Ace cases for soft score valuing
# Stand, Hit, DoubleDown, Split
choices = ["S", "H", "D", "T"] #choices 0-3
train_data = []
train_labels = []
counter = 0
while(counter < ThreeCardDatapoints):
    counter += 1
    dealerCard = Card(random.randint(1,13),random.randint(1,4))#randomly select a value from 0-12
    if(counter < AceThreshhold):
        card1 = Card(1,random.randint(1,4)) #Ace
    else:
        card1 = Card(random.randint(1,13),random.randint(1,4))#randomly select a value from 0-12
    card2 = Card(random.randint(1,13),random.randint(1,4))#randomly select a value from 0-12
    hand = BlackjackHand()
    hand.addCard(card1)
    hand.addCard(card2)
    numberOfCards = len(hand.cards)
    canSplit = hand.canSplit
    canDoubleDown = hand.canDoubleDown
    softScore = hand.getSoftScore()
    hardScore = hand.getHardScore()
    datapoint = [softScore/21, hardScore/21, dealerCard.rank/13, card1.rank/13, int(hand.canSplit)/1.0, int(hand.canDoubleDown)/1.0, numberOfCards/14]
    # print(datapoint)
    train_data.append(datapoint) #normalize the data as we store it
    # Set the training label... https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
    choice = labeler(dealerCard, softScore, hardScore, card1, canSplit, canDoubleDown)
    # print(softScore, hardScore, dealerCard,"|", card1, card2, canSplit, canDoubleDown, numberOfCards, choice)
    if(choice == -1):
        print("No Label applied")
        print(dealerCard.rank, softScore, hardScore, card1.rank, card2.rank)
        exit()
    train_labels.append(choice)

counter = 0
while(counter < ThreeCardDatapoints):
    dealerCard = Card(random.randint(1,13),random.randint(1,4))#randomly select a value from 0-12
    if(counter < AceThreshhold):
        card1 = Card(1,random.randint(1,4)) #Ace
    else:
        card1 = Card(random.randint(1,13),random.randint(1,4))#randomly select a value from 0-12
    card2 = Card(random.randint(1,13),random.randint(1,4))#randomly select a value from 0-12
    card3 = Card(random.randint(1,13),random.randint(1,4))#randomly select a value from 0-12
    hand = BlackjackHand()
    hand.addCard(card1)
    hand.addCard(card2)
    hand.addCard(card3)
    softScore = hand.getSoftScore()
    hardScore = hand.getHardScore()
    if(not hand.bust): #creating 3 card hands can result in lots of busts
        counter += 1
        numberOfCards = len(hand.cards)
        canSplit = hand.canSplit
        canDoubleDown = hand.canDoubleDown
        datapoint = [softScore/21, hardScore/21, dealerCard.rank/13, card1.rank/13, int(hand.canSplit)/1.0, int(hand.canDoubleDown)/1.0, numberOfCards/14]
        # print(datapoint)
        train_data.append(datapoint) #normalize the data as we store it
        # Set the training label... https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
        choice = labeler(dealerCard, softScore, hardScore, card1, canSplit, canDoubleDown)
        # print(softScore, hardScore, dealerCard,"|", card1, card2, card3, canSplit, canDoubleDown, numberOfCards, choice)
        if(choice == -1):
            print("No Label applied")
            print(dealerCard.rank, softScore, hardScore, card1.rank, card2.rank)
            exit()
        train_labels.append(choice)



#print the dataset and labels
# for i in range(len(train_data)):
#     print(train_data[i], train_labels[i])


data = []
test_data = []
test_labels = []
testCount = 0

# random.shuffle(data)
# for datapoint in data:
#     test_data.append(datapoint[:-1])
#     test_labels.append(datapoint[-1])

# for i in range(len(test_data)):
#     print(test_data[i], test_labels[i])



pickle_out = open("train_data.pickle", "wb")
pickle.dump(train_data, pickle_out)
pickle_out.close()

pickle_out = open("train_labels.pickle", "wb")
pickle.dump(train_labels, pickle_out)
pickle_out.close()

pickle_out = open("test_data.pickle", "wb")
pickle.dump(test_data, pickle_out)
pickle_out.close()

pickle_out = open("test_labels.pickle", "wb")
pickle.dump(test_labels, pickle_out)
pickle_out.close()

print("Finished!")
print("TwoCardDatapoints:", TwoCardDatapoints)
print("ThreeCardDatapoints:", ThreeCardDatapoints)
print("Minimum Ace cases: ",AceThreshhold*2)
