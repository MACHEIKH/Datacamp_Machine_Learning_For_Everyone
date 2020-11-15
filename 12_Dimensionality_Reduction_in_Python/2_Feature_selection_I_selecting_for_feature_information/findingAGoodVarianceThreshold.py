# Finding a good variance threshold
# You'll be working on a slightly modified subsample of the ANSUR dataset with just head measurements pre-loaded as head_df.

# Instructions 1/4
# 35 XP
# Create a boxplot on head_df.

# Instructions 2/4
# 35 XP
# Normalize the data by dividing the dataframe with its mean values.

# Instructions 3/4
# 0 XP
# Print the variances of the normalized data.


# Create the boxplot (Instruction 1)
# head_df.boxplot()

# plt.show()


# Normalize the data (Instruction 2)
# normalized_df = head_df / np.mean(head_df)

# normalized_df.boxplot()
# plt.show()


# Normalize the data (Instruction 3)
normalized_df = head_df / head_df.mean()

# Print the variances of the normalized data
print(normalized_df.var())
