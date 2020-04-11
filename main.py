import requests
import json
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkChatEventType
import time


class Server:

        def __init__(self, server_name: str="Empty"):

            self.server_name = server_name
            global api_token
            f = open("token.txt")
            api_token = f.read()

            self.vk = vk_api.VkApi(token=api_token)
            self.long_poll = VkLongPoll(self.vk)

            self.vk_api = self.vk.get_api()


        def send_img(self, send_id):
                """
                Отправка сообщения через метод messages.send
                :param send_id: vk id пользователя, который получит сообщение
                :param message: содержимое отправляемого письма
                :return: None
                """
                self.vk_api.messages.send(peer_id=send_id,
                                          attachment = "photo510166866_457241739",
                                          random_id=123456 + random.randint(1,27))
        def send_msg(self, send_id, message):
            """
            Отправка сообщения через метод messages.send
            :param send_id: vk id пользователя, который получит сообщение
            :param message: содержимое отправляемого письма
            :return: None
            """
            self.vk_api.messages.send(peer_id=send_id,
                                    message=message,
                                    random_id=123456 + random.randint(1,27))
        def send_chmok(self, send_id, message_id):
            self.send_msg(send_id, "Чмок")
            message_id=int(message_id)
            message_id = message_id + 1
            messages = [
                " &#128538; &#10084; &#4448; &#4448; &#4448; &#4448; &#4448; &#4448; &#128522; ",
                " &#128526; &#4448; &#10084; &#4448; &#4448; &#4448; &#4448; &#4448; &#128522; ",
                " &#128526; &#4448; &#4448; &#10084; &#4448; &#4448; &#4448; &#4448; &#128522; ",
                " &#128526; &#4448; &#4448; &#4448; &#10084; &#4448; &#4448; &#4448; &#128522; ",
                " &#128526; &#4448; &#4448; &#4448; &#4448; &#10084; &#4448; &#4448; &#128522; ",
                " &#128526; &#4448; &#4448; &#4448; &#4448; &#4448; &#10084; &#4448; &#128522; ",
                " &#128526; &#4448; &#4448; &#4448; &#4448; &#4448; &#4448;  &#10084; &#128522; ",
                " &#128526; &#4448; &#4448; &#4448; &#4448; &#4448; &#4448; &#4448; &#128525; "
            ]

            for i in range(len(messages)):
                time.sleep(1+random.uniform(0.3, 0.9))
                self.vk_api.messages.edit(peer_id=send_id, 
                                            message=messages[i],
                                            message_id=message_id)

            
        def start(self):
            for event in self.long_poll.listen():

                if str(event.type.MESSAGE_NEW) == "VkEventType.MESSAGE_NEW":
                    try:
                        master_key = self.vk_api.messages.getLongPollServer()

                        keygen = master_key["key"]
                        server = master_key["server"]
                        ts = master_key["ts"]
                        response = requests.get("https://{}?act=a_check&key={}&ts={}&wait=25&mode=2&version=3".format(server, keygen, ts)).text
                        response = json.loads(response)
                        #print("res " + response["updates"][0][6]["from"])
                        print(self.vk_api.users.get()[0])
                        print(response["updates"][0][6]["from"])
                        print(int(self.vk_api.users.get()[0]["id"]) == int((response["updates"][0][6]["from"])))
                        if ( (response["updates"][0][5]).lower() == "чмок".lower() ) and ( int(self.vk_api.users.get()[0]["id"]) == int((response["updates"][0][6]["from"])) ):
                            peer_id = response["updates"][0][3]
                            message_id = response["updates"][0][1]

                            self.send_chmok(peer_id, message_id)

                    except:
                        pass


if __name__ ==  "__main__":
    server1 = Server("server1")
    server1.start() 