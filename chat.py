from assistant.assistant import GPTAssistant
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-v", "--voice", action="store_true", help = "Make GPT talk")
parser.add_argument("-l", "--listen", action="store_true", help = "Make GPT listen")
parser.add_argument("-t", "--text", action="store_true", help = "Text to GPT")

if __name__ == '__main__':
    assistant = GPTAssistant(
            startListening = parser.parse_args().listen,
            startTexting =  parser.parse_args().text,
            voice=parser.parse_args().voice)