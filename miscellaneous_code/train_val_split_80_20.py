#!pip install split-folders #uncomment this line to install splitfolders library
import splitfolders
# Set the path to the main folder and the destination folder
destination_folder = '/content/drive/MyDrive/multiclass_8020'

# Split the main folder into train and validation sets in a ratio of 80:20
def split():  
    splitfolders.ratio(data_dir, output = destination_folder, seed = 42, ratio = (0.8, 0.2), group_prefix = None, move = False)

if os.path.exists(destination_folder):
    print("Files already present in splitted ratio 0.8, 0.2")
else:
    split()
    print("Files are splitted in the ratio 0.8, 0.2")