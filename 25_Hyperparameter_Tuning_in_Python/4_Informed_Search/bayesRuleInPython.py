# Bayes Rule in Python
# In this exercise you will undertake a practical example of setting up Bayes formula, obtaining new evidence and updating your 'beliefs' in order to get a more accurate result. The example will relate to the likelihood that someone will close their account for your online software product.

# These are the probabilities we know:

# 7% (0.07) of people are likely to close their account next month
# 15% (0.15) of people with accounts are unhappy with your product (you don't know who though!)
# 35% (0.35) of people who are likely to close their account are unhappy with your product
# Instructions 1/3
# 35 XP
# Assign the different probabilities (as decimals) to variables. p_unhappy is the likelihood someone is unhappy, p_unhappy_close is the probability that someone is unhappy with the product, given they are going to close their account.

# Instructions 2/3
# 35 XP
# Assign the probability that someone will close their account next month to the variable p_close as a decimal.

# Instructions 3/3
# 30 XP
# You interview one of your customers and discover they are unhappy. What is the probability they will close their account, now that you know this evidence? Assign the result to p_close_unhappy and print it.


# Assign probabilities to variables (Instruction 1)
p_unhappy = 0.15
p_unhappy_close = 0.35

# Probabiliy someone will close (Instruction 2)
p_close = 0.07

# Probability unhappy person will close (Instruction 3)
p_close_unhappy = (p_close * p_unhappy_close) / p_unhappy
print(p_close_unhappy)
