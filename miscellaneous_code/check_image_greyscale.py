import cv2
import os

# Loop through the train_dir directory
for root, dirs, files in os.walk(train_dir):
  # Loop through the files in the current directory
  for file in files:
    # Join the file name to the path
    file_path = os.path.join(root, file)
    
    # Read in the image
    image = cv2.imread(file_path)
    
    # Check if the image is grayscale
    if len(image.shape) > 2:
      print(f'{file} is not grayscale')