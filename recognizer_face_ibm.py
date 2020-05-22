import pandas as pd
import json
from watson_developer_cloud import VisualRecognitionV3



data = pd.read_csv('buyer_information.csv')
data = data.drop(columns = ['Unnamed: 0'],axis=0)
data = data.set_index('name')


def face_classifier():

    visual_recognition = VisualRecognitionV3(
        version='2018-03-19',
        iam_apikey='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    )

    with open('face/opencv_face_0.jpg', 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.3',
        classifier_ids='People_1684231973').get_result()
    response = json.dumps(classes)
    name = json.loads(response)['images'][0]['classifiers'][0]['classes'][0]['class']

    return data.loc[name]