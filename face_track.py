import cv2
import numpy as np
from classifier import classify
import tools
from Conversation.text_to_speech import TextToSpeech
from Conversation.sound_rec_demo import SpeechToText
import take_photo
from datetime import datetime
import os
from Conversation import robot

COUNT = 0
NAME = ''
PRE_NAME = ''
NAME_LIST = []
START = datetime.now()


def face_detection():
    global COUNT
    global NAME
    global START
    global NAME_LIST
    cv2.namedWindow("test")
    cap = cv2.VideoCapture(0)
    success, frame = cap.read()
    classifier = cv2.CascadeClassifier("C:\Python34\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml")
    prelen = ''
    while success:
        success, frame = cap.read()
        size = frame.shape[:2]
        image = np.zeros(size, dtype=np.float16)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.equalizeHist(image, image)
        divisor = 8
        h, w = size
        minSize = (w // divisor, h // divisor)
        faceRects = classifier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)
        # print(len(faceRects))
        if prelen == len(faceRects) and len(faceRects) != 0:
            # print('equal')
            for faceRect in faceRects:
                x, y, w, h = faceRect
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
            if NAME != 'unknown people':
                robot.start_robot(False, name=NAME)  # False means that the robot does not need to wait for silence
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, NAME, (x + 30, y + 30), font, 1, (255, 0, 255), 4)
            COUNT += 1
        else:
            # print('classify')
            if len(faceRects) > 0:
                for faceRect in faceRects:
                    x, y, w, h = faceRect
                    image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                    cv2.imwrite('1.jpg', image)

                    NAME = classify('1.jpg')
                    voice = TextToSpeech()
                    end = datetime.now()
                    # print((end - START).seconds)
                    if (end - START).seconds > 60:
                        NAME_LIST = []
                        START = datetime.now()
                    # print(NAME_LIST)
                    if NAME == 'unknown people':
                        if tools.check_status() == False:
                            voice.play(voice.get_audio_bytes(
                                'Hi'))
                        else:
                            time = 0
                            voice.play(voice.get_audio_bytes(
                                'Hey! I never meet you before. I am a robot! Nice to meet you! I will try to remember you!'))  # using text to speech to ask: hey: I never meet you before. What's your name? Just say your name. I will remember you.

                            NAME_LIST.append(NAME)
                            robot.start_robot(False, name=NAME)


                    else:
                        if NAME not in NAME_LIST:
                            robot.start_robot(False, name=NAME)
                            voice.play(voice.get_audio_bytes('Hi,' + NAME))
                            NAME_LIST.append(NAME)

                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(frame, NAME, (x + 30, y + 30), font, 1, (255, 0, 255), 4)
                    COUNT += 1
                    prelen = len(faceRects)
            else:
                prelen = len(faceRects)

                # print(len(image))

        cv2.imshow("test", frame)
        key = cv2.waitKey(10)
        c = chr(key & 255)
        if c in ['q', 'Q', chr(27)]:
            break
    cv2.destroyWindow("test")


face_detection()
