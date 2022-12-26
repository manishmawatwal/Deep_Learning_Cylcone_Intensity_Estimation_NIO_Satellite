import os
import cv2

def load_data():
    X = []
    y = []
    for label in os.listdir('/content/drive/MyDrive/multiclass_data/data_categorised_rgb'):
      print('Label name:',{label})
      for file in os.listdir(f'/content/drive/MyDrive/multiclass_data/data_categorised_rgb/{label}'):
          img = cv2.imread(f'/content/drive/MyDrive/multiclass_data/data_categorised_rgb/{label}/{file}')
          X.append(img)
          y.append(label)
    return np.array(X), np.array(y)

X, y = load_data()

from sklearn.model_selection import KFold
import statistics
kfold = KFold(n_splits = 5, shuffle = True, random_state = 4)
accuracies = []

ResNet50_model = ResNet50(weights='imagenet', include_top = False, input_shape = (310,310,3), classes=5)
for layers in ResNet50_model.layers:
    layers.trainable = True

# resnet50_x = Conv2D(64, (3, 3), activation='relu')(ResNet50_model.output)
# resnet50_x = MaxPooling2D(pool_size=(3, 3))(resnet50_x)
resnet50 = Flatten()(ResNet50_model.output)
resnet50 = Dense(256,activation='relu')(resnet50)
resnet50 = Dense(5,activation='softmax')(resnet50)
model = Model(inputs = ResNet50_model.input, outputs = resnet50)

data_dir = '/content/drive/MyDrive/multiclass_data/data_categorised_rgb'

datagen = ImageDataGenerator(rescale = 1./255, rotation_range = 10, fill_mode='nearest', validation_split = 0.2)

model.compile(optimizer = tf.optimizers.Adam(learning_rate = 0.0001), loss='categorical_crossentropy', metrics = ['accuracy'])

for split_number, (train_index, test_index) in enumerate(kfold.split(X)):
  print(f'Split number: {split_number}')
  X_train, X_test = X[train_index], X[test_index]
  y_train, y_test = y[train_index], y[test_index]
  train_generator = datagen.flow_from_directory(data_dir, target_size = (310, 310), batch_size = 2, class_mode = 'categorical', subset = 'training')
  val_generator = datagen.flow_from_directory(data_dir, target_size = (310, 310), batch_size = 1, class_mode = 'categorical',subset = 'validation', shuffle = False)
  class_weights = {0: 4.67, 1: 5.26, 2: 3.46, 3: 7.19, 4: 6}
  history = model.fit(train_generator, epochs = 30, validation_data = val_generator, class_weight = class_weights)
  accuracy = history.history['accuracy']
  accuracies.append(accuracy)

model.save('/content/drive/MyDrive/proposed_dfmulticlass_model.hdf5')

accuracies = np.array(accuracies).flatten().tolist()
mean_accuracy = statistics.mean(accuracies) 
std_accuracy = statistics.stdev(accuracies)

print(mean_accuracy*100)
print(std_accuracy)

