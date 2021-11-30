import cv2
import numpy as np
import imutils
fgbg = cv2.createBackgroundSubtractorMOG2(); 
kernel_dil=np.ones((20,20),dtype='uint8')
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
cap=cv2.VideoCapture("/Users/apoorvgarg/Documents/ms/1-1/cv/project/Object-detection-and-tracking/project_bb.avi")
cap.open('/Users/apoorvgarg/Documents/ms/1-1/cv/project/Object-detection-and-tracking/project_bb.avi')
videofile=cv2.VideoWriter('bg_subs_trajectory.avi',cv2.VideoWriter_fourcc(*'XVID'), 25, (640,480))

if cap.isOpened==False:
    print("Error opening")
count=0
sensor_measurement=[]
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        cv2.imshow('bb',frame)
        if cv2.waitKey(25)&0xFF==ord('q'):
            break
        fgmask = fgbg.apply(frame)
        fgmask=cv2.morphologyEx(fgmask, cv2.MORPH_OPEN,kernel)
        dilation=cv2.dilate(fgmask,kernel_dil)
        cnts = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)   
        cnts = imutils.grab_contours(cnts)     
        if len(cnts)>0:
            max_area_contour=max(cnts,key=cv2.contourArea)
            (x, y), radius = cv2.minEnclosingCircle(max_area_contour)
            M = cv2.moments(max_area_contour)
            centroid = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            # Thresholding on size of object detected
            if radius>10:
                cv2.circle(frame, centroid, 5, (0, 0, 255), -1)
            sensor_measurement.append(centroid)
            count+=1
	    # loop over the set of tracked points
        for i in range(2, len(sensor_measurement)):
            if sensor_measurement[i - 1] is None or sensor_measurement[i] is None:
                continue
            cv2.line(frame, sensor_measurement[i - 1], sensor_measurement[i], (0, 0, 255), 2)
        cv2.imshow('bouding box',frame)
        videofile.write(frame)

    else:   
        break
print(len(sensor_measurement))
cap.release()
cv2.destroyAllWindows()
