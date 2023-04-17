import math
import os

import requests
import datetime
QMSG_KEY = os.environ["QMSG_KEY"]
TORN_KEY = os.environ["TORN_KEY"]
TORN_ID = '2783662'
webhook = 'https://qmsg.zendee.cn:443/send/' + QMSG_KEY  # Qmsg酱接口
api_url = 'https://api.torn.com/user/' + TORN_ID + '?selections=&key=' + TORN_KEY
bars_url = 'https://api.torn.com/user/' + TORN_ID + '?selections=cooldowns,bars&key=' + TORN_KEY


def analyse_second(second):
    m, s = divmod(second, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


def main_handler():
    i = datetime.datetime.now()
    data = requests.get(api_url).json()
    bars = requests.get(bars_url).json()
    name = data['name'] + '[{}]'.format(data['player_id'])
    status = '你还在城里面潇洒着'
    more_info =''

    if data["status"]["description"] != 'Okay':
        status = '你看起来不在城里潇洒了'
    life = '{}/{}'.format(bars['life']['current'], bars['life']['maximum'])
    energy = '{}/{}'.format(bars['energy']['current'], bars['energy']['maximum'])
    nerve = '{}/{}'.format(bars['nerve']['current'], bars['nerve']['maximum'])

    drug = '药物CD好了'
    if bars['cooldowns']['drug']!=0:
        drug = '药物CD: {}'.format(analyse_second(bars['cooldowns']['drug']))

    booster = '助推器CD好了'
    if bars['cooldowns']['booster'] != 0:
        booster = '饮料CD: {}'.format(analyse_second(bars['cooldowns']['booster']))

    medical = '医药CD好了'
    if bars['cooldowns']['medical'] != 0:
        medical = '医药CD: {}'.format(analyse_second(bars['cooldowns']['medical']))

    if bars['energy']['current'] >= bars['energy']['maximum']:
        more_info += '能量满了哦'
    else:
        achive_max_time = int(bars['energy']['maximum']) - int(bars['energy']['current'])/5
        if achive_max_time>60:
            achive_max_time=str(math.floor(achive_max_time/60))+'小时'
        else:
            achive_max_time=str(math.floor(achive_max_time))+'分钟'
        more_info += '能量预计还有{}补满\n'.format(str(achive_max_time))

    if bars['nerve']['current'] >= bars['nerve']['maximum']:
        more_info += '勇气满了哦'
    else:
        achive_max_time = int(bars['nerve']['maximum']) - int(bars['nerve']['current'])/10
        if achive_max_time>60:
            achive_max_time=str(math.floor(achive_max_time/60))+'小时'
        else:
            achive_max_time=str(math.floor(achive_max_time))+'分钟'
        more_info += '勇气预计还有{}补满\n'.format(str(achive_max_time))

    message = '{}\n{}\n能量: {}\n勇气: {}\n生命: {}\n{}\n{}\n{}\n{}'.format(
        name, status, energy, nerve, life, drug, booster, medical, more_info
    )

    QQPusher(message)


def QQPusher(data):
    data = data.encode('UTF-8')
    massage = {
        'msg': data
    }
    requests.post(webhook, massage)
    print("发送完成")


main_handler()