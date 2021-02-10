import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Resources/haarcasacde_facefrontal_default.xml")

img = cv2.imread("images/image1.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
cv2.imshow("Face image ",img)
cv2.waitKey(0)


faceCascade = cv2.CascadeClassifier("Resources/haarcasacde_facefrontal_default.xml")
cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success , img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4) #changeable parameters depending on results

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break


cv2.waitKey(0)
