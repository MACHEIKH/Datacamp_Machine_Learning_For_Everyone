# Getting to know your data
# Pandas is one the most popular packages used to work with tabular data in Python. It is generally imported using the alias pd and can be used to load a CSV (or other delimited files) using read_csv().

# You will be working with a modified subset of the Stackoverflow survey response data in the first three chapters of this course. This data set records the details, and preferences of thousands of users of the StackOverflow website.

# Instructions 1/4
# 50 XP
# Import the pandas library as pd.
# so_survey_csv contains the URL to a CSV file. Import it using Pandas into so_survey_df.

# Instructions 2/4
# 0 XP
# Print the first five rows of so_survey_df.

# Instructions 3/4
# 0 XP
# Print the data type of each column in so_survey_df.


# # Import pandas (Instruction 1)
# import pandas as pd

# # Import so_survey_csv into so_survey_df
# so_survey_df = pd.read_csv(so_survey_csv)


# # Import pandas (Instruction 2)
# import pandas as pd

# # Import so_survey_csv into so_survey_df
# so_survey_df = pd.read_csv(so_survey_csv)

# # Print the first five rows of the DataFrame
# print(so_survey_df.head())


# Import pandas (Instruction 3)
import pandas as pd

# Import so_survey_csv into so_survey_df
so_survey_df = pd.read_csv(so_survey_csv)

# Print the first five rows of the DataFrame
print(so_survey_df.head())

# Print the data type of each column
print(so_survey_df.dtypes)
