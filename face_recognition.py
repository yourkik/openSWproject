import cv2
import crop as c

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('./scientist.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.1,14)

Num = 1

for(x,y,w,h) in faces:
    
    crop = c.crop(x,y,w,h,img)
    c.outprint(Num,crop)
    Num = Num + 1

cv2.imshow('img',img)
cv2.waitKey()