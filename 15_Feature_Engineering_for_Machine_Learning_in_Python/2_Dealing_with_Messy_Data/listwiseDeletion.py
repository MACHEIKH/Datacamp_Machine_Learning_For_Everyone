# Listwise deletion
# The simplest way to deal with missing values in your dataset when they are occurring entirely at random is to remove those rows, also called 'listwise deletion'.

# Depending on the use case, you will sometimes want to remove all missing values in your data while other times you may want to only remove a particular column if too many values are missing in that column.

# Instructions 1/4
# 35 XP
# Print the number of rows and columns in so_survey_df.

# Instruction 2/4
# Drop all rows with missing values in so_survey_df.

# Instruction 3/4
# Drop all columns with missing values in so_survey_df.

# Instruction 4/4
# Drop all rows in so_survey_df where 'Gender' is missing.


# Print the number of rows and columns (Instruction 1)
print(so_survey_df.shape)


# Create a new DataFrame dropping all incomplete rows (Instruction 2)
no_missing_values_rows = so_survey_df.dropna()

# Print the shape of the new DataFrame
print(no_missing_values_rows.shape)


# Create a new DataFrame dropping all columns with incomplete rows (Instruction 3)
no_missing_values_cols = so_survey_df.dropna(how='any',axis=1)

# Print the shape of the new DataFrame
print(no_missing_values_cols.shape)


# Drop all rows where Gender is missing (Instruction 4)
no_gender = so_survey_df.dropna(subset=['Gender'])

# Print the shape of the new DataFrame
print(no_gender.shape)
