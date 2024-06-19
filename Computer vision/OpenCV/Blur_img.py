import cv2 as cv
from resize import resize_frame
img = cv.imread('Divansh.jpg')
img = resize_frame(img,0.25)
cv.imshow('img',img)
#averaging

average_blur = cv.blur(img,(3,3))
cv.imshow('avrage_blur',average_blur)

#gaussian blur

gaussian_blur = cv.GaussianBlur(img,(5,5),0)
cv.imshow("gauss",gaussian_blur)

#median blur

median_blur = cv.medianBlur(img, 7)
cv.imshow('median',median_blur)

#bilateral blur

bilateral_blur = cv.bilateralFilter(img,10,35,20,)
cv.imshow('bilateral',bilateral_blur)

cv.waitKey(0)
cv.destroyAllWindows()