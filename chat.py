from yaspin import yaspin
from termcolor import colored
from keys import OPENAI_API_KEY

print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

print(colored("Welcome to GPT assistant\n\n", 'magenta'))
print(colored("   YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY   \n"+
" YYYYYYYYYYYYYYYYYJJ?JJYYYYYYYYYYYYYYYYYYYYY \n"+
" YYYYYYYYYYYY?~:.......^!?YYYYYYYYYYYYYYYYYY \n"+
"YYYYYYYYYYYY?: .^7?JJJ?!:  :^::^~7?YYYYYYYYYY\n"+
"YYYYYYYYYYY!  ~JYYYYY?!^. :^~~~^:. :!JYYYYYYY\n"+
"YYYYYYY?~:.  !YYYJ!^. .^7JYYYYYYYJ7: :?YYYYYY\n"+
"YYYYY7: .~^  ?YY! .:!?YYYJ!^:~7JYYYY^ .JYYYYY\n"+
"YYYY~ .!YY7  ?YY~ 75YJ7~::~!~: .:!?YJ. !YYYYY\n"+
"YYY!  ?YYY!  ?YY~ !!:::..~?YYYJ7^. .^  !YYYYY\n"+
"YYY^ :YYYY!  JYY~ :!?JYJ?~:.^!?YYY?!:  !YYYYY\n"+
"YYY!  ?YYY7  7JY~ ?YYYYYYY7 ^~::~7YYY7. ^YYYY\n"+
"YYYY^ .7YYY?!::^: ?YYYYYYY7 !YY!  ?YYY?  7YYY\n"+
"YYYYY~  .~7JYYJ7~::~7JYJ!^. !YY?  7YYYJ. ~YYY\n"+
"YYYYY~ .~: .:!?YYYJ~. ::^7! !YY?  7YYY!  ?YYY\n"+
"YYYYY~ .YYJ7^. .^~^:^!?YYY! !YY?  ?YJ~  !YYYY\n"+
"YYYYY?. ^YYYYY?!^~?YYYJ7^. .7YY7  ^:  ^?YYYYY\n"+
"YYYYYY?: .!JYYYYYYJ?~:  :~?JYYY^ .:^7JYYYYYYY\n"+
"YYYYYYYY7:  .:^^^:. :~7JYYYYY?^ .?YYYYYYYYYYY\n"+
"YYYYYYYYYYJ7!~~~~^. :!7???7~: .~JYYYYYYYYYYYY\n"+
" YYYYYYYYYYYYYYYYYJ7^:.....:~7JYYYYYYYYYYYYYY\n"+
" YYYYYYYYYYYYYYYYYYYYYYJJJYYYYYYYYYYYYYYYYYYY\n"+
"   YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY\n"+
"                                         YYYY\n"+
"     Developed by JVPC0D3R                YYY\n"+
"                                           YY\n"+
"                                            Y\n"+
"\n",'green'))

with yaspin(text="Waking agent...") as spinner:
    import os
    import time
    import requests
    import base64
    import threading
    import scipy.io.wavfile as wav
    from queue import Queue
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    from pygame import mixer
    
    from modules.Whisper import transcribe
    from modules.VoiceActivityDetection import VADDetector
    import openai
    from gtts import gTTS
    from modules.command import CommandDetector

    from modules.Yolo import Eyes
    from modules.google import GoogleManager

    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--voice", action="store_true", help = "Make GPT talk")
    parser.add_argument("-l", "--listen", action="store_true", help = "Make GPT listen")
    parser.add_argument("-t", "--text", action="store_true", help = "Text to GPT")

    cdet = CommandDetector(model_path = "./models/cd_CKPT_IV")
    google = GoogleManager()
    eyes = Eyes()

    openai.api_key = OPENAI_API_KEY
    mixer.init()

class GPTAssistant():

    def __init__(self, startListening=False, startTexting = False, voice=False, local=False):

        
        self.voice = voice
        self.listening = startListening
        self.texting = startTexting
        self.vad = VADDetector(self.onSpeechStart, self.onSpeechEnd)
        self.vad_data = Queue()
        self.context = [{"role": "system", "content": self.read_system_context("jvp.txt")}]
        
        

    
        if startListening and not startTexting:
            self.startListening()

            t = threading.Thread(target=self.transcription_loop)
            t.start()
        
        else:
            
            self.writingMessage()

    def writingMessage(self):

        text = ''

        while True:

            text = input(colored("[👨]: ", "magenta"))

            self.build_context(role ='user', content = text)

            command = cdet.command_filter(text)

            if (command is not 'goodbye'):
                    

                    if command == "vision":

                        vision = eyes.see()

                        self.build_context(role ='system', content = f'The vision module detected {vision}. Respond to the last user promt using this information.')

                    if command == "google":

                        google.get_query(text)

                        if (self.voice):
                            self.play_audio(response = google.notification, exit = exit, response_name = "google_notification.mp3")

                        search = google.search()

                        self.build_context(role ='system', content = f'The google module found {search}. Respond to the last user promt using this information.')
        

                    self.send_to_GPT(messages = self.context)

            else:
                self.send_to_GPT(messages = self.context)

                break




            

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

                    self.build_context(role ='user', content = text)

                    command = cdet.command_filter(text)

                    print(command)

                    if (command is not 'goodbye'):
                    

                        if command == "vision":

                            vision = eyes.see()

                            self.build_context(role ='system', content = f'The vision module detected {vision}. Respond to the last user promt using this information.')

                        if command == "google":
                            
                            google.get_query(text)

                            if (self.voice):
                                self.play_audio(response = google.notification, exit = exit, response_name = "google_notification.mp3")

                            search = google.search()

                            self.build_context(role ='system', content = f'The google module found {search}. Respond to the last user promt using this information.')
        

                        self.send_to_GPT(messages = self.context)

                    else:

                        self.send_to_GPT(messages = self.context, exit = True)

                        break
                    
            
    def read_system_context(self, file):

        context = ''

        with open(file) as f:

            lines = f.readlines()

            for line in lines:

                context += line

        return context

                
    def build_context(self, role, content):

        self.context.append({"role": role, "content": content})


    def send_to_GPT(self, messages, exit = False):

        completion = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = messages)
    
        response = completion['choices'][0]['message']['content']

        print(colored(f'[🤖]:{response}','green'))

        self.build_context(role = 'assistant', content = response)
        if (self.voice):
            self.play_audio(response=response, exit = exit)




    def play_audio(self, response, language= "en", exit = False, response_name = "GPT_response.mp3"):

        speech = gTTS(text = response, lang = language, slow = False)

        speech.save(response_name)

        # play audio
        mixer.music.load(response_name)
        mixer.music.play()

        # wait for audio to finish
        duration = mixer.Sound(response_name).get_length()
        time.sleep(duration + 1)

        # unload and delete audio
        mixer.music.unload()
        os.remove(response_name)
        
        # re-activate microphone
        if (parser.parse_args().listen and not exit):
            self.toggleListening()


if __name__ == '__main__':
    assistant = GPTAssistant(
            startListening = parser.parse_args().listen,
            startTexting =  parser.parse_args().text,
            voice=parser.parse_args().voice)