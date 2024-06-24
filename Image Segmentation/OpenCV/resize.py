import cv2 as cv 
def resize_frame (frame, scale):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width ,  height)
    new_frame = cv.resize(frame , dimensions, interpolation = cv.INTER_AREA)

    return new_frame
"""
img = cv.imread('Monty.jpg')
cv.imshow('monty',img)
reshaped_img  = resize_frame(img , 0.15)
cv.imshow('montySmall',reshaped_img)
cv.waitKey(0)

capture = cv.VideoCapture('Mahadev.mp4')
while True:
    isTrue, frame = capture.read()
    new_frame = resize_frame (frame , 0.75)
    cv.imshow('video',frame)
    cv.imshow('videoSmall', new_frame)

    if cv.waitKey(20) & 0xFF == ord('k'):
        break
    
capture.release()
cv.destroyAllWindows()"""