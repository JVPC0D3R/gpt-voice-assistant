from ultralytics import YOLO
import cv2
from PIL import Image

def see():
    print('\n\n \033[93m System watching...')
    cam = cv2.VideoCapture(0)

    ret, img = cam.read()

    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    model = YOLO("yolov8n.pt")
    result = model(source = img_pil)

    print('\033[0m')

    return result[0].verbose()
    