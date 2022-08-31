from bs4 import BeautifulSoup as bs
import requests
import webbrowser
l=[]
r=requests.get(input("enter a link: \n"))
soup=bs(r.content,features="html.parser")
f=soup.find_all("img",attrs={"class":"lazyload"})
print(soup)
for i in f:
    q = i.previous_element
    try:
       l.append(q['data-linkurl'])
    except:
        pass
m=0
for i in l:
    print(i.split("/")[-1])
    webbrowser.open(i)
    if m==len(l)/2:
        break
    m+=1