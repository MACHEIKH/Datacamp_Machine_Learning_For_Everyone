# Prepare a submission
# You've already built a model on the training data from the Kaggle Store Item Demand Forecasting Challenge. Now, it's time to make predictions on the test data and create a submission file in the specified format.

# Your goal is to read the test data, make predictions, and save these in the format specified in the "sample_submission.csv" file. The rf object you created in the previous exercise is available in your workspace.

# Note that starting from now and for the rest of the course, pandas library will be always imported for you and could be accessed as pd.

# Instructions 1/2
# 50 XP
# Read "test.csv" and "sample_submission.csv" files using pandas.
# Look at the head of the sample submission to determine the format.

# Instructions 2/2
# 50 XP
# Note that sample submission has id and sales columns. Now, make predictions on the test data using the rf model, that you fitted on the train data.
# Using the format given in the sample submission, write your results to a new file.


# Read test and sample submission data (Instruction 1)
test = pd.read_csv('test.csv')
sample_submission = pd.read_csv('sample_submission.csv')

# Show the head() of the sample_submission
print(sample_submission.head())

# Get predictions for the test set (Instruction 2)
test['sales'] = rf.predict(test[['store', 'item']])

# Write test predictions using the sample_submission format
test[['id', 'sales']].to_csv('kaggle_submission.csv', index=False)
