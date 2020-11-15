# Visually detecting redundant features
# Data visualization is a crucial step in any data exploration. Let's use Seaborn to explore some samples of the US Army ANSUR body measurement dataset.

# Two data samples have been pre-loaded as ansur_df_1 and ansur_df_2.

# Seaborn has been imported as sns.

# Instructions 1/4
# 25 XP
# Create a pairplot of the ansur_df_1 data sample and color the points using the 'Gender' feature.

# Instructions 2/4
# 25 XP
# Two features are basically duplicates, remove one of them from the dataset.

# Instructions 3/4
# 25 XP
# Now create a pairplot of the ansur_df_2 data sample and color the points using the 'Gender' feature.

# Instructions 4/4
# 25 XP
# One feature has no variance, remove it from the dataset.


# # Create a pairplot and color the points using the 'Gender' feature (Intruction 1)
# sns.pairplot(ansur_df_1, hue='Gender', diag_kind='hist')

# # Show the plot
# plt.show()


# # Remove one of the redundant features (Intruction 2)
# reduced_df = ansur_df_1.drop('body_height', axis=1)

# # Create a pairplot and color the points using the 'Gender' feature
# sns.pairplot(reduced_df, hue='Gender')

# # Show the plot
# plt.show()


# # Create a pairplot and color the points using the 'Gender' feature (Intruction 3)
# sns.pairplot(ansur_df_2, hue='Gender', diag_kind='hist')

# # Show the plot
# plt.show()


# Remove the redundant feature (Intruction 4)
reduced_df = ansur_df_2.drop('n_legs', axis=1)

# Create a pairplot and color the points using the 'Gender' feature
sns.pairplot(reduced_df, hue='Gender', diag_kind='hist')

# Show the plot
plt.show()
