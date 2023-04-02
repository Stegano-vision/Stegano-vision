import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO


st.set_page_config(page_title="EXtraction")
status=False

page_bg_img = '''
<style>
.stApp {
background-image: url("https://cdn.wallpapersafari.com/29/6/0V26D1.png");
background-size: cover;
background-repeat:no-repeat;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("# LETS HIDE WHAT IT IS....!")

msg = st.text_input('Enter the secret message without space')
key = st.text_input('Enter the secret key without space(should consist of 4 letters)')
st.write(msg)

img= cv2.imread("C:/Users/glair/Desktop/S7 project/mo4.png", cv2.IMREAD_COLOR)



download = st.button("download", key="lets see")
if download:
    status=cv2.imwrite("C:/Users/glair/Desktop/mo4.png", img)
if status:
    st.write("done")
else:
    st.write("OOOPS...!!!Try again")

#with open(uploaded_file.name, "rb") as file:
 #   btn = st.download_button(
  #          label="Download Image",
   #         data=file,
    #        file_name="made_omr.png",
     #       mime="image/png",
      #     )
