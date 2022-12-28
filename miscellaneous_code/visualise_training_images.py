import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Create a grid of plots with one row for each label
fig, axs = plt.subplots(nrows=len(train_labels), ncols=5, figsize=(10, len(train_labels)*2))

for i, label in enumerate(train_labels):
  label_dir = os.path.join(train_dir, label)
  file_names = os.listdir(label_dir)[:5]  # choose the first 5 images
  for j, file_name in enumerate(file_names):
    file_path = os.path.join(label_dir, file_name)
    img = mpimg.imread(file_path)
    axs[i, j].imshow(img)
    axs[i, j].set_title(f'Label: {label}')

plt.show()