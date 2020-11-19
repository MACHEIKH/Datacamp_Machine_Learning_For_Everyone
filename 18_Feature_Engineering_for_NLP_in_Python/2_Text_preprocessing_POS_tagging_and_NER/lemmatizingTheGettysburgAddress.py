# Lemmatizing the Gettysburg address
# In this exercise, we will perform lemmatization on the same gettysburg address from before.

# However, this time, we will also take a look at the speech, before and after lemmatization, and try to adjudge the kind of changes that take place to make the piece more machine friendly.

# Instructions 1/3
# 35 XP
# Print the gettysburg address to the console.

# Instructions 2/3
# 35 XP
# Loop over doc and extract the lemma for each token of gettysburg.

# Instructions 3/3
# 30 XP
# Convert lemmas into a string using join.


import spacy

# Load the en_core_web_sm model (Instruction 2)
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
doc = nlp(gettysburg)

# Generate lemmas
lemmas = [token.lemma_ for token in doc]

# Convert lemmas into a string (Instruction 3)
print(' '.join(lemmas))
