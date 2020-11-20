# Build your LSTM model
# You've already prepared your sequences of text. It's time to build your LSTM model!

# Remember your sequences had 4 words each, your model will be trained on the first three words of each sequence, predicting the 4th one. You are going to use an Embedding layer that will essentially learn to turn words into vectors. These vectors will then be passed to a simple LSTM layer. Our output is a Dense layer with as many neurons as words in the vocabulary and softmax activation. This is because we want to obtain the highest probable next word out of all possible words.

# The size of the vocabulary of words (the unique number of words) is stored in vocab_size.

# Instructions
# 100 XP
# Import the Embedding, LSTM and Dense layer from Keras layers.
# Add an Embedding() layer of the vocabulary size, that will turn words into 8 number vectors and receive sequences of length 3.
# Add a 32 neuron LSTM() layer.
# Add a hidden Dense() layer of 32 neurons and an output layer of vocab_size neurons with softmax.


# Import the Embedding, LSTM and Dense layer
from keras.layers import Embedding, LSTM, Dense

model = Sequential()

# Add an Embedding layer with the right parameters
model.add(Embedding(input_dim = vocab_size, input_length = 3, output_dim = 8 ))

# Add a 32 unit LSTM layer
model.add(LSTM(32))

# Add a hidden Dense layer of 32 units and an output layer of vocab_size with softmax
model.add(Dense(32, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
model.summary()
