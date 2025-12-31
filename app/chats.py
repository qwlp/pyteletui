from client import client

tg = client()


def get_chats():
    hist = tg.get_chats()
    hist.wait()
    return hist.update


def get_chat_info(chat_id):
    info = tg.get_chat(chat_id=chat_id)
    info.wait()
    return info.update


print(get_chat_info(894339800))
