from client import client
import time

tg = client()

tg.call_method("loadChats", {"limit": 20}).wait()
time.sleep(1)


def get_chats():
    hist = tg.get_chats()
    hist.wait()
    return hist.update


def get_chat_info(chat_id):
    info = tg.get_chat(chat_id=chat_id)
    info.wait()
    return info.update


def new_message_handler(update):
    # We want to process only text messages.
    message_content = update["message"]["content"].get("text", {})
    message_text = message_content.get("text", "").lower()
    is_outgoing = update["message"]["is_outgoing"]

    if not is_outgoing and message_text == "ping":
        chat_id = update["message"]["chat_id"]
        print(f"Ping has been received from {chat_id}")
        tg.send_message(
            chat_id=chat_id,
            text="pong",
        )


def get_chats_user(limit):
    chats = tg.get_chats(limit=limit)
    chats.wait()
    return chats.update


def order_chats(limit):
    """
    Orders the chat by using the order property found in info. I actually don't
    know if it is need or not
    """
    chats = get_chats_user(limit)
    random_chats = {}
    for c in chats["chat_ids"]:
        info = get_chat_info(c)
        order = info["positions"][0]["order"]
        random_chats[order] = c
    ordered_chats = dict(sorted(random_chats.items(), reverse=True))
    return list(ordered_chats.values())


def get_lastest_message(chat):
    """
    Alot to do left, it currently only renders the text, will try to implement a class for it
    """
    info = get_chat_info(chat)
    try:
        if info["title"] == "Telegram":
            lm = "[redacted]"
        else:
            lm = info["last_message"]["content"]["text"]["text"]
    except KeyError:
        lm = ""
        # print("Non text not implemented")

    return lm


def get_chats_title(limit):
    chats = order_chats(limit)
    for i, c in enumerate(chats):
        title = get_chat_info(c)["title"]
        lm = get_lastest_message(c)
        print(f"{i + 1}. {title} - {lm}")


# tg.add_message_handler(new_message_handler)
# tg.idle()

# print(get_chat_info(906653657))


get_chats_title(10)
