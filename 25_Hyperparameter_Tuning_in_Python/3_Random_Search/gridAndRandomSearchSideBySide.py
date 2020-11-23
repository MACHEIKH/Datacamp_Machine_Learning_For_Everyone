# Grid and Random Search Side by Side
# Visualizing the search space of random and grid search together allows you to easily see the coverage that each technique has and therefore brings to life their specific advantages and disadvantages.

# In this exercise, you will sample hyperparameter combinations in a grid search way as well as a random search way, then plot these to see the difference.

# You will have available:

# combinations_list which is a list of combinations of learn_rate and min_samples_leaf for this algorithm
# The function visualize_search() which will make your hyperparameter combinations into X and Y coordinates and plot both grid and random search combinations on the same graph. It takes as input two lists of hyperparameter combinations.
# Instructions 1/4
# 35 XP
# Sample (by slicing) 300 hyperparameter combinations for a grid search from combinations_list into two lists and print the result.

# Instructions 2/4
# 35 XP
# Let's randomly sample too. Create a list of every index in combinations_list to sample from using range()
# Use np.random.choice() to sample 300 combinations. The first two arguments are a list to sample from and the number of samples.

# Instructions 3/4
# 0 XP
# Now use the list of random indexes to index into combinations_list using a list comprehension.

# Instructions 4/4
# 30 XP
# Use the provided visualize_search() function to visualize the two sampling methodologies. The first argument is your grid combinations, the second argument is the random combinations you created.


# Sample grid coordinates (Instruction 1)
grid_combinations_chosen = combinations_list[0:300]

# Create a list of sample indexes (Instruction 2)
sample_indexes = list(range(0,len(combinations_list)))

# Randomly sample 300 indexes
random_indexes = np.random.choice(sample_indexes, 300, replace=False)

# Use indexes to create random sample (Instruction 3)
random_combinations_chosen = [combinations_list[index] for index in random_indexes]

# Call the function to produce the visualization (Instruction 4)
visualize_search(grid_combinations_chosen, random_combinations_chosen)
