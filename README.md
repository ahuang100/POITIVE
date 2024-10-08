# POITIVE: Parking Spot Availability Computer Vision Project

## Project Overview
POITIVE is a parking space availability computer vision project. 
Trained Yolov8's object detection CV model on a custom dataset containing multiple images of neighborhood curbs and relative objects (orange box). Actively look for open curbs and measure via a detected relative object. Terminal interface that runs the model given a specified time interval to detect for open parking space. 

## Notes
- Reduced input size (imgsz) to a multiple of 32 due to backbone filter stride of yolov8 architecture. Made sure dataset images follow same dimensional scheme.
- Training terminated at 100 epochs
- Model performance:
  - mAP50: 0.74112
  - val/cls_loss: 1.432

## Usage
The project provides a terminal interface that runs the model at specified time intervals to detect open parking spaces. Notifications sent through text.


## Future Steps
-Camera parallel to the curb case, implement an OBB yolov8 model instead to obtain 4 corners of bounding box. Utilize dist. formula for curb space calculation. 

-Varying perspective case, where the curb seems like its minimizing to a certain point, make use of 2 relative objects of the same height for calibration. Assume linear perspective and apply a linear transformation to length calculation. 

-Expand dataset. 

-Retrain model across varying initializations/epochs. 

-Expand use to cases from neighborhood curbs to parking structures/lots. 

-Create API endpoints and establish a cleaner front facing user interface. 
