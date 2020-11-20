# Comparing activation functions
# Comparing activation functions involves a bit of coding, but nothing you can't do!

# You will try out different activation functions on the multi-label model you built for your farm irrigation machine in chapter 2. The function get_model('relu') returns a copy of this model and applies the 'relu' activation function to its hidden layer.

# You will loop through several activation functions, generate a new model for each and train it. By storing the history callback in a dictionary you will be able to visualize which activation function performed best in the next exercise!

# X_train, y_train, X_test, y_test are ready for you to use when training your models.

# Instructions
# 100 XP
# Fill up the activation functions array with relu,leaky_relu, sigmoid, and tanh.
# Get a new model for each iteration with get_model() passing the current activation function as a parameter.
# Fit your model providing the train and validation_data, use 20 epochs and set verbose to 0.


# Activation functions to try
activations = ['relu', 'leaky_relu', 'sigmoid', 'tanh']

# Loop over the activation functions
activation_results = {}

for act in activations:
  # Get a new model with the current activation
  model = get_model(act)
  # Fit the model and store the history results
  h_callback = model.fit(X_train, y_train, epochs=20, verbose=0, validation_data=(X_test, y_test))
  activation_results[act] = h_callback
