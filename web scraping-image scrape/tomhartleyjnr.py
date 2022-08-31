from bs4 import BeautifulSoup as bs
import requests
import urllib.request as ur
l=[]
r=requests.get(input("enter link: \n"))
soup=bs(r.content,features="html.parser")
f=soup.select("ul.gallery")
g=f[0].find_all("li")
for i in g:
    m=i.find("a")['href']
    l.append(m)
for i in l:
    o=i.split("/")[-1]
    print(o)
    ur.urlretrieve(i,o)