import cv2 as cv
capture = cv.VideoCapture('Mahadev.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video' , frame)

    if cv.waitKey(20) & 0xFF == ord('k'):
        break
capture.release()
cv.destroyAllWindows()