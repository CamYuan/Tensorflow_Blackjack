import pickle
import random
from CardClass import Card
from BlackjackHandClass import BlackjackHand
import numpy as np
from Labeler import *


'''
Datapoints needed
{
    dealerUpCard.rank:
    SoftScore:
    HardScore:
    Card1.rank:
    Card2.rank:
}
TODO: In the future it would be good if we can just pass the card (52 card deck) so we can also detect suits

'''
numTrainingDataPoints = 1000000
# Stand, Hit, DoubleDown, Split
choices = ["S", "H", "D", "T"] #choices 0-3
train_data = []
train_labels = []
for i in range(0, numTrainingDataPoints):
    dealerCard = Card(random.randint(1,13),random.randint(1,4))#randomly select a value from 0-12
    card1 = Card(random.randint(1,13),random.randint(1,4))#randomly select a value from 0-12
    card2 = Card(random.randint(1,13),random.randint(1,4))#randomly select a value from 0-12
    hand = BlackjackHand()
    hand.addCard(card1)
    hand.addCard(card2)
    softScore = hand.getSoftScore()
    hardScore = hand.getHardScore()
    datapoint = [dealerCard.rank/13, softScore/21, hardScore/21, card1.rank/13, card2.rank/13]
    # print(dealerCard.rank, softScore, hardScore, card1.rank, card2.rank)
    train_data.append(datapoint) #normalize the data as we store it

    # Set the training label... https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
    # Split > SoftScore > HardScore
    choice = labeler(dealerCard, softScore, hardScore, card1, card2)

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
for upcard in range(1,14):
    for value in range(1,14):
        for value2 in range(value,14):
            testCount+=1
            dealerCard = Card(upcard,random.randint(1,4))#randomly select a value from 0-12
            card1 = Card(value,random.randint(1,4))#randomly select a value from 0-12
            card2 = Card(value2,random.randint(1,4))#randomly select a value from 0-12
            hand = BlackjackHand()
            hand.addCard(card1)
            hand.addCard(card2)
            softScore = hand.getSoftScore()
            hardScore = hand.getHardScore()
            datapoint = [dealerCard.rank/13, softScore/21, hardScore/21, card1.rank/13, card2.rank/13]
            # print("[", dealerCard.rank, softScore, hardScore, card1.rank, card2.rank, "]", sep = ' ')

            # Set the training label... https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
            # Split > SoftScore > HardScore
            choice = labeler(dealerCard, softScore, hardScore, card1, card2)
            if(choice == -1):
                print("No Label applied")
                print(dealerCard.rank, softScore, hardScore, card1.rank, card2.rank)
                exit()
            datapoint.append(choice)
            # print("[", dealerCard.rank, softScore, hardScore, card1.rank, card2.rank, "]", choices[choice])
            data.append(datapoint) #normalize the data as we store it

# random.shuffle(data)
for datapoint in data:
    test_data.append(datapoint[:-1])
    test_labels.append(datapoint[-1])

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

print("Finished creating", numTrainingDataPoints, "training datapoints and ", testCount, " test datapoints.")
