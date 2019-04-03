

from watson_developer_cloud import TextToSpeechV1
from pyaudio import *

class TextToSpeech():
    def __init__(self):
        self.config = TextToSpeechV1(
            #iam_apikey='EXma-hCvh2GhQc8ncOGd0Daum9QH77xeqbiut1i7TLyU',
            iam_apikey='s7VYeKvAUCfTP7Yp7TJm7XHXat_slRrL2W1RjcQfQHzp',
            url='https://stream.watsonplatform.net/text-to-speech/api'
        )

    def get_audio_bytes(self, sentance):
        return self.config.synthesize(
                     sentance,
                    'audio/l16;rate=16000',
                    'en-US_AllisonVoice'
                ).get_result().content

    def play(self, data):
        p = PyAudio()
        stream = p.open(format= paInt16, channels=1,
                    rate=16000, output=True)

    #while data != b'':
        #output = data[:2]
        #data = data[2:]
        #print(output)
        stream.write(data)  # put the data to stream in order to play them

        stream.stop_stream()  # stop the stream
        stream.close()  # close stream
        p.terminate()  # close PyAudio

#if __name__ == '__main__':
 #   play(get_audio_bytes('How are you?'))
