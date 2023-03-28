import torch
from transformers import BartTokenizer, BartForConditionalGeneration


class Sumarizer:

    def __init__(self, max_length_input, max_length_output ):

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
        self.model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn').to(self.device)
        self.max_length_input = max_length_input
        self.max_length_output = max_length_output

    def sumup(self, input_text):
        
        # tokenize the input text
        inputs = self.tokenizer(input_text, max_length=self.max_length_input, truncation=True, padding='max_length', return_tensors='pt').to(self.device)

        # generate the summary
        summary_ids = self.model.generate(inputs['input_ids'], attention_mask=inputs['attention_mask'], max_length=self.max_length_output, num_beams=4, early_stopping=True)

        # decode the summary
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)



if __name__ == '__main__':

    mySumarizer = Sumarizer(max_length_input=1024,max_length_output=128)

    input = "YOLOv5 is a state-of-the-art object detection algorithm developed by Ultralytics, which stands for 'You Only Look Once version 5'. The YOLOv5 architecture is built on top of the principles of previous YOLO versions, but introduces several key improvements, including a more efficient backbone network, a novel anchor-based mechanism for object detection, and the integration of new data augmentation techniques. YOLOv5 is capable of detecting and classifying objects in real-time with high accuracy and performance, making it an ideal algorithm for a wide range of applications, such as self-driving cars, surveillance systems, and robotics."

    output = mySumarizer.sumup(input)
    print(len(input))
    print(input)
    print('______________________________________________________')
    print(len(output))
    print(output)
    

