import cv2

cam = cv2.VideoCapture(0)
camW = 640
camH = 480
cam.set(3, camW)
cam.set(4, camH)


def nil(x):
    pass


cv2.namedWindow('Frame')
cv2.createTrackbar('X_Pos', 'Frame', 200, 640, nil)
cv2.createTrackbar('Y_Pos', 'Frame', 200, 480, nil)

while True:

    success, frame = cam.read()
    x = cv2.getTrackbarPos('X_Pos', 'Frame')
    y = cv2.getTrackbarPos('Y_Pos', 'Frame')

    cv2.line(frame, (0, y), (640, y), (0, 255, 0), 3)
    cv2.line(frame, (x, 0), (x, 480), (0, 255, 0), 3)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xff == 27:  # ESE
        break

cam.release()
cv2.destroyAllWindows()
