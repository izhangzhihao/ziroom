#!/usr/bin/env python
# coding: utf-8
#

from wxbot import *


class MyWXBot(WXBot):
    # def handle_msg_all(self, msg):
    #     if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
    #         self.send_msg_by_uid(u'hi', msg['user']['id'])
    # def schedule(self):
    #     self.send_msg(u'张志豪', u'机器人测试')
    #     time.sleep(30)

    def s_msg(self):
        self.send_msg(u'张志豪', u'机器人测试')


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
