
from Model_128_64_4 import *
import pickle
import numpy as np

test_data_file = "test_data.pickle"
test_labels_file = "test_labels.pickle"

print("Data is already normalized")

pickle_in = open(test_data_file, "rb")
test_data = pickle.load(pickle_in)
test_data = np.array(test_data)
pickle_in.close()

pickle_in = open(test_labels_file, "rb")
test_labels = pickle.load(pickle_in)
test_labels = np.array(test_labels)
pickle_in.close()

# Create a new model instance
model = create_model()

# Restore the weights
model.load_weights('./checkpoints/TrainedModel')

# for i in range(20):
#     output = model.predict(np.expand_dims(test_data[i], axis=0))
#     print(test_data[i], np.argmax(output), test_labels[i])

loss, acc = model.evaluate(test_data,  test_labels, verbose=0)
print("loss", loss)
print("Accuracy", acc)
