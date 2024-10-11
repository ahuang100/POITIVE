# !pip install ultralytics
# !curl -L "https://app.roboflow.com/ds/egWDTB1LmW?key=fEQDmp6yKt" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip

import os
from ultralytics import YOLO

# lOAD the pretrained model on COCO dataset
model = YOLO("yolov8n.yaml").load("yolov8n.pt")

#Yolov8 architecture has stride 32 for filters -> scale image size to be multiple of 32
#training the model 
results = model.train(data="data.yaml", epochs=100, imgsz=[1344,1008])










