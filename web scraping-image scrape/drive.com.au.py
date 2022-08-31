from bs4 import BeautifulSoup as bs
import requests
import webbrowser
l=[]
link="https://www.drive.com.au/reviews/2019-lotus-evora-gt410-sport-review/"
r=requests.get(link)
soup=bs(r.content)
a=soup.find("figure",attrs={"class":"lightbox_drive-lightbox__media-grid__Z9wIx"}).find_parent()
b=a.find_all("figure")
for i in b:
    l.append(i.find("img")['src'])
for j in l:
    j=j.replace("674","1440")
    j=j.replace("1200","2560")
    print(j)
    webbrowser.open(j)

