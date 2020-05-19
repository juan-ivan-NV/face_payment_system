from keras.models import model_from_json, load_model
import numpy as np
import json
import cv2
import os



with open('models_testings/model_architecture_15_fruits.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('models_testings/model_weights_15_fruits.h5')

def fruits_classifier():
    path = 'fruit'
    prices = {'apple':5,'avocado':7,'banana':2,'blueberry':6,'lemon':7,'onion red':4,'orange':4,'pepper green':7,'potato':3,'tomato':4,'strawberry':3,'raspberry':5,'pineapple':2,'pear':2,'coco':2}
    fruits = []
    fruits_buy = {}

    for filename in os.listdir(path):
        if 'jpg' in filename:

            photo2 = cv2.imread(os.path.join(path,filename))
            img = cv2.resize(photo2,(100,100))
            image = np.expand_dims(img, axis=0)

            predict = model.predict(image)

            output = { 0:'apple',1:'avocado',2:'banana',3:'blueberry',4:'lemon',5:'onion red',6:'orange',7:'pepper green',8:'potato',9:'tomato',10:'strawberry',11:'raspberry',12:'pineapple',13:'pear',14:'coco'}
            #output = { 0:'apple',1:'avocado',2:'banana',3:'blueberry',4:'lemon',5:'onion red',6:'orange',7:'pepper green',8:'potato',9:'tomato'}

            #print(predict)
            fruits.append(output[np.argmax(predict)])

    for key,val in prices.items():
        if key in fruits:
            fruits_buy[key] = val

    return fruits_buy

#print(fruits_classifier())