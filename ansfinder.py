__author__ = 'Mursalin'
import requests
from bs4 import BeautifulSoup
list =[]
avgword =[]
def afinder(link):

    q=requests.get(link)
    qhtml = q.content
    qsoup= BeautifulSoup(qhtml)
    answers = qsoup.find_all("span",{"class":"answerbag_vibrant"}) #fetching the span containing ans
    numofans = len(answers)
    list.append(numofans)
    print("The Number of ans are : %s"%(numofans))
    tmpavglist = []
    for item in answers:
        ansindex=answers.index(item)+1
        print("Answer: %s"%(ansindex))
        print(item.text) #printing the answer text
        tmptext= item.text
        tmpsplt= tmptext.split(" ")
        tmpavglist.append(len(tmpsplt)) #adding the len of words of current anss
    print("Printing tmpavglist %s"%(tmpavglist))
    finavg=sum(tmpavglist)/numofans #countung temp avg word count for this question
    avgword.append(finavg) #adding current avg to main avg list

def avgresponse():
    avgans= sum(list)/float(len(list))
    print("average ans till now is %s"%(avgans))

def avgwordcount():
    avgwordnow= sum(avgword)/float(len(avgword))
    print("List of avgword count %s"%(avgword))

    print("average words till now is %s"%(avgwordnow))