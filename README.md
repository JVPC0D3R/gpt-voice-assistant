# Welcome to gpt-voice-assistant

<p align="justify">
This software builds on top of <a href="https://github.com/huwprosser/carter-voice-assistant">carter-voice-assistant</a>  project and replaces the Carter API with 👾 <a href="https://openai.com/blog/openai-api">OpenAI API</a>. With this integration, the assistant is able to provide more accurate and sophisticated responses to user input.
</p>

<p align="center">
  <img src="https://github.com/JVPC0D3R/resources/blob/main/JVP_gpt_voice_chat_gif.gif" width="100%" />
</p>

<p align="center"><em>gpt-voice-assistant pixel-art by JVPC0D3R</em></p>


## 🛠 how it works

<p align="justify">
GPT-3.5 is the core of the assistant, but this project uses other AI models to extract more data from the user and it's environment:
  
* The first model implemented is 🦻 <a href="https://openai.com/research/whisper">Whisper </a>, which was prebuilt in the original Carter project. Whisper's goal is to listen to the user and transcript it's voice into text.
 
* In order to give vision to the assistant, I used  👁 <a href="https://github.com/ultralytics/ultralytics">Ultralytics YOLOv8</a> model, which can detect, classify and track objects in real time.

* To give the assistant access to the Internet I implemented a 🔍 <a href="https://serpapi.com/">SerpAPI </a> based module.

* In order for the assistant to know if the user wants to perform one action or another, I implemented a 📑 <a href="https://huggingface.co/bert-base-uncased">text classification model</a>, which has to decide if the user input is a chat, a vision query, a google search or a farewell.
  
* Also if the user command needs a google search before calling GPT, the assistant has to get arguments to call the SerpAPI. In order to do that I used another 🔑 <a href="https://pypi.org/project/rake-nltk/"> keyword extraction model</a>.
</p>

## 🛹 getting started

<p align="justify">
To run the gpt Voice Assistant, you will need to provide an OpenAI API and a SerpAPI key. I suggest creating a python file named keys.py to store the API key variable.
</p>

### 📦 installation

To install and run the GPT Voice Assistant, follow these steps:

```
git clone https://github.com/JVPRUGBIER/gpt-voice-assistant
```

Install the required dependencies:

```
pip install -r requirements.txt
```

Create a 'keys.py' file in the project directory and add your OpenAI API key:

```
OPENAI_API_KEY = "your_api_key"
SERP_API_KEY = "your_api_key"
```

### 🏃 run the assistant:

Chat using text with GPT

```
python chat.py -t
```

Chat using text with GPT and let the assistant read the response out loud

```
python chat.py -t -v
```

Have a full speech chat with the GPT voice assistant

```
python chat.py -l -v
```
