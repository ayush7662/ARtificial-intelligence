import cv2
import time

cam = cv2.VideoCapture(0)
time.sleep(1)
_,img = cam.read()
cv2.imwrite("image from Camera.jpg",img)
cam.release()