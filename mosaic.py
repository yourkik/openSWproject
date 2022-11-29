import cv2

def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst


cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('einstein.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(gray, 1.05, 3, minSize = (150,150))

for (x,y,w,h) in faces:
    img = mosaic_area(img,x,y,w,h)
    
cv2.imshow("mosaic", img)

cv2.waitKey()
cv2.destroyAllWindows()