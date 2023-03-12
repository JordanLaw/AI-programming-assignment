import cv2
import numpy as np

cam = cv2.VideoCapture(0)

point_matrix = np.zeros((2, 2), np.int64)

counter = 0
cropping = False


def click_and_crop(event, x, y, flags, params):
    global counter, cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix[counter] = x, y
        counter = counter + 1
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        point_matrix[counter] = x, y
        counter = counter + 1
        cropping = False
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        np.delete(point_matrix, 0, 4)


while True:
    success, frame = cam.read()

    for x in range(0, 2):
        cv2.circle(frame, (point_matrix[x][0], point_matrix[x][1]), 3, (0, 255, 0), cv2.FILLED)

    if counter == 2:
        starting_x = point_matrix[0][0]
        starting_y = point_matrix[0][1]

        ending_x = point_matrix[1][0]
        ending_y = point_matrix[1][1]

        cv2.rectangle(frame, (starting_x, starting_y), (ending_x, ending_y), (0, 255, 0), 3)

        frame_cropped = frame[starting_y: ending_y, starting_x: ending_x]
        cv2.imshow("ROI", frame_cropped)

    cv2.imshow("Frame", frame)
    cv2.setMouseCallback("Frame", click_and_crop)
    print(point_matrix)
    cv2.waitKey(1)