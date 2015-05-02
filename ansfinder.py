__author__ = 'Mursalin'
import requests
from bs4 import BeautifulSoup
list =[]
def afinder(link):

    q=requests.get(link)
    qhtml = q.content
    qsoup= BeautifulSoup(qhtml)
    answers = qsoup.find_all("span",{"class":"answerbag_vibrant"}) #fetching the span containing ans
    numofans = len(answers)
    list.append(numofans)
    print("The Number of ans are : %s"%(numofans))
    for item in answers:
        ansindex=answers.index(item)+1
        print("Answer: %s"%(ansindex))
        print(item.text) #printing the answer text

def avgresponse():
    avgans= sum(list)/float(len(list))
    print("average till now is %s"%(avgans))