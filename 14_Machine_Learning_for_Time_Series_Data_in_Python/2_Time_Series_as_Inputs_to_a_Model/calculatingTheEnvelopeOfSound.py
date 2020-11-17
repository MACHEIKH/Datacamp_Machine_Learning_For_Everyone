# Calculating the envelope of sound
# One of the ways you can improve the features available to your model is to remove some of the noise present in the data. In audio data, a common way to do this is to smooth the data and then rectify it so that the total amount of sound energy over time is more distinguishable. You'll do this in the current exercise.

# A heartbeat file is available in the variable audio.

# Instructions 1/3
# 33 XP
# Visualize the raw audio you'll use to calculate the envelope.

# Instructions 2/3
# 33 XP
# Rectify the audio.
# Plot the result.

# Instructions 3/3
# 34 XP
# Smooth the audio file by applying a rolling mean.
# Plot the result.


# # Plot the raw data first (Instruction 1)
# audio.plot(figsize=(10, 5))
# plt.show()


# # Rectify the audio signal (Instruction 2)
# audio_rectified = audio.apply(np.abs)

# # Plot the result
# audio_rectified.plot(figsize=(10, 5))
# plt.show()


# Smooth by applying a rolling mean (Instruction 3)
audio_rectified_smooth = audio_rectified.rolling(50).mean()

# Plot the result
audio_rectified_smooth.plot(figsize=(10, 5))
plt.show()
