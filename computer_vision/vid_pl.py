import cv2, time

#read the computer camera (1 camera means index 0) 
video = cv2.VideoCapture(0)
# check : bool --> cehcking if the video is running
#frame : nparray -- > the first img/frame in the video 

a = 1
while True:
    a+=1
    check, frame = video.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV_YV12)
    cv2.imshow("hey",frame)
    key=cv2.waitKey(1) 
    if key == ord("q"):
        break

print(a)
#closes the camera 
video.release()
cv2.destroyAllWindows()