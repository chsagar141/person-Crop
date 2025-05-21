import cv2
import os
from ultralytics import YOLO

# Load YOLOv8 model (make sure to download the model first, e.g., 'yolov8n.pt')
model = YOLO('yolov8n.pt')  # Or 'yolov8s.pt', 'yolov8m.pt', etc.

# Input and output directories
input_folder = 'input_images'
output_folder = 'cropped_waist_images'
os.makedirs(output_folder, exist_ok=True)

# Class ID for 'person' in COCO dataset
PERSON_CLASS_ID = 0

# Process each image
for filename in os.listdir(input_folder):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    image_path = os.path.join(input_folder, filename)
    image = cv2.imread(image_path)

    # Detect objects
    results = model(image)

    for i, result in enumerate(results):
        for box in result.boxes:
            if int(box.cls[0]) == PERSON_CLASS_ID:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                # Crop up to waist (approx. halfway from top to bottom)
                waist_y = y1 + (y2 - y1) // 2
                cropped = image[y1:waist_y, x1:x2]

                # Save cropped image
                crop_filename = f"{os.path.splitext(filename)[0]}_person{i}.jpg"
                crop_path = os.path.join(output_folder, crop_filename)
                cv2.imwrite(crop_path, cropped)

print("Done! Cropped images saved in:", output_folder)
