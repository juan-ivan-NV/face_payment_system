import cv2
import numpy as np
#import cvlib as cv
#from cvlib.object_detection import draw_bbox                       # 80 objetos


face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

i = 0

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                  # color changed             
    facesquare = face_cascade.detectMultiScale(gray, 1.1, 7)

    #bbox, label, conf = cv.detect_common_objects(frame)

    for (x,y,w,h) in facesquare:                                    # squares where the face should be
        #si_gray = gray[y:y+h, x:x+w]                                # square interest region color gray
        si_color = frame[y-80:y+h+30, x-40:x+w+30]                                # square interest region color

        cv2.rectangle(frame, (x-40,y-80), (x+w+30,y+h+30), (200,0,0), 2)              # video, begin cords, end cords, color, line thickness

    k = cv2.waitKey(1)
    if k%256 == 27:                                                 # esc = close
        print('Closing...')
        break

    elif k%256 == 32:                                               # space = photo
        img_name = 'opencv_frame_{}.jpg'.format(i)
        cv2.imwrite(img_name,si_color)
        print('Image name: {}'.format(img_name))
        i += 1


    #output_image = draw_bbox(frame, bbox, label, conf)
    cv2.imshow('frame',frame)
        

cap.realise()
cv2.destroyAllWindows()



