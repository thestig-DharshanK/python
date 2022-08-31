import webbrowser
from bs4 import BeautifulSoup as bs
import requests
import urllib.request as ur
l=[]
n=input("enter link \n")
r=requests.get(n)
soup=bs(r.content,features="html.parser")
p=soup.find_all("div",attrs={"class":"col-sm-2 veo gallery-bottom"})
for i in p:
    j=i.find("a")
    l.append(j['href'])

for i in range(len(l)):
    print(l[i])
    ur.urlretrieve(l[i],"{0}.jpg".format(i))