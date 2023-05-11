import cv2
import numpy as np
import textwrap
#global bubbledimg

count=0

test_str = "hi"
bit_stream = ''.join(format(ord(i), '08b') for i in test_str)
#bit_stream='0000010000111101'
listtt=textwrap.wrap(bit_stream, 5)
Dict={}
question=1
for i in listtt:
    decimal= int(i, 2)
    print(decimal)
    if(decimal<=15):
      # belongs to first set
      #check a or b
      for j in i:
        if(j=='0'):
          option='a'
        else:
          option='b'
        Dict[question]=option
        question=question+1
       

    else:
      # belongs to second set
      #check c or b
      for j in i:
        if(j=='0'):
          option='c'
        else:
          option='d'
        Dict[question]=option
        question=question+1


# Read image.
img = cv2.imread("C:/Users/glair/Desktop/S7 project/mo4.png", cv2.IMREAD_COLOR)
  
# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))
  
# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred, 
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
               param2 = 30, minRadius = 30, maxRadius = 40)
#print(len(detected_circles))


# Draw circles that are detected.
if detected_circles is not None:
  
    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))
  
    
    base_question=0
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        count=count+1
        # Draw the circumference of the circle.
        #cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        
        p=count%40
        if(count==160 or count==320 or count==480 or count==640 or count==800):
            actual_question=base_question+40
            base_question=count/4
            
        else:
            actual_question=base_question+p
        

        if ((count>=1 and count<=40) or (count>=161 and count<=200) or (count>=321 and count<=360) or (count>=481 and count<=520) or (count>=641 and count<=680)):
            alphabet='a'
        elif ((count>=41 and count<=80) or (count>=201 and count<=240) or (count>=361 and count<=400)  or (count>=521 and count<=560) or (count>=681 and count<=720)):
            alphabet='b'
        elif ((count>=81 and count<=120) or (count>=241 and count<=280) or (count>=401 and count<=440)  or (count>=561 and count<=600) or (count>=721 and count<=760)):
            alphabet='c'
        elif ((count>=121 and count<=160) or (count>=281 and count<=320) or (count>=441 and count<=480)  or (count>=601 and count<=640) or (count>=761 and count<=800)):
            alphabet='d'

        print(count, p,actual_question,alphabet)

       
        # black color in BGR
        color = (0, 0, 0)

        # Line thickness of -1 px
        thickness = -1             

        if(actual_question in Dict):
           if(alphabet==Dict[actual_question]):        
                # Using cv2.circle() method
                # Draw a circle of black color of thickness -1 px (filling entire circle)
                img=cv2.circle(img, (a, b), r, color, thickness)





        #print(r)             
        # Draw a small circle (of radius 1) to show the center.
        #cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        #cv2.imshow("Detected Circle", img)
        #cv2.waitKey(0)
        
print(count)
status = cv2.imwrite("C:/Users/glair/Desktop/mo4_3.png", img)

