# Creating Hyperparameters
# For a school assignment, your professor has asked your class to create a random forest model to predict the average test score for the final exam.

# After developing an initial random forest model, you are unsatisfied with the overall accuracy. You realize that there are too many hyperparameters to choose from, and each one has a lot of possible values. You have decided to make a list of possible ranges for the hyperparameters you might use in your next model.

# Your professor has provided de-identified data for the last ten quizzes to act as the training data. There are 30 students in your class.

# Instructions 1/3
# 35 XP
# Print.get_params() in the console to review the possible parameters of the model that you can tune.

# Instructions 2/3
# 35 XP
# Create a maximum depth list, [4, 8, 12] and a minimum samples list [2, 5, 10] that specify possible values for each hyperparameter.

# Instructions 3/3
# 30 XP
# Create one final list to use for the maximum features.
# Use values 4 through the maximum number of features possible (10), by 2.


# Review the parameters of rfr (Instruction 1)
print(rfr.get_params())

# Maximum Depth (Instruction 2)
max_depth = [4, 8, 12]

# Minimum samples for a split
min_samples_split = [2, 5, 10]
 
# Max features (Instruction 3)
max_features = [4, 6, 8, 10]
