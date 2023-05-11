import cv2
import numpy as np
import textwrap
#global bubbledimg

count=0
answer={}
# Read image.
img = cv2.imread("C:/Users/glair/Desktop/mo4_3.png", cv2.IMREAD_COLOR)
              
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
#cordinates_sorted = [item[1] for item in sorted([(pt[0],pt) for pt in coordinates])]
cordinates_sorted=[(176, 58), (176, 132), (176, 208), (176, 282), (176, 358), (176, 432), (176, 508), (176, 582), (176, 658), (176, 732), (176, 808), (176, 882), (176, 958), (176, 1032), (176, 1108), 
(176, 1182), (176, 1258), (176, 1332), (176, 1408), (176, 1482), (176, 1558), (176, 1632), (176, 1708), (176, 1782), (176, 1858), (176, 1932), (176, 2008), (176, 2082), (176, 2158), 
(176, 2232), (176, 2308), (176, 2382), (176, 2458), (176, 2532), (176, 2608), (176, 2682), (176, 2758), (176, 2832), (176, 2908), (176, 2982), (252, 58), (252, 132), (252, 208), 
(252, 282), (252, 358), (252, 432), (252, 508), (252, 582), (252, 658), (252, 732), (252, 808), (252, 882), (252, 958), (252, 1032), (252, 1108), (252, 1182), (252, 1258), (252, 1332), (252, 1408), 
(252, 1482), (252, 1558), (252, 1632), (252, 1708), (252, 1782), (252, 1858), (252, 1932), (252, 2008), (252, 2082), (252, 2158), (252, 2232), (252, 2308), (252, 2382), (252, 2458), (252, 2532), 
(252, 2608), (252, 2682), (252, 2758), (252, 2832), (252, 2908), (252, 2982), (326, 58), (326, 132), (326, 208), (326, 282), (326, 358), (326, 432), (326, 508), (326, 582), (326, 658), (326, 732), 
(326, 808), (326, 882), (326, 958), (326, 1032), (326, 1108), (326, 1182), (326, 1258), (326, 1332), (326, 1408), (326, 1482), (326, 1558), (326, 1632), (326, 1708), (326, 1782), (326, 1858), (326, 1932), 
(326, 2008), (326, 2082), (326, 2158), (326, 2232), (326, 2308), (326, 2382), (326, 2458), (326, 2532), (326, 2608), (326, 2682), (326, 2758), (326, 2832), (326, 2908), (326, 2982), (402, 58), (402, 132), 
(402, 208), (402, 282), (402, 358), (402, 432), (402, 508), (402, 582), (402, 658), (402, 732), 
(402, 808), (402, 882), (402, 958), (402, 1032), (402, 1108), (402, 1182), (402, 1258), (402, 1332), (402, 1408), (402, 1482), (402, 1558), (402, 1632), (402, 1708), (402, 1782), (402, 1858), (402, 1932), 
(402, 2008), (402, 2082), (402, 2158), (402, 2232), (402, 2308), (402, 2382), (402, 2458), (402, 2532), (402, 2608), (402, 2682), (402, 2758), (402, 2832), (402, 2908), (402, 2982), (596, 58), (596, 132), 
(596, 208), (596, 282), (596, 358), (596, 432), (596, 508), (596, 582), (596, 658), (596, 732), (596, 808), (596, 882), (596, 958), (596, 1032), (596, 1108), (596, 1182), (596, 1258), (596, 1332), (596, 1408), 
(596, 1482), (596, 1558), (596, 1632), (596, 1708), (596, 1782), (596, 1858), (596, 1932), (596, 2008), (596, 2082), (596, 2158), (596, 2232), (596, 2308), (596, 2382), (596, 2458), (596, 2532), (596, 2608), (596, 2682), 
(596, 2758), (596, 2832), (596, 2908), (596, 2982), (672, 58), (672, 132), (672, 208), (672, 282), (672, 358), (672, 432), (672, 508), (672, 582), (672, 658), (672, 732), (672, 808), (672, 882), (672, 958), (672, 1032), 
(672, 1108), (672, 1182), (672, 1258), (672, 1332), (672, 1408), (672, 1482), (672, 1558), (672, 1632), (672, 1708), (672, 1782), (672, 1858), (672, 1932), (672, 2008), (672, 2082), (672, 2158), (672, 2232), (672, 2308), 
(672, 2382), (672, 2458), (672, 2532), (672, 2608), (672, 2682), (672, 2758), (672, 2832), (672, 2908), (672, 2982), (746, 58), (746, 132), (746, 208), (746, 282), (746, 358), (746, 432), (746, 508), (746, 582), (746, 658), 
(746, 732), (746, 808), (746, 882), (746, 958), (746, 1032), (746, 1108), (746, 1182), (746, 1258), (746, 1332), (746, 1408), (746, 1482), (746, 1558), (746, 1632), (746, 1708), (746, 1782), (746, 1858), (746, 1932), (746, 2008), 
(746, 2082), (746, 2158), (746, 2232), (746, 2308), (746, 2382), (746, 2458), (746, 2532), (746, 2608), (746, 2682), (746, 2758), (746, 2832), (746, 2908), (746, 2982), (822, 58), (822, 132), (822, 208), (822, 282), (822, 358), 
(822, 432), (822, 508), (822, 582), (822, 658), (822, 732), (822, 808), (822, 882), (822, 958), (822, 1032), (822, 1108), (822, 1182), (822, 1258), (822, 1332), (822, 1408), (822, 1482), (822, 1558), (822, 1632), (822, 1708), (822, 1782),
(822, 1858), (822, 1932), (822, 2008), (822, 2082), (822, 2158), (822, 2232), (822, 2308), (822, 2382), (822, 2458), (822, 2532), (822, 2608), (822, 2682), (822, 2758), (822, 2832), (822, 2908), (822, 2982), (1016, 58), (1016, 132), 
(1016, 208), (1016, 282), (1016, 358), (1016, 432), (1016, 508), (1016, 582), (1016, 658), (1016, 732), (1016, 808), (1016, 882), (1016, 958), (1016, 1032), (1016, 1108), (1016, 1182), (1016, 1258), (1016, 1332), (1016, 1408), (1016, 1482), 
(1016, 1558), (1016, 1632), (1016, 1708), (1016, 1782), (1016, 1858), (1016, 1932), (1016, 2008), (1016, 2082), (1016, 2158), (1016, 2232), (1016, 2308), (1016, 2382), (1016, 2458), (1016, 2532), (1016, 2608), (1016, 2682), (1016, 2758), (1016, 2832), 
(1016, 2908), (1016, 2982), (1092, 58), (1092, 132), (1092, 208), (1092, 282), (1092, 358), (1092, 432), (1092, 508), (1092, 582), (1092, 658), (1092, 732), (1092, 808), (1092, 882), (1092, 958), (1092, 1032), (1092, 1108), (1092, 1182), (1092, 1258), (1092, 1332), 
(1092, 1408), (1092, 1482), (1092, 1558), (1092, 1632), (1092, 1708), (1092, 1782), (1092, 1858), (1092, 1932), (1092, 2008), (1092, 2082), (1092, 2158), (1092, 2232), (1092, 2308), (1092, 2382), (1092, 2458), (1092, 2532), (1092, 2608), (1092, 2682), (1092, 2758), 
(1092, 2832), (1092, 2908), (1092, 2982), (1166, 58), (1166, 132), (1166, 208), (1166, 282), (1166, 358), (1166, 432), (1166, 508), (1166, 582), (1166, 658), (1166, 732), (1166, 808), (1166, 882), (1166, 958), (1166, 1032), (1166, 1108), (1166, 1182), (1166, 1258), 
(1166, 1332), (1166, 1408), (1166, 1482), (1166, 1558), (1166, 1632), (1166, 1708), (1166, 1782), (1166, 1858), (1166, 1932), (1166, 2008), (1166, 2082), (1166, 2158), (1166, 2232), (1166, 2308), (1166, 2382), (1166, 2458), (1166, 2532), (1166, 2608), (1166, 2682), 
(1166, 2758), (1166, 2832), (1166, 2908), (1166, 2982), (1242, 58), (1242, 132), (1242, 208), (1242, 282), (1242, 358), (1242, 432), (1242, 508), (1242, 582), (1242, 658), (1242, 732), (1242, 808), (1242, 882), (1242, 958), (1242, 1032), (1242, 1108), (1242, 1182), (1242, 1258), (1242, 1332), (1242, 1408), (1242, 1482), (1242, 1558), (1242, 1632), (1242, 1708), (1242, 1782), (1242, 1858), (1242, 1932), (1242, 2008), (1242, 2082), (1242, 2158), (1242, 2232), (1242, 2308), (1242, 2382), (1242, 2458), (1242, 2532), (1242, 2608), (1242, 2682), (1242, 2758), (1242, 2832), (1242, 2908), (1242, 2982), (1436, 58), (1436, 132), (1436, 208), (1436, 282), (1436, 358), (1436, 432), (1436, 508), (1436, 582), (1436, 658), (1436, 732), (1436, 808), (1436, 882), (1436, 958), (1436, 1032), (1436, 1108), (1436, 1182), (1436, 1258), (1436, 1332), (1436, 1408), (1436, 1482), (1436, 1558), (1436, 1632), (1436, 1708), (1436, 1782), (1436, 1858), (1436, 1932), (1436, 2008), (1436, 2082), (1436, 2158), (1436, 2232), (1436, 2308), (1436, 2382), (1436, 2458), (1436, 2532), (1436, 2608), (1436, 2682), (1436, 2758), (1436, 2832), (1436, 2908), (1436, 2982), (1512, 58), (1512, 132), (1512, 208), (1512, 282), (1512, 358), (1512, 432), (1512, 508), (1512, 582), (1512, 658), (1512, 732), (1512, 808), (1512, 882), (1512, 958), (1512, 1032), (1512, 1108), (1512, 1182), (1512, 1258), (1512, 1332), (1512, 1408), (1512, 1482), (1512, 1558), (1512, 1632), (1512, 1708), (1512, 1782), (1512, 1858), (1512, 1932), (1512, 2008), (1512, 2082), (1512, 2158), (1512, 2232), (1512, 2308), (1512, 2382), (1512, 2458), (1512, 2532), (1512, 2608), (1512, 2682), (1512, 2758), (1512, 2832), (1512, 2908), (1512, 2982), (1586, 58), (1586, 132), (1586, 208), (1586, 282), (1586, 358), (1586, 432), (1586, 508), (1586, 582), (1586, 658), (1586, 732), (1586, 808), (1586, 882), (1586, 958), (1586, 1032), (1586, 1108), (1586, 1182), (1586, 1258), (1586, 1332), (1586, 1408), (1586, 1482), (1586, 1558), (1586, 1632), (1586, 1708), (1586, 1782), (1586, 1858), (1586, 1932), (1586, 2008), (1586, 2082), (1586, 2158), (1586, 2232), (1586, 2308), (1586, 2382), (1586, 2458), (1586, 2532), (1586, 2608), (1586, 2682), (1586, 2758), (1586, 2832), (1586, 2908), (1586, 2982), (1662, 58), (1662, 132), (1662, 208), (1662, 282), (1662, 358), (1662, 432), (1662, 508), (1662, 582), (1662, 658), (1662, 732), (1662, 808), (1662, 882), (1662, 958), (1662, 1032), (1662, 1108), (1662, 1182), (1662, 1258), (1662, 1332), (1662, 1408), (1662, 1482), (1662, 1558), (1662, 1632), (1662, 1708), (1662, 1782), (1662, 1858), (1662, 1932), (1662, 2008), (1662, 2082), (1662, 2158), (1662, 2232), (1662, 2308), (1662, 2382), (1662, 2458), (1662, 2532), (1662, 2608), (1662, 2682), (1662, 2758), (1662, 2832), (1662, 2908), (1662, 2982), (1856, 58), (1856, 132), (1856, 208), (1856, 282), (1856, 358), (1856, 432), (1856, 508), (1856, 582), (1856, 658), (1856, 732), (1856, 808), (1856, 882), (1856, 958), (1856, 1032), (1856, 1108), (1856, 1182), (1856, 1258), (1856, 1332), (1856, 1408), (1856, 1482), (1856, 1558), (1856, 1632), (1856, 1708), (1856, 1782), (1856, 1858), (1856, 1932), (1856, 2008), (1856, 2082), (1856, 2158), (1856, 2232), (1856, 2308), (1856, 2382), (1856, 2458), (1856, 2532), (1856, 2608), (1856, 2682), (1856, 2758), (1856, 2832), (1856, 2908), (1856, 2982), (1932, 58), (1932, 132), (1932, 208), (1932, 282), (1932, 358), (1932, 432), (1932, 508), (1932, 582), (1932, 658), (1932, 732), (1932, 808), (1932, 882), (1932, 958), (1932, 1032), (1932, 1108), (1932, 1182), (1932, 1258), (1932, 1332), (1932, 1408), (1932, 1482), (1932, 1558), (1932, 1632), (1932, 1708), (1932, 1782), (1932, 1858), (1932, 1932), (1932, 2008), (1932, 2082), (1932, 2158), (1932, 2232), (1932, 2308), (1932, 2382), (1932, 2458), (1932, 2532), (1932, 2608), (1932, 2682), (1932, 2758), (1932, 2832), (1932, 2908), (1932, 2982), (2006, 58), (2006, 132), (2006, 208), (2006, 282), (2006, 358), (2006, 432), (2006, 508), (2006, 582), (2006, 658), (2006, 732), (2006, 808), (2006, 882), (2006, 958), (2006, 1032), (2006, 1108), (2006, 1182), (2006, 1258), (2006, 1332), (2006, 1408), (2006, 1482), (2006, 1558), (2006, 1632), (2006, 1708), (2006, 1782), (2006, 1858), (2006, 1932), (2006, 2008), (2006, 2082), (2006, 2158), (2006, 2232), (2006, 2308), (2006, 2382), (2006, 2458), (2006, 2532), (2006, 2608), (2006, 2682), (2006, 2758), (2006, 2832), (2006, 2908), (2006, 2982), (2082, 58), (2082, 132), (2082, 208), (2082, 282), (2082, 358), (2082, 432), (2082, 508), (2082, 582), (2082, 658), (2082, 732), (2082, 808), (2082, 882), (2082, 958), (2082, 1032), (2082, 1108), (2082, 1182), (2082, 1258), (2082, 1332), (2082, 1408), (2082, 1482), (2082, 1558), (2082, 1632), (2082, 1708), (2082, 1782), (2082, 1858), (2082, 1932), (2082, 2008), (2082, 2082), (2082, 2158), (2082, 2232), (2082, 2308), (2082, 2382), (2082, 2458), (2082, 2532), (2082, 2608), (2082, 2682), (2082, 2758), (2082, 2832), (2082, 2908), (2082, 2982)]
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

       