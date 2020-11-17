# Dealing with stray characters (I)
# In this exercise, you will work with the RawSalary column of so_survey_df which contains the wages of the respondents along with the currency symbols and commas, such as $42,000. When importing data from Microsoft Excel, more often that not you will come across data in this form.

# Instructions 1/2
# 50 XP
# Remove the commas (,) from the RawSalary column.

# Instruction 2/2
# Remove the dollar ($) signs from the RawSalary column.


# # Remove the commas in the column (Instruction 1)
# so_survey_df['RawSalary'] = so_survey_df['RawSalary'].str.replace(',', '')


# Remove the dollar signs in the column (Instruction 2)
so_survey_df['RawSalary'] = so_survey_df['RawSalary'].str.replace('$','')
