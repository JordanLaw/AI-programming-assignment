import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(3, 1200)
cam.set(4, 600)

point_matrix = np.zeros((2, 2), np.int64)

counter = 0
cropping = False
cropped = False
first_Click = False
x1 = 0
y1 = 0


def click_and_crop(event, x, y, flags, params):
    global counter, cropping, point_matrix, cropped, x1, y1, first_Click
    if cropped:
        if event == cv2.EVENT_RBUTTONDOWN:
            cropped = False
            counter = 0
            point_matrix = np.zeros((2, 2), np.int64)
            cv2.destroyWindow('ROI')

    else:
        if event == cv2.EVENT_LBUTTONDOWN:
            first_Click = True
            x1 = x
            y1 = y
            point_matrix[counter] = x, y
            cropping = True
            counter = counter + 1
            print(x1,y1)

        elif event == cv2.EVENT_MOUSEMOVE:
            if cropping:
                point_matrix[counter] = x, y
                print(x1, y1)
                first_Click = False

        elif event == cv2.EVENT_LBUTTONUP:
            point_matrix[counter] = x, y
            first_Click = False
            cropping = False
            cropped = True


while True:
    success, frame = cam.read()

    if counter == 1:

        print(point_matrix)

        starting_x = point_matrix[0][0]
        starting_y = point_matrix[0][1]

        ending_x = point_matrix[1][0]
        ending_y = point_matrix[1][1]

        if ending_x < starting_x:
            starting_x = point_matrix[1][0]
            starting_y = point_matrix[0][1]

            ending_x = point_matrix[0][0]
            ending_y = point_matrix[1][1]

            if(ending_y < starting_y):
                starting_x = point_matrix[1][0]
                starting_y = point_matrix[1][1]

                ending_x = point_matrix[0][0]
                ending_y = point_matrix[0][1]

        if(ending_y < starting_y):
            starting_x = point_matrix[0][0]
            starting_y = point_matrix[1][1]

            ending_x = point_matrix[1][0]
            ending_y = point_matrix[0][1]

            if(ending_x < starting_x):
                starting_x = point_matrix[1][0]
                starting_y = point_matrix[1][1]

                ending_x = point_matrix[0][0]
                ending_y = point_matrix[0][1]
        if first_Click:
            pass
        else:
            cv2.rectangle(frame, (starting_x, starting_y), (ending_x, ending_y), (0, 255, 0), 3)
            print(point_matrix)
            cv2.namedWindow("ROI", cv2.WINDOW_FULLSCREEN)

            if point_matrix[1][0] == x1:
                ending_x += 1

            if point_matrix[1][1] == y1:
                ending_y += 1

            frame_cropped = frame[starting_y: ending_y, starting_x: ending_x]
            cv2.imshow("ROI", frame_cropped)

    cv2.imshow("Frame", frame)
    cv2.setMouseCallback("Frame", click_and_crop)

    cv2.waitKey(1)
