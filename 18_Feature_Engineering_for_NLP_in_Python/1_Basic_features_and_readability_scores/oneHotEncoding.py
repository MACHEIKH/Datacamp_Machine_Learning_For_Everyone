# One-hot encoding
# In the previous exercise, we encountered a dataframe df1 which contained categorical features and therefore, was unsuitable for applying ML algorithms to.

# In this exercise, your task is to convert df1 into a format that is suitable for machine learning.

# Instructions 1/3
# 35 XP
# Use the columns attribute to print the features of df1.

# Instructions 2/3
# 35 XP
# Use the pd.get_dummies() function to perform one-hot encoding on feature 5 of df1.

# Instructions 3/3
# 30 XP
# Use the columns attribute again to print the new features of df1.
# Print the first five rows of df1 using head().


# Print the features of df1 (Instruction 1)
print(df1.columns)

# Perform one-hot encoding (Instruction 2)
df1 = pd.get_dummies(df1, columns=['feature 5'])

# Print the new features of df1 (Instruction 3)
print(df1.columns)

# Print first five rows of df1
print(df1.head())
