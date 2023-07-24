import requests
import json


class ChatBot:
    def __init__(self):
        """
            Initializes the ChatBot instance with a default system prompt.
        """
        self.messages = [
            {"role": "system",
             "content": "You are Batman, Having a conversation with superman"},
        ]

    def add_user_message(self, message):
        """
        Adds a user message to the conversation.

        Args:
            message (str): The user's message to add to the conversation.
        """
        dict_user = {"role": "user", "content": str(message)}
        self.messages.append(dict_user)

    def add_ai_message(self, bot_message):
        """
        Adds an AI assistant message to the conversation.

        Args:
            bot_message (str): The AI assistant's response to add to the conversation.
        """

        dict_assistant = {"role": "assistant", "content": bot_message}
        self.messages.append(dict_assistant)

    def respond(self, message):
        """
        Sends the user's message to the chatbot API and adds the response to the conversation.

        Args:
            message (str): The user's message to send to the chatbot API.

        Returns:
            str: The chatbot's response to the user's message.
        """
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

    def update_system_messages(self, prompt):
        """
        Updates the system prompt of the chat conversation.

        Args:
            prompt (str): The new system prompt to be updated in messages list.
                          If None or empty, a default friendly prompt is used.
        """
        if prompt is None or prompt == "":
            prompt = "You are a friendly AI Assistant"

        for message in self.messages:
            if message["role"] == "system":
                message["content"] = prompt
