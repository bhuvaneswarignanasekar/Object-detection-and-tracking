import cv2
import numpy as np
import imutils
import json

with open('measurements.txt', 'r') as f:
    b=json.load(f)
print(b[0])    