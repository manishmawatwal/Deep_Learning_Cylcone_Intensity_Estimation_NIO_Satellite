#import libraries
from keras.preprocessing import image

#load model
binary_model = load_model('/content/drive/MyDrive/proposed_binary_model.hdf5')
regression_model = load_model('/content/drive/MyDrive/proposed_regression_model.hdf5')

#predict binary class
path = '/content/drive/MyDrive/cyclone_testing/20220507.00-20.jpg'
img = image.load_img(path, target_size = (310, 310))
x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)
images = np.vstack([x])
classes = binary_model.predict(images)
if classes[0] < 0.5:
  print("\n Uploaded image doesn't have a cyclone \n")
else:
  print('Uploaded image has a cyclone')

#predict regression rmse
path = '/content/drive/MyDrive/regression_data/regression_data/40/20090416.09-40.jpg'
img = image.load_img(path, target_size = (310, 310, 3))
x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)
images = np.vstack([x])
regression_prediction = regression_model.predict(images)
print('\nPredicted intensity of the cylone in the image :-', int(regression_prediction))