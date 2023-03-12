import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

while True:

    success, frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameBlur = cv2.GaussianBlur(frameGray, (5,5), 0)
    frameCanny = cv2.Canny(frameBlur, 100, 100)
    frameDilate = cv2.dilate(frameCanny, kernel, iterations=1)
    cv2.imshow('Frame', frame)
    cv2.imshow('FrameDilate', frameDilate)

    if cv2.waitKey(20) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
