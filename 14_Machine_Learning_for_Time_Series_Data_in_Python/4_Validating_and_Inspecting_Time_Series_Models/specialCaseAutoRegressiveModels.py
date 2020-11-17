# Special case: Auto-regressive models
# Now that you've created time-shifted versions of a single time series, you can fit an auto-regressive model. This is a regression model where the input features are time-shifted versions of the output time series data. You are using previous values of a timeseries to predict current values of the same timeseries (thus, it is auto-regressive).

# By investigating the coefficients of this model, you can explore any repetitive patterns that exist in a timeseries, and get an idea for how far in the past a data point is predictive of the future.

# Instructions
# 100 XP
# Replace missing values in prices_perc_shifted with the median of the DataFrame and assign it to X.
# Replace missing values in prices_perc with the median of the series and assign it to y.
# Fit a regression model using the X and y arrays.


# Replace missing values with the median for each column
X = prices_perc_shifted.fillna(np.nanmedian(prices_perc_shifted))
y = prices_perc.fillna(np.nanmedian(prices_perc))

# Fit the model
model = Ridge()
model.fit(X, y)
