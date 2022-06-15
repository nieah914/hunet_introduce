import playsound
from gtts import gTTS
import time
from datetime import datetime
import random
import math
import os

class GTTS:
    def __init__(self):

        # self.__random_string = math.floor(random.random()*1000)
        self.__language = 'ko'
        # self.__file_path = f'{self.__random_string}.mp3'
        self.__file_path = os.path.join(os.path.curdir, 'statics', "music_play.mp3")

    def make_mp3(self, _text):
        tts = gTTS(
            text=_text,
            lang=self.__language, slow=False
        )
        tts.save(self.__file_path)

    def set_file_name(self, _name):
        self.__file_path = os.path.join(os.path.curdir, 'statics', f"{_name}.mp3")

    def get_file_path(self):
        return self.__file_path


class Mp3Player:
    def __init__(self):
        self.__file_path = os.path.join(os.path.curdir, 'statics', "music_play.mp3")

    def set_file_path(self, _path):
        self.__file_path = _path

    def play_mp3(self):
        if self.__file_path != '':
            playsound.playsound(self.__file_path)
        else:
            print('error')