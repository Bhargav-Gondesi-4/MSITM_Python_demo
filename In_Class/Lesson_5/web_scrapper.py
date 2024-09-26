import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/GitHub")
bs = BeautifulSoup(response.text,"lxml")
with open("output.txt","w") as file:         
    for paragraph in bs.find_all("p"):        
        print(paragraph.text)
        file.write(str(paragraph))
file.close()