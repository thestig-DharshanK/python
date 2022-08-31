import webbrowser
from bs4 import BeautifulSoup as bs
import requests
import urllib.request as ur
l=[]
r=requests.get(input('enter a link'))
soup=bs(r.content,features="html.parser")
p=soup.find_all("div",attrs={"class":"text-center m-0"})
for i in p:
    a=i.find("img")
    l.append(a['data-src'])
for i in range(len(l)):
    webbrowser.open(l[i])