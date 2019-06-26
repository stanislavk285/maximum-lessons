import vk_api
import time
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
from Valute import *
token="f74c1dd7f74c1dd7f74c1dd7bdf7275616ff74cf74c1dd7aa5c816c678957d25f1424af"
vk=vk_api.VkApi(token=token)
vk._auth_token()
posts=vk.method("wall.get",{"owner_id":"-113766658","offset":"1","count":"99"})
print(posts)

def keyboard():
    keyboard= VkKeyboard(one_time=False)
    keyboard.add_button("Белый цвет", color= VkKeyboardColor.DEFAULT)
    keyboard.add_button("Зеленый цвет", color= VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Красный цвет", color= VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Синий цвет", color= VkKeyboardColor.PRIMARY)
    return keyboard.get_keyboard()
print(keyboard())

while True:
    messages=vk.method("messages.getConversations",{"count" :20, "filter":"unanswered"})
    if messages['count']>=1:
        id=messages['items'][0]['last_message']['from_id']
        random_id=random.randint(1,99999999999)
        message_text=messages['items'][0]['last_message']['text']
        if message_text.lower()=="Курс":
            vk.method("messages.send",{"peer_id":id,"random_id":random_id,"message":get_course("R01235")})
        elif  message_text.lower()=="начать":
            vk.method("messages.send",{"peer_id":id,"random_id":random_id,"message":"Выбор команды","keyboard":keyboard()})
        else:
            vk.method("messages.send",{"peer_id":id,"random_id":random_id,"message":"неизвестная команда"})
        
        


