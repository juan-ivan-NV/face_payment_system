import recognizer_things_cvlib
import recognizer_fruits_cnn
import recognizer_face_ibm
import send_mail

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2

import cvlib as cv
from cvlib.object_detection import draw_bbox                               


face_cascade=cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(1)

face = 0
fruit = 0
thing = 0

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                                       
    facesquare = face_cascade.detectMultiScale(gray, 1.1, 7)

    bbox, label, conf = cv.detect_common_objects(frame)

    for (x,y,w,h) in facesquare:                                                                                   
        si_color = frame[y-80:y+h+30, x-40:x+w+30]                         

        cv2.rectangle(frame, (x-40,y-80), (x+w+30,y+h+30), (200,0,0), 2)   

    k = cv2.waitKey(1)
    if k%256 == 27:                                                         
        print('Closing...')
        break

    elif k%256 == 32:                                                          
        img_name = 'face/opencv_face_{}.jpg'.format(face)
        cv2.imwrite(img_name,si_color)
        print('Image name: {}'.format(img_name))
        face += 1
                                     
    elif k%256 == 113:                                                        
        img_name = 'fruit/opencv_fruit_{}.jpg'.format(fruit)
        cv2.imwrite(img_name,frame)
        print('Image name: {}'.format(img_name))
        fruit += 1
    
    elif k == ord('s'):                                                        
        img_name = 'thing/opencv_things_{}.jpg'.format(thing)
        cv2.imwrite(img_name,frame)
        print('Image name: {}'.format(img_name))
        thing += 1

    output_image = draw_bbox(frame, bbox, label, conf)                     
    cv2.imshow('frame',frame)
        

cv2.destroyAllWindows()



fruits_class = recognizer_fruits_cnn.fruits_classifier()
things_class = recognizer_things_cvlib.things_classifier()
buyer_identity = recognizer_face_ibm.face_classifier()

products = dict(fruits_class.items() | things_class.items())
total_items = pd.DataFrame(products.items(),columns=['Product', 'Price'])
total_items.loc['Total'] = pd.Series(total_items['Price'].sum(), index = ['Price'])

print(buyer_identity)
print('\n\n')
print(total_items)


products = dict(fruits_class.items() | things_class.items())

total_items = pd.DataFrame(products.items(),columns=['Product', 'Price'])
total_items.loc['Total'] = pd.Series(total_items['Price'].sum(), index = ['Price'])
total_items=total_items.fillna(total_items.index[-2]+1)
total_items['Items'] = total_items.index
total_items = total_items[ ['Items'] + [ col for col in total_items.columns if col != 'Items' ] ]

fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=total_items.values,colLabels=total_items.columns,loc='center')

pp = PdfPages("tickets.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()

print(send_mail.sending_mail('tickets.pdf'))














