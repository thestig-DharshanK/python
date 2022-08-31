from bs4 import BeautifulSoup as bs
import requests
import urllib.request as ur
b=[]
n=input("enter link: \n")
r=requests.get(n)
soup=bs(r.content,features="html.parser")
a=soup.find_all("img",attrs={"title":"Lot Image"})
for i in a:
    b.append(i['src'])
for j in b:
    m=j.split("/")
    print(m[-1])
    ur.urlretrieve(j,m[-1])

