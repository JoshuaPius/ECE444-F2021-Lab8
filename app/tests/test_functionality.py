import time
import requests

API_PATH = "http://fake-real-news-env.eba-dpwqnn8g.us-east-2.elasticbeanstalk.com/tweet/"
HEADER = {
        'Content-Type': "application/json"
    }

def get_Verdict(text):
    endPont = API_PATH + text
    response = requests.request("GET", endPont, headers=HEADER)
    return response.json()
        
def main():
    print(get_Verdict("BOOK"))
    
if __name__ == "__main__":
    main()