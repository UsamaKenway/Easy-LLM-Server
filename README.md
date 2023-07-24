# LLM-fastapi-n-gradio-server
This project allows you to use open-source language models in your applications through an API and test the models in real-time using Gradio's web user interface. It includes an implementation of Langchain.

The project can run in 2 ways.
1. Fastapi only mode, you run it through uvicorn command. "[Jump to example](#launch-through-uvicorn-command)"
2. Gradio + Fastapi which you can run by launching ```server.py```. 
In both the example. You can hit a POST API request with this payload -> "[Jump to example](#payload-example)"

Gradio Screenshot:
![image](https://github.com/UsamaKenway/LLM-fastapi-n-gradio-server/assets/56207634/0455fd83-e445-479d-b7a6-0fbddda0601e)

### Launch-through-uvicorn-command
```sh
$ uvicorn LLMApp.main:app --reload --host 0.0.0.0 --port 8080
```
### Payload-example
The chatbot API follows the format commonly used in ChatGPT, making it familiar to many users. You can send messages in a list, where each message is a dictionary with two key-value pairs: "role" and "content". The roles can be "system", "user", or "assistant". For example:
```sh

{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
}
```
You can also assign names to the roles for a role-playing conversation:

```sh
{
  "user_name": "Batman",
  "ai_name": "Mia",
  "messages": [
    {"role": "system", "content": "Conversation with the Gotham Knight"},
    {"role": "user", "content": "When did you meet superman the last time"},
    {"role": "assistant", "content": "Last month"},
    {"role": "user", "content": "How did it go"}
  ]
}
```
Note:
If the Last message is not from ```"role": "user"```, the system will run "continue" to make the assistant continue typing.

