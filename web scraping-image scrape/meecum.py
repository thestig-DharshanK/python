from bs4 import BeautifulSoup as bs
import requests
import urllib.request as ur
l=[]
r=requests.get(input("enter link: \n"))
soup=bs(r.content,features="html.parser")
f=soup.find_all("div",attrs={"class":"ms-slide"})
for i in f:
    g=i.find("a")
    print(g['href'])
    l.append(g['href'])
for i in l:
    try:
      print(i.split("/")[-1].split("?")[0])
      ur.urlretrieve(i,i.split("/")[-1].split("?")[0])
    except:
        continue