import cv2 as cv
import numpy as np
blank = np.zeros((400,400),dtype = 'uint8')
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cirlce = cv.circle(blank.copy(),(200,200),200,255,-1)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle,cirlce)
cv.imshow('AND',bitwise_and)

#bitwise OR
bitwise_or = cv.bitwise_or(rectangle,cirlce)
cv.imshow('OR',bitwise_or)

#bitwise XOR
bitwise_XOR = cv.bitwise_xor(rectangle,cirlce)
cv.imshow('XOR',bitwise_XOR)

cv.waitKey(0)