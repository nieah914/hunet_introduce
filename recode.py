import pyaudio
import wave
import time
import speech_recognition as sr
import requests
import os


class Recoder:
    def __init__(self):
        self.__WAVE_OUTPUT_FILENAME = os.path.join(os.path.curdir, 'statics', "output.wav")
        self.__TIMEOUT = 10
        self.__RESPEAKER_RATE = 16000
        self.__RESPEAKER_CHANNELS = 1  # change base on firmwares, 1_channel_firmware.bin as 1 or 6_channels_firmware.bin as 6
        self.__RESPEAKER_WIDTH = 2
        # run getDeviceInfo.py to get index
        self.__RESPEAKER_INDEX = 1  # refer to input device id
        self.__CHUNK = 1024
        self.__RECORD_SECONDS = 5


    def get_file_path(self):
        return self.__WAVE_OUTPUT_FILENAME

    def recoding(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            rate=self.__RESPEAKER_RATE,
            format=self.p.get_format_from_width(self.__RESPEAKER_WIDTH),
            channels=self.__RESPEAKER_CHANNELS,
            input=True,
            input_device_index=self.__RESPEAKER_INDEX, )
        print("* recording")
        frames = []
        for i in range(0, int(self.__RESPEAKER_RATE / self.__CHUNK * self.__RECORD_SECONDS)):
            data = self.stream.read(self.__CHUNK)
            frames.append(data)
        print("* done recording")

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(self.__WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.__RESPEAKER_CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.p.get_format_from_width(self.__RESPEAKER_WIDTH)))
        wf.setframerate(self.__RESPEAKER_RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

class Translater:
    def __init__(self):
        self.__WAVE_OUTPUT_FILENAME = os.path.join(os.path.curdir, 'statics', "output.wav")
        self.r = sr.Recognizer()
        self.text = ''

    def translate(self):
        harvard = sr.AudioFile(self.__WAVE_OUTPUT_FILENAME)
        with harvard as source:
            audio = self.r.record(source, offset=0, duration=60)
            try:
                self.text = self.r.recognize_google(audio, language='ko-KR')
                # dic.insert(i,outputLine)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def get_result_text(self):
        return self.text
