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

        output = ""

        if (ret):

            img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

            result = self.model(source = img_pil)

            detections = sv.Detections.from_yolov8(result[0])

            det_counter = {}
            person_boxes = []

            for bbox, _, conf, class_id, tracker_id in detections:

                det_class = self.model.model.names[class_id]

                if det_class in det_counter:
                    det_counter[det_class] += 1
                else:
                    det_counter[det_class] = 1

                if det_class == "person":
                    person_boxes.append(bbox)

            for person_bbox in person_boxes:
                for bbox, _, conf, class_id, tracker_id in detections:
                    det_class = self.model.model.names[class_id]
                    if det_class != "person" and self._is_box_inside(person_bbox, bbox):

                        output = f"One person is holding a {det_class}\n"

            # Create a sentence to describe the detected objects
            detected_items = []

            for item, count in det_counter.items():
                detected_items.append(f"{count} {item}{'' if count == 1 else 's'}")


            output = "The model detected: " + ", ".join(detected_items) + f"\n {output}"

            return output

        else:

            return "Vision module failed to load image"

    def _get_intersection_area(self, box1, box2):
        x0_1, y0_1, x1_1, y1_1 = box1
        x0_2, y0_2, x1_2, y1_2 = box2

        x0_inter = max(x0_1, x0_2)
        y0_inter = max(y0_1, y0_2)
        x1_inter = min(x1_1, x1_2)
        y1_inter = min(y1_1, y1_2)

        if x1_inter < x0_inter or y1_inter < y0_inter:
            return 0

        return (x1_inter - x0_inter) * (y1_inter - y0_inter)

    def _is_box_inside(self, box1, box2):
        intersection_area = self._get_intersection_area(box1, box2)
        area_1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        area_2 = (box2[2] - box2[0]) * (box2[3] - box2[1])

        ratio_1 = intersection_area / area_1
        ratio_2 = intersection_area / area_2

        return ratio_1 >= 0.5 or ratio_2 >= 0.5

        

if __name__ == "__main__":

    eyes = Eyes(model_path = "../models/yolov8n.pt")

    print(eyes.see())
