# Let's restore a damaged image
# In this exercise, we'll restore an image that has missing parts in it, using the inpaint_biharmonic() function.

# Small cute puppy
# Loaded as defect_image.
# We'll work on an image from the data module, obtained by data.astronaut(). Some of the pixels have been replaced by 1s using a binary mask, on purpose, to simulate a damaged image. Replacing pixels with 1s turns them totally black. The defective image is saved as an array called defect_image.

# The mask is a black and white image with patches that have the position of the image bits that have been corrupted. We can apply the restoration function on these areas. This mask is preloaded as mask.

# Remember that inpainting is the process of reconstructing lost or deteriorated parts of images and videos.

# Instructions 1/3
# 35 XP
# Import the inpaint function in the restoration module in scikit-image (skimage).

# Instructions 2/3
# 35 XP
# Show the defective image using show_image().

# Instructions 3/3
# 30 XP
# Call the correct function from inpaint. Use the corrupted image as the first parameter, then the mask and multichannel boolean.


# Import the module from restoration (Instruction 1)
from skimage.restoration import inpaint

# Show the defective image (Instruction 2)
show_image(defect_image, 'Image to restore')

# Apply the restoration function to the image using the mask (Instruction 3)
restored_image = inpaint.inpaint_biharmonic(defect_image, mask, multichannel=True)
show_image(restored_image)
