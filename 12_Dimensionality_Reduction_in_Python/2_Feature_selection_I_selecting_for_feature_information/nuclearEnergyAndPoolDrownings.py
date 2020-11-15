# Nuclear energy and pool drownings
# The dataset that has been pre-loaded for you as weird_df contains actual data provided by the US Centers for Disease Control & Prevention and Department of Energy.

# Let's see if we can find a pattern.

# Seaborn has been pre-loaded as sns and matplotlib.pyplot as plt.

# Instructions 1/4
# 0 XP
# Print the first five lines of weird_df.

# Instructions 2/4
# 35 XP
# Create a scatterplot with nuclear energy production on the x-axis and the number of pool drownings on the y-axis.

# Instructions 3/4
# 35 XP
# Print out the correlation matrix of weird_df.


# # Print the first five lines of weird_df
# print(weird_df.head())


# # Put nuclear energy production on the x-axis and the number of pool drownings on the y-axis
# sns.scatterplot(x='nuclear_energy', y='pool_drownings', data=weird_df)
# plt.show()


# Print out the correlation matrix of weird_df
print(weird_df.corr())
