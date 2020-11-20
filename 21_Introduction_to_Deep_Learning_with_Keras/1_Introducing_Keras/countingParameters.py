# Counting parameters
# You've just created a neural network. But you're going to create a new one now, taking some time to think about the weights of each layer. The Keras Dense layer and the Sequential model are already loaded for you to use.

# This is the network you will be creating:


# Instructions 1/2
# 50 XP
# Instantiate a new Sequential() model.
# Add a Dense() layer with five neurons and three neurons as input.
# Add a final dense layer with one neuron and no activation.

# Instantiate a new Sequential model
model = Sequential()

# Add a Dense layer with five neurons and three inputs
model.add(Dense(5, input_shape=(3,), activation="relu"))

# Add a final Dense layer with one neuron and no activation
model.add(Dense(1))

# Summarize your model
model.summary()
