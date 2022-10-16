import streamlit as st
from PIL import Image, ImageOps
import numpy as np

from binary_classification import binary_classification

st.title('Binary Image Classification')
st.header("This is an image classification web app to predict cyclone intensity")
st.text("Upload an image for image classification")

uploaded_file = st.file_uploader("Upload a cyclone image ...", type = "jpg", key = 1)

if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption = 'Uploaded Cyclone.', use_column_width = True)
        st.write("")
        
        st.write("Classifying...")
        label = binary_classification(image, "C:\\Users\\mawat\\Downloads\\research_1\\binary_own_model.hdf5")
        if label == 0:
                st.write("Not a Cyclone")
        else:
                st.write("Cyclone")
                
