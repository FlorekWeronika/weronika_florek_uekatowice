import cv2

HOGCV = cv2.HOGDescriptor()

def create_picture(picture):
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(picture, winStride = (4, 4), padding = (8, 8), scale = 1.05)
    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(picture, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(picture, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1
    print(f'Wykryto: {person - 1}')
    return picture
