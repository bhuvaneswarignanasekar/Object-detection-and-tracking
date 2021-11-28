    
import cv2
import numpy as np
img = np.zeros((480,640,3),dtype='uint8')

fgbg = cv2.createBackgroundSubtractorMOG2(); 
dx,dy =1,1
x,y = 100,100
kernel_dil=np.ones((20,20),dtype='uint8')
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

while True:
    # display frame
    cv2.imshow('bouncing_ball',img)
    k = cv2.waitKey(10)
    fgmask = fgbg.apply(img)
    fgmask=cv2.morphologyEx(fgmask, cv2.MORPH_OPEN,kernel)
    dilation=cv2.dilate(fgmask,kernel_dil)
    cv2.imshow('background_subraction',fgmask)
    (contours,hierachy)=cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if (area>50):
            i,j,w,h=cv2.boundingRect(contour)
            frame=cv2.rectangle(img,(i,j),(i+w,j+h),(0,0,255),2)
            roi_vehicle=img[j:j-10+h+5,i:i-8+w+10]
        cv2.imshow('bouding box',img)
    # Increment the position
    x = x+dx
    y = y+dy
    # change y axis
    if y >=480:
        dy *= -1
    elif y<=0:
        dy *= -1

    #change x asix
    if x >=640:
        dx *= -1
    elif x<=0:
        dx *= -1
    #create a ball
    img = np.zeros((480,640,3),dtype='uint8') 
    cv2.circle(img,(x,y),20,(255,0,0),-1)
    if k != -1:
        break
  
cv2.destroyAllWindows()
