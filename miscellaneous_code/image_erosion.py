import os
import cv2
# Set the directory to walk through
train_dir = ''
# Set the kernel size for erosion
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

# Walk through the directory
for root, dirs, files in os.walk(val_dir):
  # Iterate through the files
  for file in files:
    # Check if the file is an image
    if file.endswith('.jpg') or file.endswith('.png'):
      # Load the image
      image = cv2.imread(os.path.join(root, file))
      
      # Apply erosion to the image
      eroded_image = cv2.erode(image, kernel)
      
      # Save the eroded image
      cv2.imwrite(os.path.join(root, file), eroded_image)