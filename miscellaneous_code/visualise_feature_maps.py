from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model
from numpy import expand_dims

model = load_model('/content/drive/MyDrive/multiclass_own_model.hdf5')
model.layers

# summarize feature map shapes
for i in range(len(model.layers)):
    layer = model.layers[i]
    if 'conv' not in layer.name:
        continue
    print(i, layer.name, layer.output.shape)

img_path = '/content/drive/MyDrive/cyclone_testing/20220507.12-30.jpg'

# redefine model to output right after the first hidden layer
model = Model(inputs = model.inputs, outputs = model.layers[1].output)
img = load_img(img_path, target_size = (310, 310))

# convert the image to an array
img = img_to_array(img)
# expand dimensions so that it represents a single 'sample'
img = expand_dims(img, axis = 0)
# prepare the image (e.g. scale pixel values for the vgg)
img = preprocess_input(img)
# get feature map for first hidden layer
feature_maps = model.predict(img)
# plot all 32 maps in an 8x8 squares
rows = 8
columns = 4
ix = 1
plt.figure(figsize=(10, 20))
for _ in range(rows):
    for _ in range(columns):
        # specify subplot and turn of axis
        ax = plt.subplot(rows, columns, ix)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.imshow(feature_maps[0, :, :, ix-1], cmap = 'pink')
        ix += 1
plt.tight_layout()
plt.savefig("Feature Maps" + ".jpg", transparent = True, bbox_inches = 'tight')
plt.show()