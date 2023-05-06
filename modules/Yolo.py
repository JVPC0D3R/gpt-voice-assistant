from ultralytics import YOLO
import supervision as sv
import cv2
from PIL import Image

class Eyes():

    def __init__(self, model_path = "./models/yolov8n.pt"):

        self.model = YOLO(model_path)




    def see(self):
        print('\n\n \033[93m System watching...')
        cam = cv2.VideoCapture(0)

        ret, img = cam.read()

        if (ret):

            img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

            result = self.model(source = img_pil)

            detections = sv.Detections.from_yolov8(result[0])

            det_counter = {}

            for bbox, _, conf, class_id, tracker_id in detections:

                x0, y0, x1, y1 = bbox

                det_class = self.model.model.names[class_id]

                if det_class in det_counter:
                    det_counter[det_class] += 1
                else:
                    det_counter[det_class] = 1



            # Create a sentence to describe the detected objects
            detected_items = []

            for item, count in det_counter.items():
                detected_items.append(f"{count} {item}{'' if count == 1 else 's'}")

            return "The model detected: " + ", ".join(detected_items) 

        else:

            return "Vision module failed to load image"   
        

if __name__ == "__main__":

    eyes = Eyes(model_path = "../models/yolov8n.pt")

    print(eyes.see())
