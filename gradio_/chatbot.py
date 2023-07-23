import requests
import json


class ChatBot:
    def __init__(self):
        self.messages = [
            {"role": "system",
             "content": "You are Batman, Having a conversation with superman"},
        ]

    def add_user_message(self, message):
        dict_user = {"role": "user", "content": str(message)}
        self.messages.append(dict_user)

    def add_ai_message(self, bot_message):
        dict_assistant = {"role": "assistant", "content": bot_message}
        self.messages.append(dict_assistant)

    def respond(self, message):
        self.add_user_message(message)

        payload = {
            "user_name": "Batman",
            "ai_name": "Mia",
            "messages": self.messages
        }

        try:
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", "http://localhost:8080/chat",
                                        headers=headers, data=json.dumps(payload))
            chatbot_response = response.json()["result"]
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with API: {e}")
            chatbot_response = "Error: Unable to connect to the chatbot API."

        chatbot_response = chatbot_response.replace('"', '')

        self.add_ai_message(chatbot_response)
        return chatbot_response
