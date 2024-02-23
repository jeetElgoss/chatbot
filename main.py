from open_ai_chatbot import ChatBot


# obj_chatBot = ChatBot()
# obj_chatBot.call_chat_with_openai()


def character_count():
    char_count = {}
    data = "hello sonu"
    for x in data:
        if x in char_count:
            char_count[x] += 1
        else:
            char_count[x] = 1
    return char_count


a = character_count()
print(a)
