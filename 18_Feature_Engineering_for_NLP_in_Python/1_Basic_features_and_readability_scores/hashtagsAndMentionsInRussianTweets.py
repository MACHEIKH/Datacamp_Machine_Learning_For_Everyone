# Hashtags and mentions in Russian tweets
# Let's revisit the tweets dataframe containing the Russian tweets. In this exercise, you will compute the number of hashtags and mentions in each tweet by defining two functions count_hashtags() and count_mentions() respectively and applying them to the content feature of tweets.

# In case you don't recall, the tweets are contained in the content feature of tweets.

# Instructions 1/2
# 50 XP
# In the list comprehension, use startswith() to check if a particular word starts with '#'.

# Instructions 2/2
# In the list comprehension, use startswith() to check if a particular word starts with '@'.


# # Function that returns numner of hashtags in a string (Instruction 1)
# def count_hashtags(string):
# 	# Split the string into words
#     words = string.split()
    
#     # Create a list of words that are hashtags
#     hashtags = [word for word in words if word.startswith('#')]
    
#     # Return number of hashtags
#     return(len(hashtags))

# # Create a feature hashtag_count and display distribution
# tweets['hashtag_count'] = tweets['content'].apply(count_hashtags)
# tweets['hashtag_count'].hist()
# plt.title('Hashtag count distribution')
# plt.show()


# Function that returns number of mentions in a string (Instruction 2)
def count_mentions(string):
	# Split the string into words
    words = string.split()
    
    # Create a list of words that are mentions
    mentions = [word for word in words if word.startswith('@')]
    
    # Return number of mentions
    return(len(mentions))

# Create a feature mention_count and display distribution
tweets['mention_count'] = tweets['content'].apply(count_mentions)
tweets['mention_count'].hist()
plt.title('Mention count distribution')
plt.show()
