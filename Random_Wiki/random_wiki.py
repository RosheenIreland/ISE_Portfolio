#Building a random wikipedia page generator

import requests
from bs4 import BeautifulSoup
import webbrowser 

while True:
     url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
     soup = BeautifulSoup(url.content, "html.parser")
     title = soup.find(class_="firstHeading").text

     print(f"{title} \nDo you want to view it? (y/n)")
     ans = input("").lower()

     if ans == "y":
         url = "https://en.wikipedia.org/wiki/%s" % title
         webbrowser.open(url)
         break

     elif ans == "n":
        print("Try again!")
        continue

     else:
        print("Wrong Choice!")
        break