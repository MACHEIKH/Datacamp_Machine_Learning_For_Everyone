# Softmax predictions
# Your recently trained model is loaded for you. This model is generalizing well!, that's why you got a high accuracy on the test set.

# Since you used the softmax activation function, for every input of 2 coordinates provided to your model there's an output vector of 4 numbers. Each of these numbers encodes the probability of a given dart being thrown by one of the 4 possible competitors.

# When computing accuracy with the model's .evaluate() method, your model takes the class with the highest probability as the prediction. np.argmax() can help you do this since it returns the index with the highest value in an array.

# Use the collection of test throws stored in coords_small_test and np.argmax()to check this out!

# Instructions 1/2
# 50 XP
# Predict with your model on coords_small_test.
# Print the model predictions.

# Instructions 2/2
# 50 XP
# Use np.argmax()to extract the index of the highest probable competitor from each pred vector in preds.


# Predict on coords_small_test (Instruction 1)
preds = model.predict(coords_small_test)

# Print preds vs true values
print("{:45} | {}".format('Raw Model Predictions','True labels'))
for i,pred in enumerate(preds):
  print("{} | {}".format(pred,competitors_small_test[i]))

# Extract the position of highest probability from each pred vector (Instruction 2)
preds_chosen = [np.argmax(pred) for pred in preds]

# Print preds vs true values
print("{:10} | {}".format('Rounded Model Predictions','True labels'))
for i,pred in enumerate(preds_chosen):
  print("{:25} | {}".format(pred,competitors_small_test[i]))
