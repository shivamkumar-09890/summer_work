import cv2 as cv

def split_img (img,color_channel=RGB,show=False,mer=False ):
    b,g,r = cv.split(img)
    data = []
    if color_channel == RGB:
      blank = np.zeros(img.shape[:2],dtype ='uint8')
      blue = cv.merge([b,blank,blank])
      green = cv.merge([blank,g,blank])
      red = cv.merge([blank,blank,r])
      data = [blue,green,red]

      if show == True:
        cv.imshow('blue',blue)
        cv.imshow('green',green)
        cv.imshow('red',red)

    
    if color_channel == GRAY:
        data = [b,g,r]

        if show==True:
          cv.imshow('blue',b)
          cv.imshow('green',g)
          cv.imshow('red',r)
          cv.waitkey(0)
        if mer == True:
         cv.imshow('merged',merged)
         merged = cv.merge([b,g,r])
         data.append(merged)
         cv.waitKey(0)

    return data




