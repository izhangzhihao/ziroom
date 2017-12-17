#!/usr/bin/env python
# coding: utf-8
#
import sys
import requests
import time
from threading import Thread
from wxbot import *


class MyWXBot(WXBot):
    def test_msg(self):
        self.send_msg(u'张志豪', u'快去看看房子！！！！！！！！！！')


def check():
    while True:
        get_info('http://www.ziroom.com/detail/info?id=30233&house_id=2671')
        get_info('http://www.ziroom.com/detail/info?id=60321180&house_id=60052474')
        get_info('http://www.ziroom.com/detail/info?id=325401&house_id=51337')
        time.sleep(30)

def get_info(url):
    res = requests.get(
        url, headers={'User-Agent': 'Ziroom'})
    if res.json()['data']['status'] == 'tzpzz':
        print('配置中...')
    else:
        print('快去看看！！！')
        bot.test_msg()


bot = MyWXBot()


def main():
    # bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    thread = Thread(target=main, args=())
    thread.daemon = True
    thread.start()
    check()