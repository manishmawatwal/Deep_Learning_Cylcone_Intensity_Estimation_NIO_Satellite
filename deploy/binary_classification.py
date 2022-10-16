#import necessary libraries
import keras
from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def binary_classification(img, weights_file):
    binary_model = keras.models.load_model(weights_file)
    data = np.ndarray(shape = (1, 310, 310, 3), dtype = np.float32)
    image = img
    size = (310, 310)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = binary_model.predict(data)
    return np.argmax(prediction) 