import requests
import time
def savefile(seen):
    try:
        data=requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
        data=data.json()
        if(data["text"] not in seen):
            new_fact=data["text"]
            seen.add(data["text"].strip())
            print(data["text"])
        else:
            return
        with open("TextFile1.txt","a",encoding="utf-8")as file:
            
            file.write(new_fact.strip()+'\n')
    except requests.exceptions.RequestException as e:
        print("API 請求失敗")
        return None
        
def get_data():
    with open("TextFile1.txt","r",encoding="utf-8")as f:
        seen=set()
        for line in f:
            seen.add(line.strip())
    return seen

seen=get_data()
while True:
    time.sleep(3)
    savefile(seen)