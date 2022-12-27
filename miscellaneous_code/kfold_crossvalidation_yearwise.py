import os
import shutil
import random
import csv
import numpy as np

root_dir = 'C:\\Users\\mawat\\Downloads\\multiclass_yearwise'

years = list(range(2000, 2022))

for i in range(len(years) - 2):
    train_file_list = []
    train_label_list= []
    val_file_list = []
    val_label_list = []

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            label = os.path.split(subdir)[1] 
            year = os.path.split(os.path.split(subdir)[0])[1]
            if int(year) in years[:i] + years[i+2:]:
                train_file_list.append(file_path)
                train_label_list.append(label)
            elif int(year) in years[i:i+2]:
                val_file_list.append(file_path)
                val_label_list.append(label)

    with open('train.csv', 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        for file_path, label in zip(train_file_list, train_label_list):
            writer.writerow([file_path, label])
    csvfile.close()
    
    with open('val.csv', 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        for file_path, label in zip(val_file_list, val_label_list):
            writer.writerow([file_path, label])
    csvfile.close()

    if not os.path.exists('train'):
        os.makedirs('train')
    if not os.path.exists('val'):
        os.makedirs('val')

    for file_path, label in zip(train_file_list, train_label_list):
        label_dir = os.path.join('train', label)
        if not os.path.exists(label_dir):
            os.makedirs(label_dir)
        shutil.copy(file_path, label_dir)
    
    for file_path, label in zip(val_file_list, val_label_list):
        label_dir = os.path.join('val', label)
        if not os.path.exists(label_dir):
            os.makedirs(label_dir)
        shutil.copy(file_path, label_dir)