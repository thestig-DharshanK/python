from bs4 import BeautifulSoup as bs
import requests
import urllib.request as ur
l=[]
n=input("enter link \n")
r=requests.get(n)
soup=bs(r.content,features="html.parser")
p=soup.find_all("div",attrs={"class":"owl-carousel-hero__item"})
for i in p:
    a=i.find("img")
    l.append(a['data-zoom-image'])
for i in range(len(l)):
    b=l[i].split("/")
    print(b[-1])
    ur.urlretrieve(l[i],b[-1])

