import cv2
import cvlib as cv
import matplotlib.pyplot as plt
from cvlib.object_detection import draw_bbox
import os

things = []
path = 'thing'

for filename in os.listdir(path):
    if 'jpg' in filename:
        #im = cv2.imread('opencv_fruit_0.jpg')
        im = cv2.imread(os.path.join(path,filename))
        bbox, label, conf = cv.detect_common_objects(im)
        #output_image = draw_bbox(im, bbox, label, conf)
        #plt.imshow(output_image)
        #plt.show()
        things.append(label)

things_list = [obj for objects in things for obj in objects]
print(things_list)