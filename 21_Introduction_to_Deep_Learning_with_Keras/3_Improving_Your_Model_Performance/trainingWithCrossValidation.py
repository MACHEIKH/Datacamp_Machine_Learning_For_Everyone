# Training with cross-validation
# Time to train your model with the best parameters found: 0.001 for the learning rate, 50 epochs, a 128 batch_size and relu activations.

# The create_model() function from the previous exercise is ready for you to use. X and y are loaded as features and labels.

# Use the best values found for your model when creating your KerasClassifier object so that they are used when performing cross_validation.

# End this chapter by training an awesome tuned model on the breast cancer dataset!

# Instructions
# 100 XP
# Import KerasClassifier from keras scikit_learn wrappers.
# Create a KerasClassifier object providing the best parameters found.
# Pass your model, features and labels to cross_val_score to perform cross-validation with 3 folds.


# Import KerasClassifier from keras wrappers
from keras.wrappers.scikit_learn import KerasClassifier

# Create a KerasClassifier
model = KerasClassifier(build_fn = create_model(learning_rate = 0.001, activation = 'relu'), epochs = 50, 
             batch_size = 128, verbose = 0)

# Calculate the accuracy score for each fold
kfolds = cross_val_score(model, X, y, cv = 3)

# Print the mean accuracy
print('The mean accuracy was:', kfolds.mean())

# Print the accuracy standard deviation
print('With a standard deviation of:', kfolds.std())
