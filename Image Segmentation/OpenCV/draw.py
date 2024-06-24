import cv2 as cv 
import numpy as np 

blank_img = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('blank',blank_img)

# paint the image green
blank_img[0:50, 0:50] = 0,255,0
cv.imshow('changed', blank_img)
cv.waitKey(0)
#draw a rectangle boundary 
cv.rectangle(blank_img,(50,50),(blank_img.shape[1]//2,blank_img.shape[0]//2),(0,255,0),thickness=2)
cv.imshow('change_2',blank_img)

cv.rectangle(blank_img,(50,50),(100,100),(0,0,255),thickness=-1)
cv.imshow('change_3',blank_img)

#draw a circle given radius and centre
cv.circle(blank_img,(250,250),100,(255,0,0),thickness=2)
cv.imshow('change_4',blank_img)

cv.circle(blank_img,(250,250),70,(30,40,100),thickness=-1)
cv.imshow('change_5',blank_img)

#draw a line
cv.line(blank_img,(0,0),(250,250),(200,200,200),thickness=2)
cv.imshow('change_6',blank_img)
# write a TEXT
cv.putText(blank_img,'hello',(0,250),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),thickness=2)
cv.imshow('change_7',blank_img)
cv.waitKey(0)