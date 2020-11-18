# Performance on data subsets
# In professional basketball, there are two conferences, the East and the West. Coaches and fans often only care about how teams in their own conference will do this year.

# You have been working on an NBA prediction model and would like to determine if the predictions were better for the East or West conference. You added a third array to your data called labels, which contains an "E" for the East teams, and a "W" for the West. y_test and predictions have again been loaded for your use.

# Instructions 1/4
# 25 XP
# Create an array east_teams that can be used to filter labels to East conference teams.

# Instructions 2/4
# 25 XP
# Create the arrays true_east and preds_east by filtering the arrays y_test and predictions.

# Instructions 3/4
# 25 XP
# Use the print statements to print the MAE (using scikit-learn) for the East conference. The mean_absolute_error function has been loaded as mae.

# Instructions 4/4
# 25 XP
# The variable west_error contains the MAE for the West teams. Use the print statement to print out the Western conference MAE.


# Find the East conference teams (Instruction 1)
east_teams = labels == "E"

# Create arrays for the true and predicted values (Instruction 2)
true_east = y_test[east_teams]
preds_east = predictions[east_teams]

# Print the accuracy metrics (Instruction 3)
print('The MAE for East teams is {}'.format(
    mae(true_east, preds_east)))

# Print the West accuracy (Instruction 4)
print('The MAE for West conference is {}'.format(west_error))
