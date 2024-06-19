import cv2 as cv
from resize  import resize_frame

img = cv.imread('Varun.jpg')
img = resize_frame(img , 0.25)
cv.imshow('varun',img)

#BGR to gray scale

def BGR2GRAY (BGR_img ):
    gray = cv.cvtColor(BGR_img, cv.COLOR_BGR2GRAY)
    return gray

#BGR to HSV

def BGR2HSV (BGR_img):
    HSV_img = cv.cvtColor(BGR_img,cv.COLOR_BGR2HSV)
    return HSV_img

#BGR to l*a*b

def BGR2LAB(BGR_img):
    LAB_img = cv.cvtColor(BGR_img,cv.COLOR_BGR2LAB)
    return LAB_img

#BGR to RGB

def BGR2RGB(BGR_img):
    RGB_img = cv.cvtCOLOR(BGR_img,cv.COLOR_BGR2RGB)
    return RGB_img

