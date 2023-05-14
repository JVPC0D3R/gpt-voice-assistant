from rake_nltk import Rake
import re

class KeywordDetector():

    def __init__ (self):

        self.rake = Rake()

    def extract_keywords(self, input_text):
        
        self.rake.extract_keywords_from_text(input_text)
        keywords = self.rake.get_ranked_phrases()
        return keywords
    
    def concatenate_words(self, keywords):
        # Define regular expression to match special characters
        regex = re.compile('[^a-zA-Z0-9\s]+')

        # Concatenate words with a space and remove special characters
        concatenated = ' '.join(keywords)
        concatenated = regex.sub('', concatenated)

        return concatenated
    
if __name__ == "__main__":

    KD = KeywordDetector()
    while True:
        input_text = input()
        keywords = KD.extract_keywords(input_text)
        print(keywords)