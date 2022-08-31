from bs4 import BeautifulSoup as bs
import requests
import urllib.request as ur
l=[]
r=requests.get(input("enter a link: \n"))
soup=bs(r.content,features="html.parser")
f=soup.find_all("img",attrs={"class":"sp-image"})
for  i in f:
    l.append(i['data-src'])
    print(i['data-src'])
for i in l:
    m=i.split("/")[-1].split("?")[0]
    print(m)
    ur.urlretrieve(i,m)