import cv2
cap=cv2.VideoCapture("/Users/apoorvgarg/Documents/ms/1-1/cv/project/Object-detection-and-tracking/project_bb.avi")
cap.open('/Users/apoorvgarg/Documents/ms/1-1/cv/project/Object-detection-and-tracking/project_bb.avi')
if cap.isOpened==False:
    print("Error opening")
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        cv2.imshow('bb',frame)
        if cv2.waitKey(25)&0xFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
