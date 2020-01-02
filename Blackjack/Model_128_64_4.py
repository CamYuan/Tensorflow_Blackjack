import tensorflow as tf
from tensorflow.keras import layers

def create_model():
  model = tf.keras.Sequential()
  model.add(layers.Dense(128, activation='relu')) # Adds a densely-connected layer with 128 units to the model:
  model.add(layers.Dense(64, activation='relu'))
  model.add(layers.Dense(4, activation='softmax'))# Add a softmax layer with 4 output units:

  model.compile(optimizer="adam",
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  return model
