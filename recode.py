import pyaudio
import wave
import time
import speech_recognition as sr
import requests



class Recoder:
    def __init__(self):
        self.__WAVE_OUTPUT_FILENAME = "output.wav"
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
        self.__WAVE_OUTPUT_FILENAME = "output.wav"
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


#
#
# recode_module = Recoder()
# recode_module.recoding()
#
#
# while True:
#     if timeout == 0:
#         timeout = TIMEOUT
#         text = execute()
#
#     if text != '':
#         print(text)
#         timeout = TIMEOUT
#     else:
#         time.sleep(1)
#         timeout = timeout - 1

#
# from switchbot import SwitchBot
# # To get the token, please refer to https://github.com/OpenWonderLabs/SwitchBotAPI#getting-started
# your_switch_bot_token = "5559a03dcc3fd25bf07f3a654ca69f74778864577be534904903b60861ee67a3ae40db3c5103a8c0b1adc308c965e480"
# switchbot = SwitchBot(token=your_switch_bot_token)
# import threading
#
# def move(_device_id):
#     device_target = switchbot.device(id=_device_id)
#     device_target.command('press')
#
#
#
# # To list all devices
# devices = switchbot.devices()
# print(devices)
# while True:
#     for device in devices:
#         print(device)
#     # Bot(id=CD0A18B1C291)
#     # HubMini(id=4CAF08629A21)
#     # Bot(id=5F0B798AEF91)
#     #
#     # If you already know a device id:
#
#         if device.id == 'C5C98F1A6E81':
#             device_target = switchbot.device(id='C5C98F1A6E81')
#             print('33')
#             # if '켜줘' in text.replace(' ',''):
#             #     # device_target.command('turn_on')
#             #     # device_target.command('turn_off')
#             #     pass
#             #     # requests.get('http://192.168.0.126:8090/update')
#             #     pass
#         elif device.id in ('C5970340C7DF'): #,'C2B8D3E3514B'):
#             if '켜줘' in text.replace(' ', ''):
#                 print('22')
#                 device_target = switchbot.device(id=device.id)
#                 device_target.command('turn_on')
#                 time.sleep(3)
#                 requests.get('http://192.168.43.53:8090/update')
#                 text = ''
#
#             pass
#
#
