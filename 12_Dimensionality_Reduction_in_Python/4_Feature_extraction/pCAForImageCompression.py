# PCA for image compression
# You'll reduce the size of 16 images with hand written digits (MNIST dataset) using PCA.

# The samples are 28 by 28 pixel gray scale images that have been flattened to arrays with 784 elements each (28 x 28 = 784) and added to the 2D numpy array X_test. Each of the 784 pixels has a value between 0 and 255 and can be regarded as a feature.

# A pipeline with a scaler and PCA model to select 78 components has been pre-loaded for you as pipe. This pipeline has already been fitted to the entire MNIST dataset except for the 16 samples in X_test.

# Finally, a function plot_digits has been created for you that will plot 16 images in a grid.

# Instructions 1/4
# 25 XP
# Plot the MNIST sample data.

# Instructions 2/4
# 25 XP
# Transform the input data to principal components using the pipeline.

# Instructions 3/4
# 25 XP
# Inverse transform the components back to the original feature space.

# Instructions 4/4
# 25 XP
# Plot the reconstructed data.


# Plot the MNIST sample data (Instruction 1)
plot_digits(X_test)


# Transform the input data to principal components (Instruction 2)
pc = pipe.transform(X_test)

# Prints the number of features per dataset
print("X_test has {} features".format(X_test.shape[1]))
print("pc has {} features".format(pc.shape[1]))


# Transform the input data to principal components (Instruction 3)
pc = pipe.transform(X_test)

# Inverse transform the components to original feature space
X_rebuilt = pipe.inverse_transform(pc)

# Prints the number of features
print("X_rebuilt has {} features".format(X_rebuilt.shape[1]))


# Transform the input data to principal components (Instruction 4)
pc = pipe.transform(X_test)

# Inverse transform the components to original feature space
X_rebuilt = pipe.inverse_transform(pc)

# Plot the reconstructed data
plot_digits(X_rebuilt)
