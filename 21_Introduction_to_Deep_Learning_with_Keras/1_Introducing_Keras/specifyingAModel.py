# Specifying a model
# You will build a simple regression model to predict the orbit of the meteor!

# Your training data consist of measurements taken at time steps from -10 minutes before the impact region to +10 minutes after. Each time step can be viewed as an X coordinate in our graph, which has an associated position Y for the meteor orbit at that time step.

# Note that you can view this problem as approximating a quadratic function via the use of neural networks.


# This data is stored in two numpy arrays: one called time_steps , what we call features, and another called y_positions, with the labels. Go on and build your model! It should be able to predict the y positions for the meteor orbit at future time steps.

# Keras Sequential model and Dense layers are available for you to use.

# Instructions
# 100 XP
# Instantiate a Sequential model.
# Add a Dense layer of 50 neurons with an input shape of 1 neuron.
# Add two Dense layers of 50 neurons each and 'relu' activation.
# End your model with a Dense layer with a single neuron and no activation.


# Instantiate a Sequential model
model = Sequential()

# Add a Dense layer with 50 neurons and an input of 1 neuron
model.add(Dense(50, input_shape=(1,), activation='relu'))

# Add two Dense layers with 50 neurons and relu activation
model.add(Dense(50, activation='relu'))
model.add(Dense(50, activation='relu'))

# End your model with a Dense layer and no activation
model.add(Dense(1))
