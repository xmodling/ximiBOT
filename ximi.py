import requests
import time
import vk_api
from bs4 import BeautifulSoup as BS
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import requests
import json
cmdlist = 'Список команд бота: \n —  .report (Связь с администратором). \n —  .ok *хим. реакция* (Решить хим. уравнение). \n — .donate (Поддержать бота).'
donate = 'Привет, чтобы бот дольше жил и становился лучше, ему нужен качественный хостинг, это, конечно же, не бесплатно, поэтому ты можешь поддержать бота здесь: qiwi.com/n/ZABIVNOY2012.'
tokeng="8547ad2af5e4a3fff8d9ae8d33f3bd47cc7218ad65d64e274beddd5821de9eb1fea1210c6cbc4a2a28c50"
vk = vk_api.VkApi(token = tokeng)
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, 201383746)
for event in longpoll.listen():
    try:
        print(event.object.text)
        if event.type == VkBotEventType.MESSAGE_NEW:
            if '.report' in event.object.text.lower():
                if len(event.object.text.lower()) > 15:
                vk.method("messages.send", {"peer_id":event.object['peer_id'], "Сообщение отправлено. ✅":donate, "random_id": random.randint(1, 2132138123)})
            else:
                vk.method("messages.send", {"peer_id":event.object['peer_id'], "Введите более подробное описание. ❌":donate, "random_id": random.randint(1, 2132138123)})
            if event.object.text.lower() == '.help':
                vk.method("messages.send", {"peer_id":event.object['peer_id'], "attachment": "photo-201383746_457239022", "message":cmdlist, "random_id": random.randint(1, 2132138123)})    
            elif event.object.text.lower() == '.donate':
                vk.method("messages.send", {"attachment": "photo-201383746_457239022", "peer_id":event.object['peer_id'], "message":donate, "random_id": random.randint(1, 2132138123)})    
            elif '.ok' in event.object.text.lower():
                msg = event.object.text
                if len(str(msg)) > 4:
                    af = msg[4:]
                    
                    ximis = af.replace('+','%2B')
                    ximid = ximis.replace(' ', '')
                    ximiss = ximid.replace('=', '%3D')
                    ximisss = ximiss.replace('(', '%28')
                    ximissss = ximisss.replace(')', '%29')
                    ximig = requests.get('https://chemequations.com/ru/?s={ur}'.format(
                        ur = ximissss + '&ref=input'
                                        ))
                    ximian = BS(ximig.text, 'html.parser')
                    if ximian.select_one('div.alert-danger') != None:
                        
                        error = ximian.select_one('div.alert.alert-danger.center').text.strip()
                        vk.method("messages.send", {"peer_id":event.object['peer_id'], "message": error, "random_id": 0})
                    else:
                        if ximian.select_one("h1.equation.main-equation.well") != None:
                            a = ximian.select_one("h1.equation.main-equation.well").text.strip()
                        else:
                            a = ''
                        if ximian.select_one('div.panel.panel-default.equation-block') != None:
                            b = ximian.select_one('div.panel.panel-default.equation-block').text.strip()
                        else:
                            b = ''
                        if ximian.select_one('div.panel-body') != None:
                            c = ximian.select_one('div.panel-body').text.strip()
                        else:
                            c = ''
                        vk.method("messages.send", {"attachment": "photo-201383746_457239022", "peer_id":event.object['peer_id'], "message":a+'\n'+'\n' + '------------[Доп. информация]------------' + '\n' + '\n' +c, "random_id": random.randint(1, 2132138123)})

            else:
                print(event.object)
                if event.object['peer_id'] == event.object['from_id']:
                    С
    except Exception as s:
        print(s)
        None
