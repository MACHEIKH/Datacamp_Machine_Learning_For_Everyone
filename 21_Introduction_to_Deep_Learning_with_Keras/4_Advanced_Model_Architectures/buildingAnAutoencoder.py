# Building an autoencoder
# Autoencoders have several interesting applications like anomaly detection or image denoising. They aim at producing an output identical to its inputs. The input will be compressed into a lower dimensional space, encoded. The model then learns to decode it back to its original form.

# You will encode and decode the MNIST dataset of handwritten digits, the hidden layer will encode a 32-dimensional representation of the image, which originally consists of 784 pixels (28 x 28). The autoencoder will essentially learn to turn the 784 pixels original image into a compressed 32 pixels image and learn how to use that encoded representation to bring back the original 784 pixels image.

# The Sequential model and Dense layers are ready for you to use.

# Let's build an autoencoder!

# Instructions
# 100 XP
# Create a Sequential model.
# Add a dense layer with as many neurons as the encoded image dimensions and input_shape the number of pixels in the original image.
# Add a final layer with as many neurons as pixels in the input image.
# Compile your autoencoder using adadelta as an optimizer and binary_crossentropy loss, then summarise it.


# Start with a sequential model
autoencoder = Sequential()

# Add a dense layer with input the original image pixels and neurons the encoded representation
autoencoder.add(Dense(32, input_shape=(784, ), activation="relu"))

# Add an output layer with as many neurons as the orginal image pixels
autoencoder.add(Dense(784, activation = "sigmoid"))

# Compile your model with adadelta
autoencoder.compile(optimizer = 'adadelta', loss = 'binary_crossentropy')

# Summarize your model structure
autoencoder.summary()
