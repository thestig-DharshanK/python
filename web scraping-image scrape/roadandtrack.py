from bs4 import BeautifulSoup as bs
import requests
import urllib.request as ur
l=[]
r=requests.get(input("enter link: \n"))
soup=bs(r.content,features="html.parser")
f=soup.find_all("picture")
print(soup)
for i in f:
    a=i.find("source")
    try:
        m=a['srcset']
        l.append(m.split("?")[0])
    except:
        m=a['data-srcset']
        l.append(m.split("?")[0])
print(l)
for i in l:
    ur.urlretrieve(i,i.split("/")[-1])