# PCA in a model pipeline
# We just saw that legendary Pokemon tend to have higher stats overall. Let's see if we can add a classifier to our pipeline that detects legendary versus non-legendary Pokemon based on the principal components.

# The data has been pre-loaded for you and split into training and tests datasets: X_train, X_test, y_train, y_test.

# Same goes for all relevant packages and classes(Pipeline(), StandardScaler(), PCA(), RandomForestClassifier()).

# Instructions 1/4
# 25 XP
# Add a scaler, PCA limited to 2 components, and random forest classifier with random_state=0 to the pipeline.

# Instructions 2/4
# 25 XP
# Fit the pipeline to the training data.

# Instructions 3/4
# 25 XP
# Score the model accuracy on the test set.

# Instructions 4/4
# 25 XP
# Repeat the process with 3 extracted components.


# Build the pipeline
pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('reducer', PCA(n_components=3)),
        ('classifier', RandomForestClassifier(random_state=0))])

# Fit the pipeline to the training data
pipe.fit(X_train, y_train)

# Score the accuracy on the test set
accuracy = pipe.score(X_test, y_test)

# Prints the explained variance ratio and accuracy
print(pipe.steps[1][1].explained_variance_ratio_)
print('{0:.1%} test set accuracy'.format(accuracy))
