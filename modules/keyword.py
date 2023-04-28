from rake_nltk import Rake

class KeywordDetector():

    def __init__ (self):

        self.rake = Rake()

    def extract_keywords(self, input_text):
        
        self.rake.extract_keywords_from_text(input_text)
        keywords = self.rake.get_ranked_phrases()
        return keywords
    
if __name__ == "__main__":

    KD = KeywordDetector()

    input_text = "How many calories does an average pizza have?."
    keywords = KD.extract_keywords(input_text)
    print(keywords)