from switchbot import SwitchBot
# To get the token, please refer to https://github.com/OpenWonderLabs/SwitchBotAPI#getting-started

import threading
import time
class BotModule:

    def __init__(self):
        self.__your_switch_bot_token = "5559a03dcc3fd25bf07f3a654ca69f74778864577be534904903b60861ee67a3ae40db3c5103a8c0b1adc308c965e480"
        self.__switchbot = SwitchBot(token=self.__your_switch_bot_token)
        self.__bot_list = []
        self.get_all_switch_bot()

    def get_all_switch_bot(self):
        for bot in self.__switchbot.devices():
            if bot.id != 'D432F39C0276': # hub mini
                self.__bot_list.append(bot)

    def press_all_robot(self):
        for bot in self.__bot_list:
            self.press_robot(bot.id)
            time.sleep(3)

    def press_robot(self,_id):
        device_target = self.__switchbot.device(id=_id)
        device_target.command('press')

# To list all devices
#
# print(devices)
#
# for device in devices:
#     print(device)
# # Bot(id=CD0A18B1C291)
# # HubMini(id=4CAF08629A21)
# # Bot(id=5F0B798AEF91)
# #
# # If you already know a device id:
#
#     device_target = switchbot.device(id=device.id)
#     if device.id != 'D432F39C0276': # hub mini
#         device_target.command('turn_on')
#
#
# #
# #     if device.id == 'C5C98F1A6E81':
# #         device_target = switchbot.device(id='C5C98F1A6E81')
# #         print('33')
# #         # if '켜줘' in text.replace(' ',''):
# #         #     # device_target.command('turn_on')
# #         #     # device_target.command('turn_off')
# #         #     pass
# #         #     # requests.get('http://192.168.0.126:8090/update')
# #         #     pass
# #     elif device.id in ('C5970340C7DF'): #,'C2B8D3E3514B'):
# #         if '켜줘' in text.replace(' ', ''):
# #             print('22')
# #             device_target = switchbot.device(id=device.id)
# #             device_target.command('turn_on')
# #             # time.sleep(3)
# #             # requests.get('http://192.168.43.53:8090/update')
# #             # text = ''
# #
# #         pass
# #
# #
