import requests
def openfile():
    with open("TextFile1.txt","r")as file:
        print(file.read())
with open("TextFile1.txt","r")as f:
    seen=set()
    for line in f:
        seen.add(line.strip()+'\n')



    
with open("TextFile1.txt","r+")as file:
    for i in range(5):
        data=requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
        data=data.json()
        
        if(data["text"] not in seen):
            seen.add(data["text"].strip()+'\n')
            print(data["text"])
        else:
            print("ivan is super smart")
            break
    for line in seen:
        file.write(line.strip()+'\n')
openfile()