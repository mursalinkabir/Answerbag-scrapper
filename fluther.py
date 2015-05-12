__author__ = 'Mursalin'
import re
import requests
from ansfinder import *
from bs4 import BeautifulSoup
def responsefinder(res):
    responsefind=res
    totalans=0
    hasans=0
    for itm in responsefind:
            maintext= itm.text
            numintext=re.findall(r'\d+',maintext) #seratating  int from string
            numtextint=999
            for itm in numintext:
                numtextint= int(itm) #converting string to int
                # print(numtextint)
            # print("Number found in text %s"%(numintext))

            totalans+=1
            # noansfinder=maintext.find(noans)
            if numtextint ==0: # if the response is no answer
                                 print("NO ans found")
                                 print(maintext)
            else: #if the response is yes answer
                hasans+=1  #if ans found increment

    avgansgiven= hasans/totalans
    print("Average answered question %s"%(avgansgiven))


r = requests.get("http://www.fluther.com/")
html = r.content
soup= BeautifulSoup(html)
responsefind= soup.find_all("span",{"class":"smalltext"})
print(responsefinder(responsefind))
h4=soup.find_all("h4")
print(h4)
for item in h4:
    atag = item.find_all("a")
    for tag in atag:
        halflink= tag.get("href")
        fullink="http://www.fluther.com"+halflink   #got the full link of  each question
        print(fullink)
    # print(halflink)


# print(li)


