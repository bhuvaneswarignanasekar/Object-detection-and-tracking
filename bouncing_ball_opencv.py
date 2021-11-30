    
import cv2
import numpy as np
img = np.zeros((480,640,3),dtype='uint8')
dx,dy =1,1
x,y = 100,100
num_frames=1000
ith_frame=0
videofile=cv2.VideoWriter('project_bb_occlusion.avi',cv2.VideoWriter_fourcc(*'XVID'), 25, (640,480))
while ith_frame<num_frames:
    ith_frame+=1
    # display frame
    k = cv2.waitKey(10)
    img = np.zeros((480,640,3),dtype='uint8') 

    # Increment the position
    x = x+dx
    y = y+dy

    #create a ball
    cv2.circle(img,(x,y),20,(255,0,0),-1)
    if k != -1:
        break
    
    cv2.rectangle(img,(300,300),(600,400),(255,0,0),-1)
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
    cv2.imshow('bouncing_ball',img)
    videofile.write(img)
cv2.destroyAllWindows()