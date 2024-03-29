#Face Detection
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
faceCas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    val,frame=cap.read()
    img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCas.detectMultiScale(img_gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    #draw rectangle
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3)
        
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cap.destroyAllWindows()

#capturing selfie
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
i=0
while True:
   val,frame=cap.read()
   cv2.imwrite('MySelfie/saved{}.png'.format(i),frame)
   i +=1
   cv2.imshow('Video',frame)
   if cv2.waitKey(1) & 0xFF==ord('q'):
       break
cap.release()
cap.destroyAllWindows()