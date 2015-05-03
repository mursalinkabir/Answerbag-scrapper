__author__ = 'Mursalin'
import requests
from ansfinder import *
from bs4 import BeautifulSoup


r = requests.get("http://www.answerbag.com/category/environmentalism_10163")
html = r.content
soup= BeautifulSoup(html)
questions= soup.find_all("a",{"class":"title"})
responsefind= soup.find_all("p",{"class":"Note"})

print(responsefinder(responsefind)) # number of answered question out of all

for itm2 in responsefind:
        maintext= itm2.text
        noans= "no answers"
        noansfinder=maintext.find(noans)
        if noansfinder != -1: # if the response if no answer
                             print()
        else: #if the response is yes answer
            for links in questions:
                                    halflink = links.get("href")
                                    fulllink= "http://www.answerbag.com"+halflink
                                    print(fulllink)
                                    print(afinder(fulllink))
                                    print(avgresponse())
                                    print(avgwordcount())
                                    print(priresearch())







