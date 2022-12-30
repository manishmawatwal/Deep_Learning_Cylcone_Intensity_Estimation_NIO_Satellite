val_generator.reset()
val_predictions = xception_model.predict(val_generator)

from sklearn.metrics import confusion_matrix

# Generate predictions for the validation data
val_predictions = xception_model.predict(val_generator)

# Convert the predictions to a one-hot encoded format
val_predictions = np.argmax(val_predictions, axis=1)

# Convert the labels to a one-hot encoded format
val_labels = np.argmax(val_generator.labels, axis=1)

# Calculate the confusion matrix
confusion_matrix = confusion_matrix(val_labels, val_predictions)

print(confusion_matrix)