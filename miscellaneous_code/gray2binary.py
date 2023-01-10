import os
import cv2

# Set the directory to walk through
train_dir = ''

# Walk through the directory
for root, dirs, files in os.walk(val_dir):
  # Iterate through the files
  for file in files:
    # Check if the file is an image
    if file.endswith('.jpg') or file.endswith('.png'):
      # Load the image
      image = cv2.imread(os.path.join(root, file))
      
      # Convert the image to grayscale
      gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      
      # Apply thresholding to the grayscale image
      threshold = 128
      _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
      
      # Save the binary image
      cv2.imwrite(os.path.join(root, file), binary_image)