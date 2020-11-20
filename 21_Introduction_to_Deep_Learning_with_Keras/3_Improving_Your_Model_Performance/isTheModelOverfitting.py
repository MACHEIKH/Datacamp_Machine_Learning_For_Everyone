# Is the model overfitting?
# Let's train the model you just built and plot its learning curve to check out if it's overfitting! You can make use of the loaded function plot_loss() to plot training loss against validation loss, you can get both from the history callback.

# If you want to inspect the plot_loss() function code, paste this in the console: show_code(plot_loss)

# Instructions 1/2
# 50 XP
# Train your model for 60 epochs, using X_test and y_test as validation data.
# Use plot_loss() passing loss and val_loss as extracted from the history attribute of the h_callback object.


# Train your model for 60 epochs, using X_test and y_test as validation data
h_callback = model.fit(X_train, y_train, epochs = 60, validation_data = (X_test, y_test), verbose=0)

# Extract from the h_callback object loss and val_loss to plot the learning curve
plot_loss(h_callback.history['loss'], h_callback.history['val_loss'])
