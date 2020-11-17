# Dealing with uncommon categories
# Some features can have many different categories but a very uneven distribution of their occurrences. Take for example Data Science's favorite languages to code in, some common choices are Python, R, and Julia, but there can be individuals with bespoke choices, like FORTRAN, C etc. In these cases, you may not want to create a feature for each value, but only the more common occurrences.

# Instructions 1/3
# 35 XP
# Extract the Country column of so_survey_df as a series and assign it to countries.
# Find the counts of each category in the newly created countries series.

# Instructions 2/3
# 1 XP
# Create a mask for values occurring less than 10 times in country_counts.
# Print the first 5 rows of the mask.

# Instructions 3/3
# 30 XP
# Label values occurring less than the mask cutoff as 'Other'.
# Print the new category counts in countries.


# # Create a series out of the Country column (Instruction 1)
# countries = so_survey_df['Country']

# # Get the counts of each category
# country_counts = countries.value_counts()

# # Print the count values for each category
# print(country_counts)


# # Create a series out of the Country column (Instruction 2)
# countries = so_survey_df['Country']

# # Get the counts of each category
# country_counts = countries.value_counts()

# # Create a mask for only categories that occur less than 10 times
# mask = countries.isin(country_counts[country_counts < 10].index)

# # Print the top 5 rows in the mask series
# print(mask.head())


# Create a series out of the Country column (Instruction 3)
countries = so_survey_df['Country']

# Get the counts of each category
country_counts = countries.value_counts()

# Create a mask for only categories that occur less than 10 times
mask = countries.isin(country_counts[country_counts < 10].index)

# Label all other categories as Other
countries[mask] = 'Other'

# Print the updated category counts
print(pd.value_counts(countries))
