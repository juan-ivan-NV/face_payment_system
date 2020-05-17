'''import json
from watson_developer_cloud import VisualRecognitionV3
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    iam_apikey='11eqnJwhN7vAIg7KRTS1hCITJ3cLVmuCkpXghCtj2Wmp'
)

with open('opencv_frame_0.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.3',
	classifier_ids='People_1684231973').get_result()
print(json.dumps(classes))'''
dictionary = {"images": [{"classifiers": [{"classifier_id": "People_1684231973", "name": "People", "classes": [{"class": "Juan_Ivan", "score": 0.325}]}], "image": "opencv_frame_0.jpg"}], "images_processed": 1, "custom_classes": 10}
print(dictionary['images'][0]['classifiers'][0]['classes'][0]['class'])
