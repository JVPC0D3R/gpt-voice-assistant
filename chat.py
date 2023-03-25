from yaspin import yaspin
from termcolor import colored

from keys import API_KEY

print()
print()
print(colored("Welcome to GPT assistant", 'magenta'))

with yaspin(text="Waking agent...") as spinner:
    import os
    import time
    import requests
    import base64
    import threading
    import scipy.io.wavfile as wav
    from queue import Queue
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    from pygame import mixer
    #from modules.Whisper import transcribe
    from modules.Whisper import transcribe
    from modules.VoiceActivityDetection import VADDetector
    import openai
    from gtts import gTTS

    openai.api_key = API_KEY
    mixer.init()

class GPTAssistant():

    def __init__(self, key='asdf', startListening=False, voice=False, local=False):

        self.key = key
        self.voice = voice
        self.listening = startListening
        self.vad = VADDetector(self.onSpeechStart, self.onSpeechEnd)
        self.vad_data = Queue()
        self.local = local
        

    
        if startListening:
            self.startListening()

            t = threading.Thread(target=self.transcription_loop)
            t.start()

    def startListening(self):
        print(colored("Listening 👂", 'green'))
        t = threading.Thread(target=self.vad.startListening)
        t.start()

    def toggleListening(self):
        if not self.listening:
            print()
            print(colored("Listening 👂", 'green'))

        while not self.vad_data.empty():
            self.vad_data.get()
        self.listening = not self.listening

    def onSpeechStart(self):
        pass

    def onSpeechEnd(self, data):
        if data.any():
            self.vad_data.put(data)

    def transcription_loop(self):
        while True:
            if not self.vad_data.empty():
                data = self.vad_data.get()

            
                if self.listening:
                    self.toggleListening()
                

                text = transcribe(data)
                
                if len(text) > 4 and text != "Thank you.":
                    print(colored(f'[👨]:{text}', 'magenta'))
                    #print('enviando')
                    self.send_to_GPT(prompt = text)
                    #self.send_to_davinci(prompt = text)
            
    def send_to_davinci(self, prompt="Hi!", engine = "text-davinci-003"):

        completion = openai.Completion.create(engine=engine,prompt=prompt,max_tokens=2048) 

        response = completion.choices[0].text

        print(f'<<<{response}')

        self.play_audio(response=response)

    def send_to_GPT(self, prompt="Hi!", engine = "text-davinci-003"):

        completion = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = [
            {'role': 'user', 'content': f'{prompt}'}
            ],
            temperature = 0  
            )

        response = completion['choices'][0]['message']['content']


        print(colored(f'[🤖]{response}','green'))

        self.play_audio(response=response)




    def play_audio(self, response, language= "en"):

        speech = gTTS(text = response, lang = language, slow = False)

        speech.save("GPT_response.mp3")

        # play audio
        mixer.music.load("GPT_response.mp3")
        mixer.music.play()

        # wait for audio to finish
        duration = mixer.Sound("GPT_response.mp3").get_length()
        time.sleep(duration + 1)

        # unload and delete audio
        mixer.music.unload()
        os.remove("GPT_response.mp3")
        
        time.sleep(1)
        # re-activate microphone
        self.toggleListening()



assistant = GPTAssistant(
        startListening=True, 
        key='asdf',
        voice=True)