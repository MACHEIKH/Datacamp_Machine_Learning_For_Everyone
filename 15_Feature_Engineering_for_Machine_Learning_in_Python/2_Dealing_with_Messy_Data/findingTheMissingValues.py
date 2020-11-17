# Finding the missing values
# While having a summary of how much of your data is missing can be useful, often you will need to find the exact locations of these missing values. Using the same subset of the StackOverflow data from the last exercise (sub_df), you will show how a value can be flagged as missing.

# Instructions 1/3
# 35 XP
# Print the first 10 entries of the DataFrame.

# Instruction 2/3
# Print the locations of the missing values in the first 10 rows.

# Instruction 3/3
# Print the locations of the non-missing values in the first 10 rows.


# # Print the top 10 entries of the DataFrame (Instruction 1)
# print(sub_df.head(10))


# # Print the locations of the missing values (Instruction 2)
# print(sub_df.head(10).isnull())


# Print the locations of the non-missing values (Instruction 3)
print(sub_df.head(10).notnull())
