def apply_color_mapping(img_path):
    # Load grayscale image
    img = Image.open(img_path)
    pixels = np.array(img)

    # Define the pixel range and the gray shades for each range
    pixel_ranges = {
        (0, 0): [0],        #black
        (1, 59): [150],     #warm medium gray
        (60, 60): [64],     #dark gray
        (61, 84): [150],    #warm medium gray
        (85, 85): [50],     #cold dark gray
        (86, 108): [150],   #warm medium gray
        (109, 109): [241],  #off white 
        (110, 110): [128],  #medium gray
        (111, 134): [241],  #off white
        (135, 135): [135],  #cold medium gray
        (136, 159): [241],  #off white
        (160, 160): [192],  #light gray
        (161, 202): [241],  #off white
        (203, 254): [150],  #warm medium gray
        (255, 255): [255]   #white
    }

    # Iterate through each pixel and calculate the corresponding gray shade
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            pixel_value = pixels[i][j]
            for pixel_range, gray_shades in pixel_ranges.items():
                if pixel_value >= pixel_range[0] and pixel_value <= pixel_range[1]:
                    pixels[i][j] = gray_shades[0]
                    break

    # Overwrite the original image with the new data
    new_img = Image.fromarray(np.array(pixels, dtype=np.uint8))
    new_img.save(img_path)

# Directory containing subfolders with images
dir_path = "/content/drive/MyDrive/Multiclass_Yearwise/test"

# Loop through all subfolders and images in directory and apply color mapping
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            img_path = os.path.join(root, file)
            apply_color_mapping(img_path)