files = os.listdir(train_dir)
num_classes = 0
for item in files:
  if os.path.isdir(os.path.join(train_dir, item)):
    num_classes += 1
print(f'Number of classes in {train_dir}: {num_classes}')

# Get the class names from the generator
class_names = list(val_generator.class_indices.keys())
print(class_names)

# Get the class indices from the generator
class_indices = train_generator.class_indices
print(class_indices)

import glob# Initialize a dictionary to store the class weights
class_weights = {}

# Iterate over the class indices
for class_name, class_index in class_indices.items():
    # Count the number of images in the class
    num_images = len(glob.glob(f'/content/drive/MyDrive/train/{class_name}/*.jpg'))

    # Calculate the class weight as the inverse of the number of images in the class
    class_weight = 1 / num_images

    # Add the class weight to the dictionary
    class_weights[class_index] = class_weight

print('Class weights:', class_weights)  # {0: 0.01, 1: 0.03, ...}
# class weights are only supported for single mode.fit