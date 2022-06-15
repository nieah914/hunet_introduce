from switchbot import SwitchBot

# To get the token, please refer to https://github.com/OpenWonderLabs/SwitchBotAPI#getting-started
your_switch_bot_token = "5559a03dcc3fd25bf07f3a654ca69f74778864577be534904903b60861ee67a3ae40db3c5103a8c0b1adc308c965e480"
switchbot = SwitchBot(token=your_switch_bot_token)

# To list all devices
devices = switchbot.devices()
for device in devices:
    print(device)
# Bot(id=CD0A18B1C291)
# HubMini(id=4CAF08629A21)
# Bot(id=5F0B798AEF91)
#
# # If you already know a device id:
device = switchbot.device(id='C5970340C7DF')
device.command('turn_on')
print(device.status())
# # Device(id=5F0B798AEF91)
#
# # To query a status of a device

# # {'power': 'off'}
#
# # To command actions,

# # device.command('turn_off')
# device.command('press')
# device.command('set_position', parameter='0,ff,80')
#
# # For some device types like Bot:
# bot = devices[0]
# bot.turn('on')
# bot.turn('off')
# bot.toggle()
# bot.press()