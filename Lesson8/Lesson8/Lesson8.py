import telebot
token = "842545911:AAF_atEZH9vMO95FhlTeBJQo15ns1ksLsAI"
bot= telebot.TeleBot(token)
def get_last_message():
    return bot.get_updates()[-1]
def get_text(last_message):
    return last_message.message.text
def get_id(last_message):
    return last_message.message.chat.id
update_id=0
while True:
    last_message=get_last_message()
    text_message=get_text(last_message).lower()
    id=get_id(last_message)
    new_update_id=last_message.update_id
    if new_update_id !=update_id:
        if text_message in["привет","здарова","хай"]:
            response="Привет! "+ last_message.message.chat.first_name +"."
            bot.send_message(chat_id=id, text=response)
        if text_message in["пока","до свидания","увидимся"]:
            response="До встречи! "+ last_message.message.chat.first_name +"."
            bot.send_message(chat_id=id, text=response)
    update_id=new_update_id
       




