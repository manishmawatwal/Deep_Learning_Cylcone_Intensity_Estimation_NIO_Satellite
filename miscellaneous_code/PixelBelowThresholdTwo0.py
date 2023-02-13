import cv2
import numpy as np

# Load the grayscale image
image = cv2.imread("C:\\Users\\mawat\\Downloads\\journal\\test.jpg", 0)

# Define the threshold
threshold = 128

# Convert all pixels below the threshold to black
image[image < threshold] = 0

# Save the result
cv2.imwrite('black_and_white_image.jpg', image)

