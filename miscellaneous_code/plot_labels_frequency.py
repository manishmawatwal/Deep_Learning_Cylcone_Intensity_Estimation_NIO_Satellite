import os
import matplotlib.pyplot as plt

train_dir = 'train'
val_dir = 'val'

train_labels = []
train_counts = []
val_labels = []
val_counts = []

for label in os.listdir(train_dir):
    label_dir = os.path.join(train_dir, label)
    if os.path.isdir(label_dir):
        train_labels.append(label)
        train_counts.append(len(os.listdir(label_dir)))

for label in os.listdir(val_dir):
    label_dir = os.path.join(val_dir, label)
    if os.path.isdir(label_dir):
        val_labels.append(label)
        val_counts.append(len(os.listdir(label_dir)))

fig, ax = plt.subplots()
ax.bar(train_labels, train_counts, label = 'Train')
ax.bar(val_labels, val_counts, label = 'Validation')
ax.set_xlabel('Label')
ax.set_ylabel('Number of Files')

for i, v in enumerate(train_counts):
    ax.text(i - 0.25, v + 10, str(v), fontweight = 'bold')
for i, v in enumerate(val_counts):
    ax.text(i + 0.25, v + 10, str(v), fontweight = 'bold') 
    
ax.legend()
plt.show()