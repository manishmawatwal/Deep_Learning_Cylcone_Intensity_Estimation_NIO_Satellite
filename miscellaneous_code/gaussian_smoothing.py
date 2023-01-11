from PIL import Image, ImageFilter
import os

def apply_gaussian_smoothing(image_path):
    # Open the image
    image = Image.open(image_path)

    # Apply Gaussian smoothing
    image = image.filter(ImageFilter.GaussianBlur)

    # Save the smoothed image
    image.save(image_path)

def process_folder(folder_path):
    # Iterate through all the files in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        # If the file is an image, apply Gaussian smoothing
        if file.endswith(".jpg") or file.endswith(".png"):
            apply_gaussian_smoothing(file_path)
        # If the file is a folder, process the folder
        elif os.path.isdir(file_path):
            process_folder(file_path)

# Set the path to the folder containing the images
folder_path = train_dir
# Process the folder
process_folder(folder_path)

folder_path = val_dir
process_folder(folder_path)