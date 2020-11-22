# Medical images
# You are trying to improve the tools of a hospital by pre-processing the X-ray images so that doctors have a higher chance of spotting relevant details. You'll test our code on a chest X-ray image from the National Institutes of Health Chest X-Ray Dataset
# X-ray chest image

# Image loaded as chest_xray_image.
# First, you'll check the histogram of the image and then apply standard histogram equalization to improve the contrast. Remember we obtain the histogram by using the hist() function from Matplotlib, which has been already imported as plt.

# Instructions 1/4
# 25 XP
# Import the required Scikit-image module for contrast.

# Instructions 2/4
# 25 XP
# Show the histogram from the original x-ray image chest_xray_image, using the hist() function.

# Instructions 3/4
# 25 XP
# Use histogram equalization on chest_xray_image to obtain the improved image and load it as xray_image_eq.

# Instructions 4/4
# 25 XP
# Show the resulting improved image xray_image_eq.


# Import the required module (Instruction 1)
from skimage import exposure

# Show original x-ray image and its histogram (Instruction 2)
show_image(chest_xray_image, 'Original x-ray')

plt.title('Histogram of image')
plt.hist(chest_xray_image.ravel(), bins=256)
plt.show()

# Use histogram equalization to improve the contrast (Instruction 3)
xray_image_eq =  exposure.equalize_hist(chest_xray_image)

# Show the resulting image (Instruction 4)
show_image(xray_image_eq, 'Resulting image')
