#!/usr/bin/python3atom
import vk
import time
import requests
import json

class Controller:

    def __init__(self, bot):
        self.bot = bot
        self.session = vk.Session(access_token=self.bot.config['access_token'])
        self.api = vk.API(self.session)

    def eventListener(self):
        long_poll = self.api.messages.getLongPollServer()
        response = self.__makeRequest__(params = long_poll)
        while True:
            long_poll['ts'] = response['ts']
            if len(response['updates']) > 1 and response['updates'][1][0] == 4:
                message = response['updates'][1][5]
                answer = self.bot.giveAnswer(request = message)
                time.sleep(2)
                try:
                    self.api.messages.send(user_id = response['updates'][1][3], message = answer)
                except:
                    time.sleep(2)
            response = self.__makeRequest__(params = long_poll)

    def __makeRequest__(self, params):
        request = 'https://%(server)s?act=a_check&key=%(key)s&ts=%(ts)s&wait=25&mode=2&version=2' % params
        response = requests.get(request)
        return json.loads(response.text)
