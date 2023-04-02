import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

count=0
global img 
#img= cv2.imread("C:/Users/glair/Desktop/S7 project/mo5.png", cv2.IMREAD_COLOR)
st.set_page_config(page_title="Extraction")


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

st.markdown("# LETS SEE WHAT IT IS....!")



uploaded_file = st.file_uploader("Choose a file")


def detect(uf):

    global count
    global img
    count=0
    # Read image.
    img = cv2.imread(uf, cv2.IMREAD_COLOR)
    
    # Convert to grayscale.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (3, 3))
    
    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_blurred, 
                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                param2 = 30, minRadius = 30, maxRadius = 40)
    
    
    # Draw circles that are detected.
    if detected_circles is not None:
    
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
    
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
    
            # Draw the circumference of the circle.
            cv2.circle(img, (a, b), r, (0, 255, 0), 2)
            #print(r)             
            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
            #cv2.imshow("Detected Circle", img)
            #cv2.waitKey(0)
            count=count+1
    
    


result = st.button("lets see what it is", key="lets see")

if result:
    img=detect(uploaded_file.name)
    st.title("circles detected:")
    st.title(count)
    img.save("new.png")

#with open(uploaded_file.name, "rb") as file:
#    btn = st.download_button(
#            label="Download Image",
#            data=file,
#            file_name="made_omr.png",
#            mime="image/png",
#           )