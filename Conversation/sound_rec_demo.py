'''
The idea of detecting silence is from http://stackoverflow.com/a/6743593/903526
'''
from sys import byteorder
from array import array
from struct import pack
from io import BytesIO
import pyaudio
from watson_developer_cloud import SpeechToTextV1
from datetime import datetime
import json
from datetime import datetime


class SpeechToText():
    def __init__(self):
        self.config = SpeechToTextV1(
           # iam_apikey='6YzHFvvaDU6XJfvovrrYXxNrCfhI8Ee1enkGS-Crjouw',
            iam_apikey='z2T7SNluJPGEGStI2etKxLgBpj56kR_M6mOmYbyCilH4',
            url='https://stream.watsonplatform.net/speech-to-text/api'
        )
        self.threshold = 500
        self.chunk_size = 1024
        self.format = pyaudio.paInt16
        self.rate = 16000

    def is_silent(self, snd_data):
        "Returns 'True' if below the 'silent' threshold"
        return max(snd_data) < self.threshold

    def normalize(self, snd_data):
        "Average the volume out"
        MAXIMUM = 16384
        times = float(MAXIMUM)/max(abs(i) for i in snd_data)

        r = array('h')
        for i in snd_data:
            r.append(int(i*times))
        return r

    def trim(self, snd_data):
        "Trim the blank spots at the start and end"
        def _trim(snd_data):
            snd_started = False
            r = array('h')

            for i in snd_data:
                if not snd_started and abs(i) > self.threshold:
                    snd_started = True
                    r.append(i)

                elif snd_started:
                    r.append(i)
            return r

        # Trim to the left
        snd_data = _trim(snd_data)

        # Trim to the right
        snd_data.reverse()
        snd_data = _trim(snd_data)
        snd_data.reverse()
        return snd_data

    def add_silence(self, snd_data, seconds):
        "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
        r = array('h', [0 for i in range(int(seconds*self.rate))])
        r.extend(snd_data)
        r.extend([0 for i in range(int(seconds*self.rate))])
        return r

    def record(self, stop=True):
        """
        Record a word or words from the microphone and
        return the data as an array of signed shorts.
        Normalizes the audio, trims silence from the
        start and end, and pads with 0.5 seconds of
        blank sound to make sure VLC et al can play
        it without getting chopped off.
        """
        p = pyaudio.PyAudio()
        stream = p.open(format=self.format, channels=1, rate=self.rate,
            input=True, output=True,
            frames_per_buffer=self.chunk_size)

        num_silent = 0
        snd_started = False

        r = array('h')
        start = datetime.now()
        while True:
            # little endian, signed short
            snd_data = array('h', stream.read(self.chunk_size))
            if byteorder == 'big':
                snd_data.byteswap()
            r.extend(snd_data)

            silent = self.is_silent(snd_data)
            if stop == False:
                if silent and not snd_started:
                    end = datetime.now()
                    if (end - start).seconds > 1:
                        return False,False
            if silent and snd_started:
                num_silent += 1
            elif not silent and not snd_started:
                snd_started = True

            if snd_started and num_silent > 30:
                break

        sample_width = p.get_sample_size(self.format)
        stream.stop_stream()
        stream.close()
        p.terminate()

        r = self.normalize(r)
        r = self.trim(r)
        r = self.add_silence(r, 0.5)
        return sample_width, r

    def record_to_file(self, boolean):
        "Records from the microphone and outputs the resulting data to 'path'"
        start_h = datetime.now()
        sample_width, data = self.record(stop=boolean)
        if data == False:
            return False
        data = pack('<' + ('h'*len(data)), *data)
        f = BytesIO(data)
        end_h = datetime.now()
        #print('here: ', end_h - start_h)
        #audio_source = AudioSource(f)
        start = datetime.now()
        speech_recognition_results = self.config .recognize(
            audio=f,
            content_type='audio/l16;rate=16000',
            timestamps=True,
            word_alternatives_threshold=0.9,
        ).get_result()
        #return json.dumps(speech_recognition_results, indent=2)
        end = datetime.now()
        #print(end-start)
        try:
            return speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
        except:
            return json.dumps(speech_recognition_results, indent=2)




    #if __name__ == '__main__':
        #record_to_file()

