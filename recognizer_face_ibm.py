import pandas as pd
import json
#from watson_developer_cloud import VisualRecognitionV3



data = pd.read_csv('buyer_information.csv')
data = data.drop(columns = ['Unnamed: 0'],axis=0)
data = data.set_index('name')


'''def face_classifier():

    visual_recognition = VisualRecognitionV3(
        version='2018-03-19',
        iam_apikey='11eqnJwhN7vAIg7KRTS1hCITJ3cLVmuCkpXghCtj2Wmp'
    )

    with open('face/opencv_face_0.jpg', 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.3',
        classifier_ids='People_1684231973').get_result()'''
    #response = json.dumps(classes)
    response = '{"images": [{"classifiers": [{"classifier_id": "People_1684231973", "name": "People", "classes": [{"class": "Juan_Ivan", "score": 0.892}]}], "image": "1584205893-3623.jpg"}], "images_processed": 1, "custom_classes": 10}'
    name = json.loads(response)['images'][0]['classifiers'][0]['classes'][0]['class']

    return data.loc[name]
