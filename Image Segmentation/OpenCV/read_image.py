import cv2 as cv

# Read the image
img_of_monty = cv.imread('Monty.jpg')

# Display the image
cv.imshow('Monty', img_of_monty)

# Wait for a key event indefinitely
cv.waitKey(0)

# Close all OpenCV windows
cv.destroyAllWindows()
