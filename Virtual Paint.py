import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
myColors1 = [[5,107,0,19,255,255], #orange values
            [133,56,0,159,156,255], #purple
            [57,76,0,100,255,255]]  #green

myColors = [[64,255,0,106,255,255]]
myColorsValue = [[255,0,0]]     #use chap 5 to get values
myColorsValue1 = [ [51,153,255],     #orange
                  [255,0,255],      #purple
                  [0,255,0]]      #green in the BGR format
#hue,saturation,val to detect the color orange
#can be done by using webcam for the chap5

myPoints =[] #x,y,colorID

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x , y ,w ,h =0 ,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #number of corner points

            x , y, w, h = cv2.boundingRect(approx)

    return x+w//2 ,y #position of circle(pointer) at tip of marker/ bounding box

def findColor(img,myColors,myColorsValue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    i=0
    newPoints=[]
    for color in myColors :
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorsValue[i],cv2.FILLED)
        #cv2.imshow(str(i),mask)
        if x!= 0 and y!= 0:
            newPoints.append([x,y,i])
        i=i+1
    return newPoints

def DrawonCanvas(myPoints,myColorsValue):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),5, myColorsValue[point[2]],cv2.FILLED)


while True:
    success,img= cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorsValue)

    if len(newPoints) != 0 :
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!=0 :

        DrawonCanvas(myPoints,myColorsValue)

    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break