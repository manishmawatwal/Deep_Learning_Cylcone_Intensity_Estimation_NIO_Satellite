# Define the threshold below which the pixels will be converted to black
threshold = 128

# Define the path to the directory containing the images
img_dir = '/content/drive/MyDrive/Multiclass_Yearwise/backup_data2'

# Walk through the directory and convert each image
for root, dirs, files in os.walk(img_dir):
    for file in files:
        if file.endswith('.jpg') or file.endswith('.jpg') or file.endswith('.png'):
            # Load the image
            img = cv2.imread(os.path.join(root, file), cv2.IMREAD_GRAYSCALE)
            
            # Convert the pixels below the threshold to black
            img[img < threshold] = 0
            
            # Save the converted image
            cv2.imwrite(os.path.join(root, file), img)