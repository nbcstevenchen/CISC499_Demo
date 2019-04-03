
import json
from watson_developer_cloud import VisualRecognitionV3
import tools

def classify(filename):
        visual_recognition = VisualRecognitionV3(
            '2018-03-19',
            #iam_apikey='aZZZ4ow_F7uLCPIyMNbYC31iMXbRIOOyFLMIRo3Fvl0G',
            iam_apikey='-wbnUuYVQ04RQzINOSJJ2IBlbGZZh-GmbPYaLpIGJeYr' )

        with open(filename, 'rb') as images_file:
            classes = visual_recognition.classify(
                images_file,
                threshold='0.6',
                owners=["me"]).get_result()
            #print(classes['images'][0]['classifiers'][0]['classes'][0]['score'])
            #if classes['images'][0]['classifiers'][0]['classes'][0]['score'] >= 0.9:
            try:
                return classes['images'][0]['classifiers'][0]['classes'][0]['class']
            except:
                return 'unknown people'

#print(classify('1.png'))