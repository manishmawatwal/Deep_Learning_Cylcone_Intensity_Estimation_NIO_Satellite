# Read in the image
image = plt.imread('/content/drive/MyDrive/train/CS/20001127.12-45.jpg')

# Print the shape of the image
print(image.shape)
# If the image is a grayscale image, the output will be something like (height, width). 
# If the image is a 3-channel (BGR) image, the output will be something like (height, width, 3).

# Print the number of dimensions in the image
print(image.ndim)
# If the image is a grayscale image, the output will be 2. If the image is a 3-channel image, the output will be 3.

# Display the image
plt.imshow(image)
plt.show()