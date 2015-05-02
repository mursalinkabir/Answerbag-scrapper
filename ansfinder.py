__author__ = 'Mursalin'
import requests
from bs4 import BeautifulSoup
def afinder(link):
    q=requests.get(link)
    qhtml = q.content
    qsoup= BeautifulSoup(qhtml)
    answers = qsoup.find_all("span",{"class":"answerbag_vibrant"}) #fetching the span containing ans
    numofans = len(answers)
    print("The Number of ans are : %s"%(numofans))
    for item in answers:
        print(item.text) #printing the answer text