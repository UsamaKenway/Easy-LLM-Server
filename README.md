[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1n74YhO73qALQCZorcWJA3tqxWOqselXW)
# Easy-LLM-Server
This project allows you to use open-source language models in your applications through an API and test the models in real-time using Gradio's web user interface. It includes an implementation of Langchain.

### Features:
- 🧠 Any HF model inference support
- 🧠 Any GPTQ model inference support
- 📚  Gradio UI
- 🐳  Docker image through Github Actions
- 🚀 FastAPI | Conversation request in ChatGPT format
- 🚀 FastAPI | Load model through API
- 🚀 FastAPI | Unload model through API
- 💬 Langchain code | support for any conversation memory type
- 💬 Langchain code | Custom Ai Prefix and Human Prefix names
- ✋ Stop Sequence | Automaticlly stops at human prefix to stop rambling.

The project can run in 2 ways.
1. Fastapi only mode, you run it through uvicorn command. "[Jump to example](#launch-through-uvicorn-command)"
2. Gradio + Fastapi which you can run by launching ```server.py```. 
In both the example. You can hit a POST API request with this payload -> "[Jump to example](#payload-example)"

# Launch
### Launch-through-uvicorn-command
```sh
$ uvicorn LLMApp.main:app --reload --host 0.0.0.0 --port 8080
```
### Run server.py
This will load Gradio and Fastapi both
### Docker image
Docker image is being created through GitHub Actions and get the image using the following command. 
It will run uvicorn command automatically as mentioned in CMD here : [Dockerfile](Dockerfile)
```sh
docker pull usamakenway/easy-llm-server:latest
```
Gradio Screenshot:
![image](https://github.com/UsamaKenway/LLM-fastapi-n-gradio-server/assets/56207634/0455fd83-e445-479d-b7a6-0fbddda0601e)

### Quick Installation
Required Windows or Linux with cuda 11.8 and Python 3.10
```shell
pip install -r requirements.txt
```
Note: If you have a different Cuda version, modify the links in ```requirements.txt```
In case you are unable to install auto-gptq, you can find your desired .whl file here [AutoGPTQ Releases](https://github.com/PanQiWei/AutoGPTQ/releases)


### Payload-example
The chatbot API follows the format commonly used in ChatGPT, making it familiar to many users. You can send messages in a list, where each message is a dictionary with two key-value pairs: "role" and "content". The roles can be "system", "user", or "assistant". For example:
  
```sh
{
  "messages": [
    {"role": "system", "content": "Conversation between an Assistant and the user"},
    {"role": "user", "content": "What's your favourite book, Nora?"},
    {"role": "assistant", "content": "I don't have personal preferences, but I'm knowledgeable about many books."},
    {"role": "user", "content": "That's impressive! Can you recommend a classic novel?"}
  ]
}
```
You can also assign names to the roles for a role-playing conversation:

```sh
{
  "user_name": "Victor",
  "ai_name": "Nora",
  "messages": [
    {"role": "system", "content": "Conversation between an Assistant and the user"},
    {"role": "user", "content": "What's your favourite book, Nora?"},
    {"role": "assistant", "content": "I don't have personal preferences, but I'm knowledgeable about many books."},
    {"role": "user", "content": "That's impressive! Can you recommend a classic novel?"}
  ]
}
```
Url example: ```http://localhost:8080/chat```

Note:
If the Last message is not from ```"role": "user"```, the system will run "continue" to make the assistant continue typing.

### Langchain
code here: [LLMApp/langchain/conversation.py](./LLMApp/langchain/conversation.py)
Example of How you can use it in your Backend app here: [gradio_/chatbot.py](./gradio_/chatbot.py) 

### Model Load
#### Load Model through API:
Post request @: ```sh http://localhost:8080/load_model/ ```
payload:
```
{
    "model_name": "meta-llama/Llama-2-7b-chat-hf"
}
```
This will unload the previous model and load the model you specify. If the model is in a private repo. You need to provide hugging face read token through hf cli login
#### Unload Model through API:
```http://localhost:8080/unload_model```

### Understanding model loading code:
<details>
<summary>Click to Expand</summary>
Both HF and quantized models are supported. Class here: [LLMApp/models/load_llm.py](./LLMApp/models/load_llm.py) 

1. Load using HF transformers.AutoModelForCausalLM.from_pretrained:
```python
from LLMApp.models.load_llm import HFModel
HFModel(model_name)
```
2. Load using AutoGPTQ

```python
from LLMApp.models.load_llm import GPTQModel
GPTQModel(model_name)
```
By default the model loads in ```_startup_model()``` through ```start_app_handler```

</details>

### Upcoming features
- Gradio containing options to change character names
- vector DB for longterm chat history
- control over quantization config through loading model API # for now you have to change the code

## Contribution
I welcome contributions to make Easy-LLM-Server better and reliable. You can participate by:

- ✍ Enhancing documentation and code comments
- 💡 Adding new features or improving existing ones
- 🐛 Squashing bugs and improving performance
- 🌐 Translating the project for wider reach

Feel free to create Pull Requests





