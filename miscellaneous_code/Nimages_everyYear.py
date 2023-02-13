root_dir = '/content/drive/MyDrive/Multiclass_Yearwise/data'
extensions = ['.jpg', '.jpeg', '.png']  # Add any other image file extensions you want to count

total_images = 0
for year in range(2000, 2023):  # Change the range based on the years of your folders
    year_dir = os.path.join(root_dir, str(year))
    num_images = 0
    for subfolder in ['CS', 'D', 'DD', 'SevereCS', 'VSCS']:
        subfolder_dir = os.path.join(year_dir, subfolder)
        for filename in os.listdir(subfolder_dir):
            if any(filename.endswith(ext) for ext in extensions):
                num_images += 1
    total_images += num_images 
    print(f'Year: {year}, Number of Images: {num_images}')
print(f'Total number of images: {total_images}')