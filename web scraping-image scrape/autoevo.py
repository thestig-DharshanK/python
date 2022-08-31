from bs4 import BeautifulSoup as bs
import requests
import urllib.request as ur
l=[]
r=requests.get(input("enter link: \n"))
soup=bs(r.content,features="html.parser")
f=soup.select("div.vslide")
print(f)
m=f[0].find_all("a")
for i in m:
    l.append(i['href'])
for i in l:
    print(i.split("/")[-1])
    ur.urlretrieve(i,i.split("/")[-1])
