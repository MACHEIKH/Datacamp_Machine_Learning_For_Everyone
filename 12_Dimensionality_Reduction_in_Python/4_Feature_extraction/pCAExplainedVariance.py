# PCA explained variance
# You'll be inspecting the variance explained by the different principal components of the pca instance you created in the previous exercise.

# Instructions 1/4
# 25 XP
# Print the explained variance ratio per principal component.

# Instructions 3/4
# 25 XP
# Calculate the cumulative sum of the explained variance ratio using a method of pca.explained_variance_ratio_.


# Inspect the explained variance ratio per component
print(pca.explained_variance_ratio_)


# Print the cumulative sum of the explained variance ratio
print(pca.explained_variance_ratio_.cumsum())
