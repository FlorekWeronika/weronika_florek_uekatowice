import imutils
import cv2
from create_picture import  create_picture

def create_model(picture):
    picture = imutils.resize(picture, width=min(900, picture.shape[1]))
    result_pic = create_picture(picture)
    cv2.imshow('image', result_pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()