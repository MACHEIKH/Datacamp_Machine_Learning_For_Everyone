# Less corners
# In this exercise, you will test what happens when you set the minimum distance between corner peaks to be a higher number. Remember you do this with the min_distance attribute parameter of the corner_peaks() function.

# Building from a bottom perspective
# Image preloaded as building_image.
# The functions show_image(), show_image_with_corners() and required packages have already been preloaded for you. As well as all the previous code for finding the corners. The Harris measure response image obtained with corner_harris() is preloaded as measure_image.

# Instructions 1/3
# 35 XP
# Find the peaks of the corners with a minimum distance of 2 pixels.

# Instructions 2/3
# Find the peaks of the corners with a minimum distance of 40 pixels.

# Instructions 3/3
# Show original and resulting image with corners detected.


# Find the peaks with a min distance of 2 pixels (Instruction 1)
coords_w_min_2 = corner_peaks(measure_image, min_distance=2)
print("With a min_distance set to 2, we detect a total", len(coords_w_min_2), "corners in the image.")

# Find the peaks with a min distance of 40 pixels (Instruction 2)
coords_w_min_40 = corner_peaks(measure_image, min_distance=40)
print("With a min_distance set to 40, we detect a total", len(coords_w_min_40), "corners in the image.")

# Show original and resulting image with corners detected (Instruction 3)
show_image_with_corners(building_image, coords_w_min_2, "Corners detected with 2 px of min_distance")
show_image_with_corners(building_image, coords_w_min_40, "Corners detected with 40 px of min_distance")
