import vk_api
import random
def get_memes(id):
    Token="f74c1dd7f74c1dd7f74c1dd7bdf7275616ff74cf74c1dd7aa5c816c678957d25f1424af"
    vk_session=vk_api.VkApi(token=Token)
    vk=vk_session.get_api()
    posts=vk.wall.get(owner_id=id, count=10, offset=random.randint(1,500))
    memes=[]
    for post in posts["items"]:
        attachment=post.get("attachments")
        if attachment and attachment[0]["type"]=="photo":
            memes.append(attachment[0]["photo"]["id"])
    return "photo{}_{}".format(id, random.choice(memes))
        

