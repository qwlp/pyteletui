import threading

def send_message(tg, chat_id, message):
    result = tg.send_message(chat_id, message)
    result.wait()

    message_has_been_sent = threading.Event()

    def update_message_send_succeeded_handler(update):
        print(f"Received updateMessageSendSucceeded: {update}")
        if update["old_message_id"] == result.update["id"]:
            new_message_id = update["message"]["id"]
            print(f"Message has been sent. New message id: {new_message_id}")
            message_has_been_sent.set()

    tg.add_update_handler(
        "updateMessageSendSucceeded", update_message_send_succeeded_handler
    )

    # Wait for the message to be sent
    message_has_been_sent.wait(timeout=60)
    print("Message has been sent.")

    tg.stop()
