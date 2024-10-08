from ultralytics import YOLO

def predict(car_length): 
    # LOAD the model
    model = YOLO("runs/detect/train/weights/last.pt")

    #Predict using model 
    results = model(["curbtest.jpg"])

    #Result extraction 
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        result.show()  # display to screen
        result.save(filename="result1.jpg")  # save to disk
        #stores all detected objects in dictionary 
        detect_objects = {'curbs' : []} 
        for box in boxes:
            if(box.cls[0] == 1):
                detect_objects["relobject"] = box.xyxyn
            else: 
                detect_objects['curbs'].append(box.xyxyn)


        #calculate length dimensions using box class
        relobject_xyxyn = detect_objects["relobject"]
        #extracting box height (normalized)
        norm_length = relobject_xyxyn[0][3] - relobject_xyxyn[0][1] 
        #store as a tuple containing normalized height to relative object actual height (inches)
        relobject_tuple = (norm_length, 19)


        #calculate for curb prediction 
        #threshold is length passed in by interface
        #assume buffer space to park is 20 inches 
        threshold = car_length
        for curb in detect_objects['curbs']:
            curb_norm_length = curb[0][2] - curb[0][0] 
            openspace = (curb_norm_length / relobject_tuple[0]) * relobject_tuple[1]
            if(openspace > threshold): 
                return(True)
    
    #there are no available spots based on modeel prediction 
    return(False)
        


if __name__ == "__main__":
   #assume 185 inches as the threshold value for sample 
   predict(185)









