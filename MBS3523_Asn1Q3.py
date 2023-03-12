import cv2

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
camW = 640
camH = 480
cam.set(3, camW)
cam.set(4, camH)
boxW = 80
boxH = 80
BoxPosX = 250
BoxPosY = 200
BoxPosX2 = BoxPosX + boxW
BoxPosY2 = BoxPosY + boxH
movingH = -2
movingV = 2

while True:

    success, frame = cam.read()
    cv2.putText(frame, 'MBS3523 Assignment 1 - Q3  Name: Law Wing Lam', (10, 30), font, 0.7, (0, 255, 0), 2)
    frameRec = cv2.rectangle(frame, (BoxPosX, BoxPosY), (BoxPosX2, BoxPosY2), (0, 255, 0), 3)

    if BoxPosX <= 0 or BoxPosX2 >= camW -1:
        movingV = movingV * (-1)
    if BoxPosY <= 0 or BoxPosY2 >= camH -1:
        movingH = movingH * (-1)

    BoxPosX = BoxPosX + movingV
    BoxPosY = BoxPosY + movingH
    BoxPosX2 = BoxPosX2 + movingV
    BoxPosY2 = BoxPosY2 + movingH

    cv2.imshow('Frame', frameRec)

    if cv2.waitKey(20) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
