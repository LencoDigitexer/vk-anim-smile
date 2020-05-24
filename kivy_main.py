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
        print(data)                                                        
        req = UrlRequest('https://api.vk.com/method/messages.send', on_success=Server.send_chmok, req_body=data)


                           


class TestApp(App):

    def make_new_text(self, req, result):
        self.button.text = "test"
        print(result["response"][0])
        self.button.text = str("Привет, " + result["response"][0]["first_name"])

    def press(self, instance, **kwargs):
        send_id = 2000000008
        data= urllib.parse.urlencode({'access_token':api_token, 'v':'5.89'})
        print(data)                                                        
        req = UrlRequest('https://api.vk.com/method/users.get', on_success=self.make_new_text, req_body=data)
    

    def build(self):
        f = open("token.txt")
        global api_token
        api_token = f.read()

        self.button = Button(text='Start server', on_press=self.press)            
        return self.button

TestApp().run()