# Comparing linear_kernel and cosine_similarity
# In this exercise, you have been given tfidf_matrix which contains the tf-idf vectors of a thousand documents. Your task is to generate the cosine similarity matrix for these vectors first using cosine_similarity and then, using linear_kernel.

# We will then compare the computation times for both functions.

# Instructions 1/2
# 50 XP
# Compute the cosine similarity matrix for tfidf_matrix using cosine_similarity.

# Instructions 2/2
# Compute the cosine similarity matrix for tfidf_matrix using linear_kernel.


# # Record start time (Instruction 1)
# start = time.time()

# # Compute cosine similarity matrix
# cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# # Print cosine similarity matrix
# print(cosine_sim)

# # Print time taken
# print("Time taken: %s seconds" %(time.time() - start))

 
# Record start time (Instruction 2)
start = time.time()

# Compute cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Print cosine similarity matrix
print(cosine_sim)

# Print time taken
print("Time taken: %s seconds" %(time.time() - start))
