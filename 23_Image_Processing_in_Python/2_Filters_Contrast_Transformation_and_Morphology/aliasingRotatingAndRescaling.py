# Aliasing, rotating and rescaling
# Let's look at the impact of aliasing on images.

# Remember that aliasing is an effect that causes different signals, in this case pixels, to become indistinguishable or distorted.

# You'll make this cat image upright by rotating it 90 degrees and then rescaling it two times. Once with the anti aliasing filter applied before rescaling and a second time without it, so you can compare them.

# Little cute cat
# Image preloaded as image_cat.
# Instructions 1/4
# 25 XP
# Import the module and the rotating and rescaling functions.

# Instructions 2/4
# 25 XP
# Rotate the image 90 degrees clockwise.

# Instructions 3/4
# 25 XP
# Rescale the cat_image to be 4 times smaller and apply the anti aliasing filter. Set whether or not the image should be treated as multichannel (colored).

# Instructions 4/4
# 25 XP
# Rescale the rotated_cat_image to be 4 times smaller without applying an anti aliasing filter.


# Import the module and the rotate and rescale functions (Instruction 1)
from skimage.transform import rotate, rescale

# Rotate the image 90 degrees clockwise (Instruction 2)
rotated_cat_image = rotate(image_cat, -90)

# Rescale with anti aliasing (Instruction 3)
rescaled_with_aa = rescale(rotated_cat_image, 1/4, anti_aliasing=True, multichannel=True)

# Rescale without anti aliasing (Instruction 4)
rescaled_without_aa = rescale(rotated_cat_image, 1/4, anti_aliasing=False, multichannel=True)

# Show the resulting images
show_image(rescaled_with_aa, "Transformed with anti aliasing")
show_image(rescaled_without_aa, "Transformed without anti aliasing")
