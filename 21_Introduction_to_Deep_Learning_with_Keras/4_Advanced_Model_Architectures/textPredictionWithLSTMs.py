# Text prediction with LSTMs
# During the following exercises you will build a toy LSTM model that is able to predict the next word using a small text dataset. This dataset consist of cleaned quotes from the The Lord of the Ring movies. You can find them in the text variable.

# You will turn this text into sequences of length 4 and make use of the Keras Tokenizer to prepare the features and labels for your model!

# The Keras Tokenizer is already imported for you to use. It assigns a unique number to each unique word, and stores the mappings in a dictionary. This is important since the model deals with numbers but we later will want to decode the output numbers back into words.

# Instructions
# 100 XP
# Split the text into an array of words using .split().
# Make sentences of 4 words each, moving one word at a time.
# Instantiate a Tokenizer(), then fit it on the sentences with .fit_on_texts().
# Turn sentences into a sequence of numbers calling .texts_to_sequences().


# Split text into an array of words 
words = text.split()

# Make sentences of 4 words each, moving one word at a time
sentences = []
for i in range(4, len(words)):
  sentences.append(' '.join(words[i-4:i]))

# Instantiate a Tokenizer, then fit it on the sentences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

# Turn sentences into a sequence of numbers
sequences = tokenizer.texts_to_sequences(sentences)
print("Sentences: \n {} \n Sequences: \n {}".format(sentences[:5],sequences[:5]))
