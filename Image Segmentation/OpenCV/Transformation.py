import cv2 as cv
import numpy as np

img = cv.imread('Raj_Monty.jpg')
cv.imshow('img',img)

#resize the frame
def resize_frame (frame, scale):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return (cv.resize(frame ,dimensions,interpolation=cv.INTER_AREA))
img = resize_frame(img , 0.2)

#Translation
def translate(image, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions  =(image.shape[1],image.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

trans_img = translate(img , 150, 150)
cv.imshow('translated',trans_img)
cv.waitKey(0)
cv.destroyAllWindows()

#Rotation about a point
def rotate(img , angle, rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimension = (width,height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, 45)
rotated_2= rotate(rotated,-45)
cv.imshow('rotated',rotated)
cv.imshow('rotated_2',rotated_2)
cv.waitKey(0)
cv.destroyAllWindows()

#flip

flip = cv.flip(img,0)# 0=inverted, 1=sideway flip, -1 = both axsis flip
cv.imshow("Flip",flip)
cv.waitKey(0)
cv.destroyAllWindows()
#cropping

cropped = img[0:img.shape[1]//2,0:img.shape[0]//2]
cv.imshow("crop",cropped)

cv.waitKey(0)

