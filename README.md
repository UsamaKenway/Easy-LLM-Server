# LLM-fastapi-n-gradio-server
Use open source models in your app using API, and test it in Realtime using gradio webui. Langchain has been implemented.

![image](https://github.com/UsamaKenway/LLM-fastapi-n-gradio-server/assets/56207634/0455fd83-e445-479d-b7a6-0fbddda0601e)

<img src="https://github.com/UsamaKenway/LLM-fastapi-n-gradio-server/assets/56207634/0455fd83-e445-479d-b7a6-0fbddda0601e"width="50%" >


```sh
$ uvicorn LLMApp.main:app --reload --host 0.0.0.0 --port 8080
```
### Command for message request
I followed the chatgpt api format as most of the people are familiar with this one.
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
You can also Assign names for roleplaying. 

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

