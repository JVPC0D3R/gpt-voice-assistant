from keys import SERP_API_KEY
from modules.Keyword import KeywordDetector
import requests

class GoogleManager():

    def __init__ (self):

        self.notification = ""
        self.query = ""

    def get_query(self, prompt):

        KD = KeywordDetector()

        self.query = KD.concatenate_words(KD.extract_keywords(prompt))

        self.notification = f"Searching the web [ {self.query} ]"
        
        print(f'\n\n \033[93m {self.notification}...\033[0m\n\n')

        

    def search(self):

        params = {
        "engine": "google",
        "q": self.query,
        "num": 1,
        "api_key": SERP_API_KEY
        }
        
        

        response = requests.get("https://serpapi.com/search", params=params)

        output = ""

        if response.status_code == 200:
            data = response.json()
            answer_box = data.get("answer_box")
            if answer_box:
                answer = answer_box.get("answer")
                output = f"[Answer: {answer}]\n"
            
            organic_results = data.get("organic_results")
            if organic_results:
                for result in organic_results:
                    title = result.get("title")
                    link = result.get("link")
                    output = output + f"[Title: {title}]\n[Link: {link}]"

        else:
            output = f"Error: {response.status_code}"

        return output

if __name__ == '__main__':

    google = GoogleManager()
    prompt = "What is Valkyria Power Team?"
    print("\n"*8)
    print(f"PROMPT: {prompt}")
    print("Searching the web...")
    print(google.search("What do you know about Valkyria Power Team?"))
    print("\n"*8)