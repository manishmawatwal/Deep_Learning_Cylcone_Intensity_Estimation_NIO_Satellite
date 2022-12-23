import splitfolders
def split():
    data_dir = os.path.join('/content/drive/MyDrive/data_categorised_rgb')
    print("No of images in each class of data directory")
    for dir, subdir, files in os.walk(data_dir):
        print(dir,':', str(len(files)))
        
    splitfolders.ratio("/content/drive/MyDrive/data_categorised_rgb", 
                       output = "/content/drive/MyDrive",
                       seed = 6, 
                       ratio = (0.7, 0.2, 0.1), 
                       group_prefix = None, 
                       move = False)

if os.path.exists("/content/drive/MyDrive/multiclass_data_folders/train"):
    print("Files already present in splitted format")
else:
    split()
    print("Files are splitted in the ratio 0.8, 0.2")
