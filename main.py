import cv2
import time
from detect_person import detect_person

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

images = [cv2.imread('images/img1.jpg'), cv2.imread('images/img2.jpg'), cv2.imread('images/img3.jpg'),
          cv2.imread('images/img4.jpg')]

for image in images:
    start_point = time.time()
    detect_person(image)
    print("Czas na zbadanie %.3f sekund " % (time.time() - start_point))
