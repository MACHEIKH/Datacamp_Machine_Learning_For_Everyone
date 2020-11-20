# Neural separation
# Put on your gloves because you're going to perform brain surgery!

# Neurons learn by updating their weights to output values that help them better distinguish between the different output classes in your dataset. You will make use of the inp_to_out() function you just built to visualize the output of two neurons in the first layer of the Banknote Authentication model as it learns.

# The model you built in chapter 2 is ready for you to use, just like X_test and y_test. Paste show_code(plot) in the console if you want to check plot().

# You're performing heavy duty, once all is done, click through the graphs to watch the separation live!

# Instructions
# 100 XP
# Use the previously defined inp_to_out() function to get the outputs of the first layer when fed with X_test.
# Use the model.evaluate() method to obtain the validation accuracy for the test dataset at each epoch.


for i in range(0, 21):
  	# Train model for 1 epoch
    h = model.fit(X_train, y_train, batch_size = 16, epochs = 1, verbose = 0)
    if i%4==0: 
      # Get the output of the first layer
      layer_output = inp_to_out([X_test])[0]
      
      # Evaluate model accuracy for this epoch
      test_accuracy = model.evaluate(X_test, y_test)[1] 
      
      # Plot 1st vs 2nd neuron output
      plot()
