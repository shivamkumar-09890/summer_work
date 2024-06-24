import cv2 as cv
import numpy as np

img = cv.imread('Divansh.jpg')
img = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
canny = cv.Canny(img,125,175)

blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
canny_blur =cv.Canny(blur,125,175)

cv.imshow("edge",canny)
cv.imshow("canny_blur",canny_blur)

ret, thres = cv.threshold(gray,125,175,cv.THRESH_BINARY)
cv.imshow("thres",thres)
cv.waitKey(0)
cv.destroyAllWindows()

#contours
contours,hierarchies = cv.findContours(thres,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} countors found')
cv.waitKey(0)
cv.destroyAllWindows()

#visualising the contours
blank = np.zeros(img.shape[:2],dtype='uint8')

blank = cv.drawContours(blank,contours, -1, (0,0,255),2)
cv.imshow('contours',blank)
cv.waitKey(0)




