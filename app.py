import streamlit as st
import pytesseract
import numpy as np
from PIL import Image 
pytesseract.pytesseract.tesseract_cmd = './.apt/usr/bin/tesseract'
st.title("OCR - Optical Character Recognition")
img = st.sidebar.file_uploader("Choose an image") 
if img is not None:
  img_read = Image.open(img)
  img_new = np.array(img_read)
  st.image(img,caption='Uploaded Image')
  if st.button('PREDICT'):
    op = pytesseract.image_to_string(img_read)
    st.write(op) 
