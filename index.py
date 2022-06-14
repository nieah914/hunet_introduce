from googletts import GTTS
from googletts import Mp3Player

from recode import Recoder
from recode import Translater

import time
import requests

from bot_module import BotModule

hello = '안녕하세요 저는 인공지능 연구소 자비스 선임입니다. 브랜드컴뮤니케이션 팀의 방문을 환영합니다.' \
        '무엇을 도와드릴까요?'

gtts = GTTS()
gtts.set_file_name('hello')
gtts.make_mp3(hello)

file_path = gtts.get_file_path()
del gtts
time.sleep(1)

mp3player = Mp3Player()
mp3player.set_file_path(file_path)
mp3player.play_mp3()
del mp3player
time.sleep(1)




while True:
  recorder = Recoder()
  recorder.recoding()
  recoreded_file_path = recorder.get_file_path()
  del recorder

  trans_module = Translater()
  trans_module.translate()

  time.sleep(1)

  print(trans_module.text)


  if trans_module.text.replace(' ', '') == '':
    pass


  elif '예뻐' in trans_module.text.replace(' ', ''):

    botmodule = BotModule()
    botmodule.press_all_robot()

    say = '이주희님이 휴넷에서 제일 아름다우 십니다.'
    gtts = GTTS()
    gtts.set_file_name('switch2')
    gtts.make_mp3(say)
    file_path = gtts.get_file_path()
    del gtts

    time.sleep(1)
    mp3player = Mp3Player()
    mp3player.set_file_path(file_path)
    mp3player.play_mp3()
    del mp3player

    requests.get('http://192.168.43.53:8090/update')

    say = 'emergency emergency emergency 지지지지직 지지직'
    gtts = GTTS()
    gtts.set_file_name('switch3')
    gtts.make_mp3(say)
    file_path = gtts.get_file_path()
    del gtts

    time.sleep(1)
    mp3player = Mp3Player()
    mp3player.set_file_path(file_path)
    mp3player.play_mp3()
    del mp3player



  elif '잘생' in trans_module.text.replace(' ', ''):
    say = '단연코 조영탁 사장님께서 제일 잘 생기셨습니다.'
    gtts = GTTS()
    gtts.set_file_name('switch4')
    gtts.make_mp3(say)
    file_path = gtts.get_file_path()
    del gtts

    time.sleep(1)
    mp3player = Mp3Player()
    mp3player.set_file_path(file_path)
    mp3player.play_mp3()
    del mp3player


  elif '스위치' in trans_module.text.replace(' ', ''):
    say = '스위치봇 명령을 주셨습니다. 스위치봇을 동작합니다.'
    gtts = GTTS()
    gtts.set_file_name('switch')
    gtts.make_mp3(say)
    file_path = gtts.get_file_path()
    del gtts

    time.sleep(1)
    mp3player = Mp3Player()
    mp3player.set_file_path(file_path)
    mp3player.play_mp3()
    del mp3player








  hello = '더 질문하실건 없으신가요?'

  gtts = GTTS()
  gtts.set_file_name('hello6')
  gtts.make_mp3(hello)

  file_path = gtts.get_file_path()
  del gtts
  time.sleep(1)

  mp3player = Mp3Player()
  mp3player.set_file_path(file_path)
  mp3player.play_mp3()
  del mp3player
  time.sleep(1)
