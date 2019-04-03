from Conversation1.text_to_speech import TextToSpeech
from Conversation1.chatting import Chat
from Conversation1.sound_rec_demo import SpeechToText
from datetime import datetime
#from connect_sql import DataBase


def start_robot(boolean, name=None):
    #db = DataBase()
    while True:
        flag = True
        while flag:
            try:
                print('Connecting to the voice system')
                speaking = SpeechToText()
                start_speechtotext = datetime.now()
                print(boolean)
                input_sentence = SpeechToText().record_to_file(boolean)
                #print(input_sentence)
                if input_sentence == False:
                    break
                if name != None:
                    #db.sql_command(name, input_sentence)
                    pass
                end_speechtotext = datetime.now()
                #print(input_sentence)
                start_chat = datetime.now()
                try:
                    response = Chat(input_sentence).convert()
                except:
                    continue
                print(input_sentence)
                end_chat = datetime.now()
                voice = TextToSpeech()
                start_voice = datetime.now()
                print('response: ', response)
                voice.play(voice.get_audio_bytes(response))
                end_voice = datetime.now()
                # print('Speech to Text: ', (end_speechtotext - start_speechtotext).seconds)
                # print('Chatting Bot: ', (end_chat - start_chat).seconds)
                # print('Text to Speech: ', (end_voice - start_voice).seconds)
            except:
                voice = TextToSpeech()
                voice.play(voice.get_audio_bytes("Sorry, I don't understand."))
        break

start_robot(True, name=None)

