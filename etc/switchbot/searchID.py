import requests
import json

token = "5559a03dcc3fd25bf07f3a654ca69f74778864577be534904903b60861ee67a3ae40db3c5103a8c0b1adc308c965e480"

url = "https://api.switch-bot.com/v1.0/devices/"
h = {"Authorization": token, "Content-Type": "application/json; charset=utf8"}

reply = json.loads(requests.get(url, headers=h).text)
message = reply['message']

if message == 'success':
    list = reply['body']['infraredRemoteList']
    item = len(list)
    id = None
    print(list)
    name = input("デバイス名は？:")

    for i in range(1, item):
        if name == list[i-1]['deviceName']:
            id = list[i-1]['deviceId']

    if id:
        print(id)
    else:
        print('Error!')
else:
    print('Error:', message)
