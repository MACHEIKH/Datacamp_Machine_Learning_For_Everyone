# A binary classification model
# Now that you know what the Banknote Authentication dataset looks like, we'll build a simple model to distinguish between real and fake bills.

# You will perform binary classification by using a single neuron as an output. The input layer will have 4 neurons since we have 4 features in our dataset. The model's output will be a value constrained between 0 and 1.

# We will interpret this output number as the probability of our input variables coming from a fake dollar bill, with 1 meaning we are certain it's a fake bill.


# Instructions
# 100 XP
# Import the Sequential model and Dense layer from Keras.
# Create a sequential model.
# Add a 4 neuron input layer with the input_shape parameter and a 1 neuron output layer with sigmoid activation.
# Compile your model using sgd as an optimizer.


# Import the sequential model and dense layer
from keras.models import Sequential
from keras.layers import Dense

# Create a sequential model
model = Sequential()

# Add a dense layer 
model.add(Dense(1, input_shape=(4,), activation='sigmoid'))

# Compile your model
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Display a summary of your model
model.summary()
