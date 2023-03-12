import cv2

cam = cv2.VideoCapture(0)
camW = 640
camH = 480
cam.set(3, camW)
cam.set(4, camH)

font = cv2.FONT_HERSHEY_SIMPLEX

faceCascade = cv2.CascadeClassifier('Resource/haarcascade_frontalface_default.xml')

while True:

    success, frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameGray = cv2.cvtColor(frameGray, cv2.COLOR_GRAY2BGR)
    faces = faceCascade.detectMultiScale(frameGray, 1.1, 10)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x+w), (y+h)), (0, 255, 0), 2)
        frameGray[y:(y+h), x:(x+w)] = frame[y:(y+h), x:(x+w)]

    cv2.putText(frameGray, 'MBS3523 Assignment 1 - Q5  Name: Law Wing Lam', (10, 30), font, 0.7, (0, 255, 0), 2)
    cv2.imshow('FrameGray', frameGray)

    if cv2.waitKey(20) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
