import cv2 as cv
import numpy as np
from resize import resize_frame
img = cv.imread('school_BDY.jpg')
img = resize_frame(img,0.75)

blank = np.zeros(img.shape[:2],dtype = 'uint8')

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)
cv.waitKey(0)

