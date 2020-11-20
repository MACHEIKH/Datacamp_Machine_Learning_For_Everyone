# Predicting the orbit!
# You've already trained a model that approximates the orbit of the meteor approaching Earth and it's loaded for you to use.

# Since you trained your model for values between -10 and 10 minutes, your model hasn't yet seen any other values for different time steps. You will now visualize how your model behaves on unseen data.

# If you want to check the source code of plot_orbit, paste show_code(plot_orbit) into the console.

# Hurry up, the Earth is running out of time!

# Remember np.arange(x,y) produces a range of values from x to y-1. That is the [x, y) interval.

# Instructions 1/2
# 50 XP
# Use the model's .predict() method to predict from -10 to 10 minutes.

# Instructions 2/2
# Use the model's .predict() method to predict from -40 to 40 minutes.


# # Predict the twenty minutes orbit (Instruction 1)
# twenty_min_orbit = model.predict(np.arange(-10, 11))

# # Plot the twenty minute orbit 
# plot_orbit(twenty_min_orbit)


# Predict the eighty minute orbit (Instruction 2)
eighty_min_orbit = model.predict(np.arange(-40, 41))

# Plot the eighty minute orbit 
plot_orbit(eighty_min_orbit)
