from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

class CommandDetector():

    def __init__ (self, model_path, tokenizer = 'bert-base-uncased'):

        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
        self.classifier = pipeline('text-classification', model=model_path, tokenizer=tokenizer)


    def command_filter(self, prompt):
        # Classify the input prompt
        result = self.classifier(prompt)
        command_id = int(result[0]['label'].split('_')[-1])
        command = {0: 'vision', 1: 'chat'}[command_id]

        return command
    

if __name__ == '__main__':


    mycd = CommandDetector(model_path='../models/cd_CKPT')


    prompt1 = "How many people live in London?"
    prompt2 = "I need you to tell me about powerlifting"
    prompt3 = "Can you see me?"
    prompt4 = "What do you see in this image?"

    print(f'{prompt1} : {mycd.command_filter(prompt1)}')
    print(f'{prompt2} : {mycd.command_filter(prompt2)}')
    print(f'{prompt3} : {mycd.command_filter(prompt3)}')
    print(f'{prompt4} : {mycd.command_filter(prompt4)}')