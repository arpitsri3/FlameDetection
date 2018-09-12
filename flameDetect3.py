from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
import cv2
import numpy as np

# Camera Setup:
cam = PiCamera()
cam.resolution = (320,240)
cam.framerate = 32
raw = PiRGBArray(cam)

# Camera Warmup:
sleep(0.1)

for frame in cam.capture_continuous(raw,format='bgr',use_video_port=True):
    img = frame.array
    # Pre-processing:
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    edge = cv2.Canny(thresh1,30,200)
    
    # Defining central ROI:
    roiH,roiW,_ = img.shape
    cv2.rectangle(img,(2*roiW/5,roiH),(3*roiW/5,0),(255,128,0),2)
    pointSetROI = [2*roiW/5,roiH,3*roiW/5,0]
	# Define centroids:
    ROI_Xcent = pointSetROI[0]+abs(pointSetROI[0]-pointSetROI[2])/2
    ROI_Ycent = pointSetROI[1]+abs(pointSetROI[1]-pointSetROI[3])/2
    
    # Flame detection
    _,contours,_ = cv2.findContours(edge,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        # Flame centroid:
        F_Xcent = x+(w/2)
        # Orientation with respect to detected flame:
        #if F_Xcent < ROI_Xcent:
        #    print "left!"
        #elif F_Xcent > ROI_Xcent:
        #    print "right!"
        #else:
        #    print "forward!"

    
    cv2.imshow('img',img)
    
    # Clear current frame:
    raw.truncate(0)
    
    # Exit loop:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)