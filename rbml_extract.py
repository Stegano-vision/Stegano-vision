import cv2
import numpy as np
import textwrap
#global bubbledimg

count=0
answer={}
# Read image.
img = cv2.imread("C:/Users/glair/Desktop/mo4.png", cv2.IMREAD_COLOR)
  
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
  
    
    coordinates=[]
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        #print(a,b)
        coordinates.append((a,b))
        
        
print(count)
#print(coordinates)
cordinates_sorted = [item[1] for item in sorted([(pt[0],pt) for pt in coordinates])]
#print(coordinates)
base_question=0
for c in cordinates_sorted:
    #print(c[0],c[1])
    count=count+1
    a=c[0]
    b=c[1]
    print(a,b)          

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

    if(img[b-10,a-13][0]==0 and img[b-10,a-13][1]==0 and img[b-10,a-13][2]==0 ):
        if(alphabet=='a' or alphabet=='c'):
            answer[actual_question]='0'
        elif(alphabet=='b' or alphabet=='d'):
            answer[actual_question]='1'
    
    cv2.circle(img, (a-13,b-10), 1, (0, 0, 255), 3)
    cv2.imshow("Detected Circle", img)
    cv2.waitKey(0)
    print(answer)

print(answer)  
myKeys = list(answer.keys())
myKeys.sort()
s = {i: answer[i] for i in myKeys}
print(s)
answer_list=[]
for i in s:
    answer_list.append(s.get(i))
answerstream=''.join(answer_list)
print(answerstream)


              


    #cv2.circle(img, (a-13,b-10), 1, (0, 0, 255), 3)
    #cv2.imshow("Detected Circle", img)
    #cv2.waitKey(0)
    
       

#status = cv2.imwrite("C:/Users/glair/Desktop/mo4.png", img)

       