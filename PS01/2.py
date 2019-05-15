import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('images/horses.mov')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    intensity = np.average(frame)
    mean = np.average(frame)
    plt.plot(mean)
    # Display the resulting frame
    cv2.imshow('Frame',frame)
    # Press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
plt.show()
# Closes all the frames
cv2.destroyAllWindows()
