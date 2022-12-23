dir_path = '/content/drive/MyDrive/multiclass_augmented/'
count = 0
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('Augmented File count:', count)