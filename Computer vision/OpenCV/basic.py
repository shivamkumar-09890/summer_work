import cv2 as cv 
#to resize the frame
def resize_frame(frame,scale):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    new_frame = cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

    return new_frame
#read image
img = cv.imread('Divansh.jpg')
img = resize_frame(img,0.25)
cv.imshow('Divyansh',img)

# function for converting frame to grayscale
def convertToGrayScale (frame):
    gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
    return gray
#grayscale image
gray = convertToGrayScale(img)
cv.imshow('gray_divyansh',gray)
# conveting video to grayscale
capture = cv.VideoCapture('Mahadev.mp4')
while True:
    isTrue, frame = capture.read()
    resizedframe = resize_frame(frame,0.75)
    grayScaleFrame = convertToGrayScale(resizedframe)
    cv.imshow('grayScaleVideo',grayScaleFrame)
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF == ord('k'):
        break
capture.release()
cv.destroyAllWindows()  


#fuction to blur frame
def blurFrame(frame,a):
    blur = cv.GaussianBlur(frame,(a,a),cv.BORDER_DEFAULT)

    return blur
#blur image
blur_div = blurFrame(img,5)
cv.imshow("blured",blur_div)

#blur vedio
capture = cv.VideoCapture('Mahadev.mp4')

while True:
    isTrue, frame = capture.read()
    blur_frame = blurFrame(frame,5)
    cv.imshow('blurVideo',blur_frame)

    if cv.waitKey(20) & 0xFF == ord('y'):
        break
capture.release()
cv.destroyAllWindows()

#edge cascade
def edge_detection (frame,thres1,thres2):
    edge = cv.Canny(frame,thres1,thres2)
    return edge

cv.imshow('edge',edge_detection(img,125,175))
cv.waitKey(0)

#edge video
capture = cv.VideoCapture('Mahadev.mp4')
while True:
    isTrue, frame = capture.read()
    edge_frame =edge_detection(frame,125,175)
    cv.imshow('edge_frame',edge_frame)

    if cv.waitKey(20) & 0xFF == ord('y'):
        break
capture.release()
cv.destroyAllWindows()

# dialting image
def dilation(frame,x,y):
    canny = cv.Canny(frame,x,y)
    dilated = cv.dilate(canny , (5,5), iterations = 5)
    return dilated
cv.imshow('dilated',dilation(img,125,175))
cv.waitKey(0)

