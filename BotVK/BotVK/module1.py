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
