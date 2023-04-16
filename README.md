# GPT-VOICE-ASSISTANT

<p align="center">
  <img src="https://github.com/JVPRUGBIER/resources/blob/main/JVP_gpt_voice_chat_gif.gif" width="100%" />
</p>



Welcome to GPT Voice Assistant, this software integrates features from <a href="https://github.com/huwprosser/carter-voice-assistant">carter-voice-assistant</a> and replaces Carter API with <a href="https://openai.com/blog/openai-api">OpenAI API</a>. Currently, the chat.py script provides speech and text interaction.

## How it Works

This software builds on top of the carter-voice-assistant project and replaces the Carter API with OpenAI API (GPT models). With this integration, our assistant is able to provide more accurate and sophisticated responses to user input.

This project also gives the assistant "vision" capabilities using a <a href="https://github.com/ultralytics/ultralytics">YOLOv8</a> simple function.

## Getting Started

To run the GPT Voice Assistant, you will need to provide an OpenAI API key. I suggest creating a python file named keys.py to store the API key variable.

## Installation

To install and run the GPT Voice Assistant, follow these steps:

```git clone https://github.com/JVPRUGBIER/gpt-voice-assistant```

Install the required dependencies:

```pip install -r requirements.txt```

Create a 'keys.py' file in the project directory and add your OpenAI API key:

```API_KEY = "your_api_key"```

## Run the assistant:

Chat using text with GPT

```python chat.py -t```

Chat using text with GPT and let the assistant read the response out loud

```python chat.py -t -v```

Have a full speech chat with the GPT voice assistant

```python chat.py -l -v```
