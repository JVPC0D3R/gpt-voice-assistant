from keys import SERP_API_KEY
from modules.Keyword import KeywordDetector
import requests

def google_search(promt):

    KD = KeywordDetector()

    query = KD.concatenate_words(KD.extract_keywords(promt))
    
    params = {
    "engine": "google",
    "q": query,
    "num": 1,
    "api_key": SERP_API_KEY
    }

    print(f'\n\n \033[93m Searching the web [{query}]...\033[0m')

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

    prompt = "What is Valkyria Power Team?"
    print("\n"*8)
    print(f"PROMPT: {prompt}")
    print("Searching the web...")
    print(google_search("What do you know about Valkyria Power Team?"))
    print("\n"*8)