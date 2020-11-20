# De-noising like an autoencoder
# Okay, you have just built an autoencoder model. Let's see how it handles a more challenging task.

# First, you will build a model that encodes images, and you will check how different digits are represented with show_encodings(). To build the encoder you will make use of your autoencoder, that has already being trained. You will just use the first half of the network, which contains the input and the bottleneck output. That way, you will obtain a 32 number output which represents the encoded version of the input image.

# Then, you will apply your autoencoder to noisy images from MNIST, it should be able to clean the noisy artifacts.

# X_test_noise is loaded in your workspace. The digits in this noisy dataset look like this:



# Apply the power of the autoencoder!

# Instructions 1/2
# 50 XP
# Build an encoder model with the first layer of your trained autoencoder model.
# Predict on X_test_noise with your encoder and show the results with show_encodings().

# Instructions 2/2
# 50 XP
# Predict on X_test_noise with your autoencoder, this will effectively perform both the encoding and decoding.
# Plot noisy vs decoded images with compare_plot().


# Build your encoder by using the first layer of your autoencoder (Instruction 1)
encoder = Sequential()
encoder.add(autoencoder.layers[0])

# Encode the noisy images and show the encodings for your favorite number [0-9]
encodings = encoder.predict(X_test_noise)
show_encodings(encodings, number = 1)

# Predict on the noisy images with your autoencoder (Instruction 1)
decoded_imgs = autoencoder.predict(X_test_noise)

# Plot noisy vs decoded images
compare_plot(X_test_noise, decoded_imgs)
