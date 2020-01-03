from Labeler import *
from Model_128_64_4 import *
import pickle
import numpy as np
from CardClass import Card

choices = ["S", "H", "D", "T"] #choices 0-3
data_file = "alldecisions.pickle"

pickle_in = open(data_file, "rb")
data_input = pickle.load(pickle_in)
pickle_in.close()

# data = []
# labels = []
# for datapoint in data_input:
#     data.append(datapoint[:-1])
#     labels.append(datapoint[-1])

for dealerCard, softScore, hardScore, card1, card2, label in data_input:
    dealerCard = Card(dealerCard,1)#randomly select a value from 0-12
    card1 = Card(card1,1)#randomly select a value from 0-12
    card2 = Card(card2,1) #randomly select a value from 0-12
    if( choices[labeler(dealerCard, softScore, hardScore, card1, card2)].lower() != label ):
        print(dealerCard, softScore, hardScore, card1, card2, choices[labeler(dealerCard, softScore, hardScore, card1, card2)].lower(), label )


# # Create a new model instance
# model = create_model()
#
# # Restore the weights
# model.load_weights('./checkpoints/TrainedModel')
#
# loss, acc = model.evaluate(test_data,  test_labels, verbose=0)
# print("loss", loss)
# print("Accuracy", acc)
