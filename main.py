import time
import glob
import cv2

from detect_person import detect_person

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

images = [cv2.imread(img_path) for img_path in glob.glob("images/*.jpg")]

for image in images:
    start_point = time.time()
    detect_person(image)
    print("Czas na zbadanie %.3f sekund " % (time.time() - start_point))

#moduł globe