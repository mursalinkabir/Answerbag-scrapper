__author__ = 'Mursalin'
import requests
from ansfinder import *
from bs4 import BeautifulSoup


r = requests.get("http://www.answerbag.com/category/finance_33")
html = r.content
soup= BeautifulSoup(html)
questions= soup.find_all("a",{"class":"title"})

# print(len(questions))
# for item in questions:
#     print(item.text)


for links in questions:
    halflink = links.get("href")
    fulllink= "http://www.answerbag.com"+halflink
    print(fulllink)
    print(afinder(fulllink))
    print(avgresponse())


