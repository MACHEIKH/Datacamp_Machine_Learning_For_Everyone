# One-Hot encoding
# The problem with label encoding is that it implicitly assumes that there is a ranking dependency between the categories. So, let's change the encoding method for the features "RoofStyle" and "CentralAir" to one-hot encoding. Again, the train and test DataFrames from House Prices Kaggle competition are already available in your workspace.

# Recall that if you're dealing with binary features (categorical features with only two categories) it is suggested to apply label encoder only.

# Your goal is to determine which of the mentioned features is not binary, and to apply one-hot encoding only to this one.

# Instructions 1/4
# 35 XP
# Determine the distribution of "RoofStyle" and "CentralAir" features using pandas' value_counts() method.

# Instructions 3/4
# 35 XP
# As long as "CentralAir" is a binary feature, encode it with a label encoder (0 - for one class and 1 - for another class).

# Instructions 4/4
# 30 XP
# For the categorical feature "RoofStyle" let's use the one-hot encoder. Firstly, create one-hot encoded features using the get_dummies() method. Then they are concatenated to the initial houses DataFrame.


# # Concatenate train and test together (Instruction 1)
# houses = pd.concat([train, test])

# # Look at feature distributions
# print(houses['RoofStyle'].value_counts(), '\n')
# print(houses['CentralAir'].value_counts())


# # Concatenate train and test together (Instruction 3)
# houses = pd.concat([train, test])

# # Label encode binary 'CentralAir' feature
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# houses['CentralAir_enc'] = le.fit_transform(houses['CentralAir'])


# Concatenate train and test together (Instruction 4)
houses = pd.concat([train, test])

# Label encode binary 'CentralAir' feature
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
houses['CentralAir_enc'] = le.fit_transform(houses['CentralAir'])

# Create One-Hot encoded features
ohe = pd.get_dummies(houses['RoofStyle'], prefix='RoofStyle')

# Concatenate OHE features to houses
houses = pd.concat([houses, ohe], axis=1)

# Look at OHE features
print(houses[[col for col in houses.columns if 'RoofStyle' in col]].head(3))
