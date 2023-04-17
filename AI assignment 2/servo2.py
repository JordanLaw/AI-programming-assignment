import cv2
from ultralytics.yolo.utils import yaml_load
from ultralytics.yolo.utils.checks import check_yaml
from yolo_segmentation import YOLO_Segmentation
from yolo_segmentation import YOLO_Detection
import time
import serial

ser = serial.Serial('COM7', baudrate=115200, timeout=1) # Check and change the COM port to match with your Arduino connection
time.sleep(0.5)
pos = 90
pos1 = 90

CLASSES = yaml_load(check_yaml('coco128.yaml'))['names']
print(CLASSES)
#ys = YOLO_Segmentation("yolov8m-seg.pt")
yd = YOLO_Detection("yolov8n.pt")

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

font = cv2.FONT_HERSHEY_PLAIN

item = 67

while True:
    _, img = cam.read()
    startTime = time.time()
    if cv2.waitKey(1) & 0xff == ord('s'):
        item = int(input())

    #bboxes, classes, segmentations, scores = ys.detect(img)
    bboxes, class_ids, scores = yd.detect(img)
    #for bbox, class_id, seg, score in zip(bboxes, classes, segmentations, scores):
    for bbox, class_id, score in zip(bboxes, class_ids, scores):
        #print("bbox:", bbox, "class id:", class_id, "seg:", seg, "score:", score)
        (x, y, x2, y2) = bbox
        if score > 0.6:
            if class_id == item:
                cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 2)

                #cv2.polylines(img, [seg], True, (0, 0, 255), 4)
                label = f'{CLASSES[class_id]} ({score:.2f})'
                #cv2.putText(img, str(class_id), (x, y - 10), font, 2, (0, 0, 255), 2)
                cv2.putText(img, label, (x, y - 10), font, 2, (0, 0, 255), 2)

                w = x2 - x
                errorPan = (x + w / 2) - 640 / 2
                print('errorPan', errorPan)
                if abs(errorPan) > 20:
                    pos = pos - errorPan / 50
                    #print(type(pos))
                if pos > 170:
                    pos = 170
                    print("Out of range")
                if pos < 10:
                    pos = 10
                    print("out of range")
                servoPos = 'RL' + str(pos) + '\r'
                ser.write(servoPos.encode('utf-8'))
                print('servoPos = ', servoPos)
                time.sleep(0.001)

                h = y2 - y
                errorPan = (y + h / 2) - 480 / 2
                print('errorPan', errorPan)
                if abs(errorPan) > 20:
                    pos1 = pos1 + errorPan / 50
                    #print(type(pos))
                if pos1 > 170:
                    pos = 170
                    print("Out of range")
                if pos1 < 10:
                    pos = 10
                    print("out of range")
                servoPos = 'UD' + str(pos1) + '\r'
                ser.write(servoPos.encode('utf-8'))
                print('servoPos = ', servoPos)
                time.sleep(0.001)


    newTime = time.time()
    FPS = str(int(1 / (newTime - startTime)))
    cv2.putText(img, FPS, (20, 50), font, 3, (255, 0, 0), 3)

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xff == 27:
        break
cam.release()
cv2.destroyAllWindows()

