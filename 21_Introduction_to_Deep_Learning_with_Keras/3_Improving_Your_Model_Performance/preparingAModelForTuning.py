# Preparing a model for tuning
# Let's tune the hyperparameters of a binary classification model that does well classifying the breast cancer dataset.

# You've seen that the first step to turn a model into a sklearn estimator is to build a function that creates it. The definition of this function is important since hyperparameter tuning is carried out by varying the arguments your function receives.

# Build a simple create_model() function that receives both a learning rate and an activation function as arguments. The Adam optimizer has been imported as an object from keras.optimizers so that you can also change its learning rate parameter.

# Instructions
# 100 XP
# Set the learning rate of the Adam optimizer object to the one passed in the arguments.
# Set the hidden layers activations to the one passed in the arguments.
# Pass the optimizer and the binary cross-entropy loss to the .compile() method.


# Creates a model given an activation and learning rate
def create_model(learning_rate, activation):
  
  	# Create an Adam optimizer with the given learning rate
  	opt = Adam(lr = learning_rate)
  	
  	# Create your binary classification model  
  	model = Sequential()
  	model.add(Dense(128, input_shape = (30,), activation = activation))
  	model.add(Dense(256, activation = activation))
  	model.add(Dense(1, activation = 'sigmoid'))
  	
  	# Compile your model with your optimizer, loss, and metrics
  	model.compile(optimizer = opt, loss = 'binary_crossentropy', metrics = ['accuracy'])
  	return model
