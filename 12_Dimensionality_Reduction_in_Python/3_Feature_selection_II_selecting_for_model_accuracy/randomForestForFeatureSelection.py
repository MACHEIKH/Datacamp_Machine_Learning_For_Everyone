# Random forest for feature selection
# Now lets use the fitted random model to select the most important features from our input dataset X.

# The trained model from the previous exercise has been pre-loaded for you as rf.

# Instructions 1/2
# 50 XP
# Create a mask for features with an importance higher than 0.15.

# Instructions 2/2
# 50 XP
# Sub-select the most important features by applying the mask to X.


# # Create a mask for features importances above the threshold (Instruction 1)
# mask = rf.feature_importances_ > 0.15

# # Prints out the mask
# print(mask)


# Create a mask for features importances above the threshold (Instruction 2)
mask = rf.feature_importances_ > 0.15

# Apply the mask to the feature dataset X
reduced_X = X.loc[:, mask]

# prints out the selected column names
print(reduced_X.columns)
