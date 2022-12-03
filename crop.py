import cv2

def crop(a,b,c,d,img):
     k = img[b - 7:b + d + 7, a - 5:a + c + 5]
     return k
def outprint(num,crop):
     cv2.imwrite("cropped" + str(num) + ".png", crop)
    
 