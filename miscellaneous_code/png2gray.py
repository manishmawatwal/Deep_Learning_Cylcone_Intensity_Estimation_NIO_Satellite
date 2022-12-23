import os
from PIL import Image
def grey():
    directory = "regression_2022\\55"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        img = Image.open(f).convert("L")
        img = img.save(f[:-4]+'.jpg')
grey()