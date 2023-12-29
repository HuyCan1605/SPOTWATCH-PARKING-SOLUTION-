import cv2

import numpy as np


frameWidth = 1080
frameHeight = 1920

# file pre-train detect biển số
platesCascade = cv2.CascadeClassifier("haarcascades/haarcascade_russian_plate_number.xml")


minArea = 500

# open Webcam

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
count = 0


while True:
    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = platesCascade.detectMultiScale(imgGray, 1.1,4)

    for(x,y,w,h) in numberPlates:
        area = w*h
        if area > minArea:

            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
            
            # path to save plate image
            cv2.putText(img, 'NumberPlate', (x,y-5), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

            imgRoi = img[y:y+h, x:x+w]

            cv2.imshow('ROI', imgRoi)
    
    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('l'):
        
        cv2.imwrite("plate"+str(count)+'.jpg', imgRoi)

        cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)

        cv2.putText(img, "Scan Saved", (15,256), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow('Result', img)
        cv2.waitKey(500)
        count +=1



