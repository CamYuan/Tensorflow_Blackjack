import pickle
import tensorflow as tf
import numpy as np
from Model_128_64_4 import *

train_data_file ="train_data.pickle"
train_labels_file = "train_labels.pickle"
test_data_file = "test_data.pickle"
test_labels_file = "test_labels.pickle"

print("Data is already normalized")

pickle_in = open(train_data_file, "rb")
train_data = pickle.load(pickle_in)
train_data = np.array(train_data)
pickle_in.close()

pickle_in = open(train_labels_file, "rb")
train_labels = pickle.load(pickle_in)
train_labels = np.array(train_labels)
pickle_in.close()

pickle_in = open(test_data_file, "rb")
test_data = pickle.load(pickle_in)
test_data = np.array(test_data)
pickle_in.close()

pickle_in = open(test_labels_file, "rb")
test_labels = pickle.load(pickle_in)
test_labels = np.array(test_labels)
pickle_in.close()

# for i in range(len(test_data)):
#     print(test_data[i], test_labels[i])

print("Building Model")
model = create_model()

model.fit(train_data, train_labels, epochs=10, batch_size=500)
# evaluation = model.evaluate(test_data, test_labels, batch_size=1)
# loss, acc = model.evaluate(test_data,  test_labels)
# print("loss", loss)
# print("Accuracy", acc)

# for i in range(20):
#     output = model.predict(np.expand_dims(test_data[i], axis=0))
#     print(test_data[i], np.argmax(output), test_labels[i])

model.save_weights('./checkpoints/TrainedModel')
