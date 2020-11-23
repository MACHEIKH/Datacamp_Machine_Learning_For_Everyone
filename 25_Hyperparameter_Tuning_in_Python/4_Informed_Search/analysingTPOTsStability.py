# Analysing TPOT's stability
# You will now see the random nature of TPOT by constructing the classifier with different random states and seeing what model is found to be best by the algorithm. This assists to see that TPOT is quite unstable when not run for a reasonable amount of time.

# Instructions 1/3
# 35 XP
# Create the TPOT classifier, fit to the data and score using a random_state of 42.

# Instructions 2/3
# Now try using a random_state of 122. The numbers don't mean anything special, but should produce different results.

# Instructions 3/3
# Finally try using the random_state of 99. See how there is a different result again?

 
# # Create the tpot classifier (Instruction 1)
# tpot_clf = TPOTClassifier(generations=2, population_size=4, offspring_size=3, scoring='accuracy', cv=2,
#                           verbosity=2, random_state=42)

# # Fit the classifier to the training data
# tpot_clf.fit(X_train, y_train)

# # Score on the test set
# print(tpot_clf.score(X_test, y_test))


# # Create the tpot classifier (Instruction 2)
# tpot_clf = TPOTClassifier(generations=2, population_size=4, offspring_size=3, scoring='accuracy', cv=2,
#                           verbosity=2, random_state=122)

# # Fit the classifier to the training data
# tpot_clf.fit(X_train, y_train)

# # Score on the test set
# print(tpot_clf.score(X_test, y_test))


# Create the tpot classifier (Instruction 3)
tpot_clf = TPOTClassifier(generations=2, population_size=4, offspring_size=3, scoring='accuracy', cv=2,
                          verbosity=2, random_state=99)

# Fit the classifier to the training data
tpot_clf.fit(X_train, y_train)

# Score on the test set
print(tpot_clf.score(X_test, y_test))
