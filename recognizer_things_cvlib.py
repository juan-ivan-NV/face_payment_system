from cvlib.object_detection import draw_bbox
from yolov3_items import yolo_labels_prices
#import matplotlib.pyplot as plt
import cvlib as cv
import cv2
import os



def things_classifier():
    
    things = []
    path = 'thing'
    things_buy = {}

    for filename in os.listdir(path):
        if 'jpg' in filename:
            im = cv2.imread(os.path.join(path,filename))
            bbox, label, conf = cv.detect_common_objects(im)
            #output_image = draw_bbox(im, bbox, label, conf)
            #plt.imshow(output_image)
            #plt.show()
            things.append(label)

    things_list = [obj for objects in things for obj in objects]

    for key,val in yolo_labels_prices.items():
        if key in things_list:
            things_buy[key] = val
            
    return things_buy

#print(things_classifier())