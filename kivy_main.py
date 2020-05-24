from kivy.app import App
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
import vk_api
from vk_api.longpoll import VkLongPoll, VkChatEventType
import time
import random
import requests
import json
import asyncio
import concurrent.futures
from kivy.network.urlrequest import UrlRequest
import urllib.parse

class Server():

    def send_chmok(req, result):
        send_id = 2000000008
        message_id = result["response"]
        data= urllib.parse.urlencode({'access_token':api_token,
                                                                'v':'5.103',
                                                                'peer_id':send_id,
                                                                'message':'&#128538; &#10084; &#4448; &#4448; &#4448; &#4448; &#4448; &#4448; &#128522;',
                                                                'message_id': message_id,
                                                                'random_id':random.randint(1,27)})
        req = UrlRequest('https://api.vk.com/method/messages.edit', req_body=data)


    def send_first_message(self):
        send_id = 2000000008
        data= urllib.parse.urlencode({'access_token':api_token,
                                                                'v':'5.89',
                                                                'peer_id':send_id,
                                                                'message':'Чмок',
                                                                'random_id':random.randint(1,27)})
        req = UrlRequest('https://api.vk.com/method/messages.send', on_success=Server.send_chmok, req_body=data)

                           


class TestApp(App):

    def on_press_button(self, args):
        Server.send_first_message(self)


    def build(self):
        f = open("token.txt")
        global api_token
        api_token = f.read()
        vk = vk_api.VkApi(token=api_token)
        global long_poll
        long_poll = VkLongPoll(vk)
        global vkapi 
        vkapi = vk.get_api()
        self.button = Button(text='Start server', on_press=self.on_press_button)            
        return self.button

TestApp().run()