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

def get_latency(text):
    endPont = API_PATH + text
    start = time.time()
    for ctr in range (100):
        response = requests.request("GET", endPont, headers=HEADER)
    time_lapsed = time.time() - start
    return time_lapsed/100
        
def main():
    print("Running individual test cases")
    test_cases = [
        {"text":"Brack Obama is a good president",
        "expected":"REAL"},
        {"text":"Tiger Woods says his days of being a full-time golfer are over: 'Never full time, ever again'",
        "expected":"REAL"},
        {"text":"Holy Bible was written and published by donald trump in the last financial quarter",
        "expected":"FAKE"},
        {"text":"The Toike Oike is the official (serious) newspaper of the Republic of Congo for the last 800 years",
        "expected":"FAKE"}]
    for ctr in range(len(test_cases)):
        print("Test Case #" + str(ctr+1))
        print ("Phrase: " + test_cases[ctr]["text"])
        print("Expected: " + test_cases[ctr]["expected"]+ " Actual: ", get_Verdict(test_cases[ctr]["text"]))
        print("Average Latency Over 100 Calls: " + str (get_latency(test_cases[ctr]["text"])) + " seconds")
    
if __name__ == "__main__":
    main()