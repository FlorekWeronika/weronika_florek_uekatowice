from create_model import create_model

def detect_person(picture_path):
    if picture_path is not None:
        create_model(picture_path)
