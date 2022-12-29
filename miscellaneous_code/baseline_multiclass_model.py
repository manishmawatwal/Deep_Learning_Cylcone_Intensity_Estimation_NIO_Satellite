from collections import Counter
# Assume y is a list of class labels
class_counts = Counter(class_names)

# Find the most frequent class
most_common_class = class_counts.most_common(1)[0][0]
print('Most common class:', most_common_class)

# Calculate the number of occurrences of the most frequent class
num_most_common_class = class_counts[most_common_class]
print('Num of most common class:', num_most_common_class)

# Calculate the total number of instances in the dataset
total_count = sum(class_counts.values())
print('Total instances in the dataset:', total_count)

# Calculate the baseline accuracy
baseline_accuracy = num_most_common_class / total_count
print('Baseline Accuracy:',baseline_accuracy*100)