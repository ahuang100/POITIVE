
POITIVE: Parking Spot Availability Detection
POITIVE is a computer vision-based parking spot availability project, leveraging the YOLOv8 object detection model. The system is trained to detect available parking spaces by analyzing neighborhood curbs and relevant surrounding objects like orange boxes.

Features
Trained on a custom dataset of neighborhood curb images and relative objects (orange boxes) for parking spot detection.
Utilizes YOLOv8’s object detection capabilities to actively identify open parking spaces.
Terminal interface that runs the model at specified time intervals to continuously check for available parking spaces.
Accurate detection with YOLOv8, achieving a mean average precision (mAP) score of 0.74112 mAP50 after 100 epochs of training.
Model Details
YOLOv8 Architecture: Reduced input image size to a multiple of 32 to align with the backbone filter stride of the YOLOv8 model.
Training Summary:
Dataset followed a consistent dimension scheme.
Training stopped at 100 epochs.
Achieved a validation classification loss (val/cls_loss) of 1.432.
Future Plans
Camera Parallel to Curb:

Implement an oriented bounding box (OBB) YOLOv8 model to capture the 4 corners of the bounding box.
Use distance formulas to calculate the exact curb space available.
Varying Perspective:

For views where the curb seems to minimize into the distance, use two relative objects of known height for calibration.
Apply a linear transformation based on the perspective to estimate parking space dimensions.
Further Improvements:

Expand the dataset to include more diverse environments.
Retrain the model with varying initializations and epochs to improve performance.
Extend usage to other parking scenarios like parking structures or lots.
UI & API Enhancements:

Create API endpoints for integration.
Design a cleaner and more user-friendly front-end interface.
