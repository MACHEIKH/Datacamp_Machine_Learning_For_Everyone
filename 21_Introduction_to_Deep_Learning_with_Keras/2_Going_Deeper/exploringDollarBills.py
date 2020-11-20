# Exploring dollar bills
# You will practice building classification models in Keras with the Banknote Authentication dataset.

# Your goal is to distinguish between real and fake dollar bills. In order to do this, the dataset comes with 4 features: variance,skewness,kurtosis and entropy. These features are calculated by applying mathematical operations over the dollar bill images. The labels are found in the dataframe's class column.


# A pandas DataFrame named banknotes is ready to use, let's do some data exploration!

# Instructions
# 100 XP
# Import seaborn as sns.
# Use seaborn's pairplot() on banknotes and set hue to be the name of the column containing the labels.
# Generate descriptive statistics for the banknotes authentication data.
# Count the number of observations per label with .value_counts().


# Import seaborn
import seaborn as sns

# Use pairplot and set the hue to be our class column
sns.pairplot(banknotes, hue='class') 

# Show the plot
plt.show()

# Describe the data
print('Dataset stats: \n', banknotes.describe())

# Count the number of observations per class
print('Observations per class: \n', banknotes['class'].value_counts())
