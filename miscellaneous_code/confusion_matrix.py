from sklearn.metrics import confusion_matrix

val_generator.reset()

label_map = dict((v, k) for k, v in train_generator.class_indices.items())
label_map

actualLables_val = [label_map[k] for k in val_generator.classes]
print("Length of actual validation labels:", len(actualLables_val))

# Generate predictions for the validation data
val_predictions = xception_model.predict(val_generator, verbose=1)

# Convert the predictions to a one-hot encoded format
val_predictions = np.argmax(val_predictions, axis=1)
predictedLables_val = [label_map[k] for k in val_predictions]

# Calculate the confusion matrix
confusion_matrix = confusion_matrix(actualLables_val, predictedLables_val)
print(confusion_matrix)

print("Filename \t\t\t Actual \t Predicted")
for i in range(len(actualLables_val)):
    print(actualLables_val[i] + '\t ' + predictedLables_val[i])


