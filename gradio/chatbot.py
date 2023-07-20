class ChatBot:
    def __init__(self):
        self.messages = [
            {"role": "system",
             "content": "You are Batman, Having a conversation with superman"},
        ]

    def add_user_message(self, message):
        dict_user = {"role": "user", "content": str(message)}
        self.messages.append(dict_user)
        return self.messages

    def add_ai_message(self, bot_message):
        dict_assistant = {"role": "assistant", "content": bot_message}
        self.messages.append(dict_assistant)
        return self.messages

    def respond(self, message):
        messages = self.add_user_message(message)

        # Chat code (assuming `llm` is defined somewhere)
        chat = Conversation(llm, messages=messages, ai_prefix="Batman",
                            human_prefix="Superman")
        bot_res = chat.predict_response()
        bot_res = bot_res.replace('"', '')

        messages = self.add_ai_message(bot_res)
        return bot_res