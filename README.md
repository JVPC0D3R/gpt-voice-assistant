# GPT-VOICE-ASSISTANT

<p align="center">
  <img src="https://github.com/JVPRUGBIER/resources/blob/main/JVP_gpt_voice_chat_gif.gif" width="800" height="400" />
</p>



Welcome to GPT Voice Assistant, this software integrates features from <a href="https://github.com/huwprosser/carter-voice-assistant">carter-voice-assistant</a> and replaces Carter API with <a href="https://openai.com/blog/openai-api">OpenAI API</a>. Currently, the chat.py script provides speech interaction, but I will soon be adding written interaction as well!

## How it Works

This software builds on top of the carter-voice-assistant project and replaces the Carter API with OpenAI API (GPT models). With this integration, our assistant is able to provide more accurate and sophisticated responses to user input.

## Getting Started

To run the GPT Voice Assistant, you will need to provide an OpenAI API key. I suggest creating a python file named keys.py to store the API key variable.

## Installation

To install and run the GPT Voice Assistant, follow these steps:

```git clone https://github.com/JVPRUGBIER/gpt-voice-assistant```

Install the required dependencies:

```pip install -r requirements.txt```

Create a 'keys.py' file in the project directory and add your OpenAI API key:

```API_KEY = "your_api_key"```

Run the assistant:

```python chat.py```
