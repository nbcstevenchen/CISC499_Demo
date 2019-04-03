import json
from watson_developer_cloud import VisualRecognitionV3
from watson_developer_cloud import WatsonApiException
import requests
import os

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='-wbnUuYVQ04RQzINOSJJ2IBlbGZZh-GmbPYaLpIGJeYr')
    #iam_apikey='aZZZ4ow_F7uLCPIyMNbYC31iMXbRIOOyFLMIRo3Fvl0G')



def retrieve():
    classifiers = visual_recognition.list_classifiers(verbose=True).get_result()
    print(json.dumps(classifiers, indent=2))

def check_status():
    classifiers = visual_recognition.list_classifiers(verbose=True).get_result()
    for classifier in classifiers['classifiers']:
        if classifier['status'] != 'ready':
            return False
    return True

def create():
    try:
        with open('Yuhao.zip', 'rb') as yuhao, open(
                'Xinyu.zip', 'rb') as xinyu, open(
            'pig.zip', 'rb') as pig:
            model = visual_recognition.create_classifier(
                'human',
                yuhao_positive_examples=yuhao,
                xinyu_positive_examples=xinyu,
                negative_examples=pig).get_result()
        print(json.dumps(model, indent=2))
    except WatsonApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)

#visual_recognition.delete_classifier('human_1390470737')
# pre: human_208800234
def update(name_list):


    params = (
        ('version', '2018-03-19'),
    )

    classname = 'Lixian'

    files = {
       # classname + '_positive_examples': ('Lixian.zip', open('Lixian.zip', 'rb'))
    }
    for sub in name_list:
        name = sub.replace('.zip', '')
        filename = 'update//' + sub
        #files_key = name + '_positive_examples'
        #files_value = (filename, open(filename, 'rb'))
        files[name + '_positive_examples'] = (filename, open(filename, 'rb'))
    response = requests.post(
        'https://gateway.watsonplatform.net/visual-recognition/api/v3/classifiers/human_859513605', params=params,
        files=files, auth=('apikey', '-wbnUuYVQ04RQzINOSJJ2IBlbGZZh-GmbPYaLpIGJeYr'))


#file_list = os.listdir('update//') # len = 82
#update(file_list[70:]) # 70: (已运行)
#print(check_status())
#create()
#update('yuhao')
#create()
#update('Lixian')
#update(['Brandon Chan'])

#visual_recognition.delete_classifier('human_1286123206')
#visual_recognition.delete_user_data('human_2103343659')
#with open('Yuhao2.zip', 'rb') as yuhao:
#    updated_model = visual_recognition.update_classifier(
#        classifier_id='human_208800234',
#        yuhao_positive_examples=yuhao,).get_result()
#print(json.dumps(updated_model, indent=2))
#with open('Yuhao3.zip', 'rb') as yuhao:
#    updated_model = visual_recognition.update_classifier(
#        classifier_id='human_208800234',
#        yuhao_positive_examples=yuhao).get_result()
#print(json.dumps(updated_model, indent=2))