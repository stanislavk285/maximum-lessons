import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from memes import get_memes
from Valute import get_course
import Weather
import random
def main():
    TOKEN="876a48cc3db89bb94cdfa8240b8ea5e101185e065710535cdba3a42337ff1c0ca10adcecbc1f027aefa98"
    vk_session=vk_api.VkApi(token=TOKEN)
    vk=vk_session.get_api()
    hello="""
    Привет, я БОТ! Я могу следующее:
    -к - Бот кидает курс валют
    -м - Бот кидает мемы
    -п - Бот кидает погоду В Москве
    -монета -Бот подбрасывает монету
    -вер Случайная вероятность
    """
    longpoll=VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type==VkEventType.MESSAGE_NEW and event.to_me:
            msg_text=event.text.lower()
            if msg_text=="-м":
                vk.messages.send(user_id=event.user_id,random_id=get_random_id(),
                                 attachment=get_memes("-147286578"))
            elif msg_text=="-к":
                valutes_id=["R01235","R01239","R01375"]
                valutes=[get_course(id) for id in valutes_id]
                vk.messages.send(user_id=event.user_id,random_id=get_random_id(),
                                 message="\n".join(valutes))
            elif msg_text=="-п":                 
                vk.messages.send(user_id=event.user_id,random_id=get_random_id(),
                                 message=Weather.main("moscow"))
            elif msg_text=="-монета":
                vk.messages.send(user_id=event.user_id,random_id=get_random_id(),
                                 message="Подбрасываю монету...")
                result=random.choice("1""2")
                if result=="1":
                    vk.messages.send(user_id=event.user_id,random_id=get_random_id(),
                                 message="Орёл")
                elif result=="2":
                    vk.messages.send(user_id=event.user_id,random_id=get_random_id(),
                                 message="Решка")
            elif msg_text=="-вер":
                result=random.randint(0,100)
                if result>=75:
                    vk.messages.send(user_id=event.user_id,random_id=get_random_id(),
                                 message=("{}%. Сегодня точно что-то будет.".format(result)))
                elif result>=50 and result<75:
                    vk.messages.send(user_id=event.user_id,random_id=get_random_id(),
                                 message=("{}%. Как повезёт.".format(result)))
                elif result>=0 and result<50:
                    vk.messages.send(user_id=event.user_id,random_id=get_random_id(),
                                 message="{}%. Маловероятно.".format(result))

            else:
                vk.messages.send(user_id=event.user_id,random_id=get_random_id(),
                                 message=hello)

main()
