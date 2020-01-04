import pickle
import tensorflow as tf
import numpy as np
from Model_128_64_4 import *

train_data_file ="train_data.pickle"
train_labels_file = "train_labels.pickle"
print("Data is already normalized")

pickle_in = open(train_data_file, "rb")
train_data = pickle.load(pickle_in)
train_data = np.array(train_data)
pickle_in.close()

pickle_in = open(train_labels_file, "rb")
train_labels = pickle.load(pickle_in)
train_labels = np.array(train_labels)
pickle_in.close()

print("Building Model")
model = create_model()

model.fit(train_data, train_labels, epochs=10, batch_size=500)

model.save_weights('./checkpoints/TrainedModel')
