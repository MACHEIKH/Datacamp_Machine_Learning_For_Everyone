# Train XGBoost models
# Every Machine Learning method could potentially overfit. You will see it on this example with XGBoost. Again, you are working with the Store Item Demand Forecasting Challenge. The train DataFrame is available in your workspace.

# Firstly, let's train multiple XGBoost models with different sets of hyperparameters using XGBoost's learning API. The single hyperparameter you will change is:

# max_depth - maximum depth of a tree. Increasing this value will make the model more complex and more likely to overfit.
# Instructions 1/3
# 35 XP
# Set the maximum depth to 2. Then hit Submit Answer button to train the first model.

# Instructions 2/3
# Now, set the maximum depth to 8. Then hit Submit Answer button to train the second model.

# Instructions 3/3
# Finally, set the maximum depth to 15. Then hit Submit Answer button to train the third model.


# import xgboost as xgb

# # Create DMatrix on train data (Instruction 1)
# dtrain = xgb.DMatrix(data=train[['store', 'item']],
#                      label=train['sales'])

# # Define xgboost parameters
# params = {'objective': 'reg:linear',
#           'max_depth': 2,
#           'silent': 1}

# # Train xgboost model
# xg_depth_2 = xgb.train(params=params, dtrain=dtrain)


# import xgboost as xgb

# # Create DMatrix on train data (Instruction 2)
# dtrain = xgb.DMatrix(data=train[['store', 'item']],
#                      label=train['sales'])

# # Define xgboost parameters
# params = {'objective': 'reg:linear',
#           'max_depth': 8,
#           'silent': 1}

# # Train xgboost model
# xg_depth_8 = xgb.train(params=params, dtrain=dtrain)


import xgboost as xgb

# Create DMatrix on train data (Instruction 3)
dtrain = xgb.DMatrix(data=train[['store', 'item']],
                     label=train['sales'])

# Define xgboost parameters
params = {'objective': 'reg:linear',
          'max_depth': 15,
          'silent': 1}

# Train xgboost model
xg_depth_15 = xgb.train(params=params, dtrain=dtrain)
