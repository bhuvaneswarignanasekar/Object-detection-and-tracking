import cv2
import numpy as np
import imutils
import json
from pykalman import KalmanFilter

with open('measurements.txt', 'r') as f:
    b=json.load(f)
print(b)
measurements=np.array(b)
measurements=np.delete(measurements,0,0)
print(measurements[0,0],measurements[0,1],measurements[1,0],measurements[1,1])    
print(measurements.shape)
MaskedMeasurements=np.ma.masked_less(measurements,0)
print(MaskedMeasurements.shape)
Transition_Matrix=[[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]]
Observation_Matrix=[[1,0,0,0],[0,1,0,0]]
# print(measurements)
xinit=MaskedMeasurements[0,0]
yinit=MaskedMeasurements[0,1]
vxinit=MaskedMeasurements[1,0]-MaskedMeasurements[0,0]
vyinit=MaskedMeasurements[1,1]-MaskedMeasurements[0,1]
initstate=[xinit,yinit,vxinit,vyinit]
initcovariance=1.0e-1*np.eye(4)
transistionCov=3.0e-8*np.eye(4)
observationCov=1.0e-1*np.eye(2)
kf=KalmanFilter(transition_matrices=Transition_Matrix,
            observation_matrices =Observation_Matrix,
            initial_state_mean=initstate,
            initial_state_covariance=initcovariance,
            transition_covariance=transistionCov,
            observation_covariance=observationCov)
filtered_state_means, filtered_state_covariances = kf.filter(MaskedMeasurements)
print(filtered_state_means.shape)
a= filtered_state_means[:,:2]
print(a.shape)
kf_list=a.tolist()
# print(kf_list)
cap=cv2.VideoCapture("/Users/apoorvgarg/Documents/ms/1-1/cv/project/Object-detection-and-tracking/project_bb_occlusion.avi")
cap.open('/Users/apoorvgarg/Documents/ms/1-1/cv/project/Object-detection-and-tracking/project_bb_occlusion.avi')
if cap.isOpened==False:
    print("Error opening")
count=0
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        for i in range(2,count+1):
            if kf_list[i - 1] is None or kf_list[i] is None:
                continue
            cv2.line(frame, (int(kf_list[i - 1][0]),int(kf_list[i - 1][1])), (int(kf_list[i][0]),int(kf_list[i][1])),  (0, 0, 255), 2)
        print(kf_list[count][0],kf_list[count][1])
        cv2.imshow('bouding box',frame)
        if cv2.waitKey(25)&0xFF==ord('q'):
            break
        count+=1
        print(count)



