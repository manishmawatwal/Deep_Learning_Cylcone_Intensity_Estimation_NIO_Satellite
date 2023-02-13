root_dir = '/content/drive/MyDrive/Multiclass_Yearwise/data'
extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']  # Add any other image file extensions you want to count

for year in range(2000, 2019):  # Change the range based on the years of your folders
    year_dir = os.path.join(root_dir, str(year))
    for subfolder in ['CS', 'D', 'DD', 'SevereCS', 'VSCS']:
        subfolder_dir = os.path.join(year_dir, subfolder)
        num_images = 0
        for filename in os.listdir(subfolder_dir):
            if any(filename.endswith(ext) for ext in extensions):
                num_images += 1
        print(f'Year: {year}, Subfolder: {subfolder}, Number of Images: {num_images}')