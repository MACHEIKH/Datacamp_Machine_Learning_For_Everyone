# Filling continuous missing values
# In the last lesson, you dealt with different methods of removing data missing values and filling in missing values with a fixed string. These approaches are valid in many cases, particularly when dealing with categorical columns but have limited use when working with continuous values. In these cases, it may be most valid to fill the missing values in the column with a value calculated from the entries present in the column.

# Instructions 1/3
# 35 XP
# Print the first five rows of the StackOverflowJobsRecommend column of so_survey_df.

# Instructions 2/3
# 35 XP
# Replace the missing values in the StackOverflowJobsRecommend column with its mean. Make changes directly to the original DataFrame.

# Instructions 3/3
# 30 XP
# Round the decimal values that you introduced in the StackOverflowJobsRecommend column.


# # Print the first five rows of StackOverflowJobsRecommend column (Instruction 1)
# print(so_survey_df['StackOverflowJobsRecommend'].head())


# # Fill missing values with the mean (Instruction 2)
# so_survey_df['StackOverflowJobsRecommend'].fillna(so_survey_df['StackOverflowJobsRecommend'].mean(), inplace=True)

# # Print the first five rows of StackOverflowJobsRecommend column
# print(so_survey_df['StackOverflowJobsRecommend'].head())


# Fill missing values with the mean (Instruction 3)
so_survey_df['StackOverflowJobsRecommend'].fillna(so_survey_df['StackOverflowJobsRecommend'].mean(), inplace=True)

# Round the StackOverflowJobsRecommend values
so_survey_df['StackOverflowJobsRecommend'] = round(so_survey_df['StackOverflowJobsRecommend'])

# Print the top 5 rows
print(so_survey_df['StackOverflowJobsRecommend'].head())
