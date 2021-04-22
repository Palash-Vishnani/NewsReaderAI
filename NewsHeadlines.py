import requests
import json

def speak(str):
    from win32com.client import Dispatch

    speek=Dispatch("SAPI.SpVoice")

    speek.Speak(str)

if __name__ == '__main__':
    r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=YourAPIkey")
    # print(r.text)
    facts = json.loads(r.text)
    k=1
    for i in facts['articles']:
        print(k,".",i['title'])
        speak(i['title'])
        print(i['description'])
        speak(i['description'])
        print(end="\n")
        k=k+1