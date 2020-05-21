from kivy.app import App
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
import vk_api
from vk_api.longpoll import VkLongPoll, VkChatEventType
import time
import random

class Server():


    def send_msg(self, send_id):
            """
            Отправка сообщения через метод messages.send
            :param send_id: vk id пользователя, который получит сообщение
            :param message: содержимое отправляемого письма
            :return: None
            """
            vkapi.messages.send(peer_id=send_id,
                                    message="message",
                                    random_id=123456 + random.randint(1,27))

    def start(self):
        vkapi.messages.send(peer_id=359634176,
                                    message="message",
                                    random_id=123456 + random.randint(1,27))


class TestApp(App):

    def on_press_button(self, args):
        Server.start(self)


    def build(self):
        f = open("token.txt")
        api_token = f.read()
        vk = vk_api.VkApi(token=api_token)
        global long_poll
        long_poll = VkLongPoll(vk)
        global vkapi 
        vkapi = vk.get_api()
        self.button = Button(text='Start server', on_press=self.on_press_button)            
        return self.button


TestApp().run()