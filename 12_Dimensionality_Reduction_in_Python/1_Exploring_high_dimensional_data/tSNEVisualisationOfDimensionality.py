# t-SNE visualisation of dimensionality
# Time to look at the results of your hard work. In this exercise, you will visualize the output of t-SNE dimensionality reduction on the combined male and female Ansur dataset. You'll create 3 scatterplots of the 2 t-SNE features ('x' and 'y') which were added to the dataset df. In each scatterplot you'll color the points according to a different categorical variable.

# seaborn has already been imported as sns and matplotlib.pyplot as plt.

# Instructions 1/3
# 35 XP
# Use seaborn's sns.scatterplot to create the plot.
# Color the points by 'Component'.

# Instructions 2/3
# Color the points of the scatterplot by 'Branch'.

# Instructions 3/3
# Color the points of the scatterplot by 'Gender'.


# Color the points according to Army Component (Instruction 1)
sns.scatterplot(x="x", y="y", hue='Component', data=df)

# Show the plot
plt.show()


# Color the points by Army Branch (Instruction 2)
sns.scatterplot(x="x", y="y", hue='Branch', data=df)

# Show the plot
plt.show()


# Color the points by Gender (Instruction 3)
sns.scatterplot(x="x", y="y", hue='Gender', data=df)

# Show the plot
plt.show()
