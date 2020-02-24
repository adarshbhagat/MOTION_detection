import cv2
import time as t
cap = cv2.VideoCapture(0)
while(1):
    _, frame = cap.read()
    frame1=cv2.resize(frame, (300,300))
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    diff=0
    _, frame = cap.read()
    frame2=cv2.resize(frame, (300,300))
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    for i in range(0,300,+5):
        for j in range(0,300,+5):
            x = int(frame2[i][j])
            y = int(frame1[i][j])
            diff = diff + abs(x-y)
    if diff-5000 > 0:
        print("motion detected")
    else:
        print("no motion")
    t.sleep((1/60)*(1/1000)*50)
