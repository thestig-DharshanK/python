import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
r=requests.get("https://en.wikipedia.org/wiki/Toy_Story_3")
ts=bs(r.content,features="html.parser")
n=ts.find("table",attrs={"class":"infobox vevent"})
m=n.find_all("tr")
movie_info={}
def get_content_value(rd):
    if(rd.find('li')):
        return [li.get_text(" ",strip=True).replace("\xa0"," ") for li in rd.find_all('li')]
    else:
        return rd.get_text(" ",strip=True).replace("\xa0"," ")

for index,row in enumerate(m):
    if index==0:
        if(row.find('th')):
          movie_info['title']=row.find('th').get_text(" ",strip=True)
    elif index==1:
        continue
    else:
        if(row.find('th') and row.find('td')):
          ck=row.find('th').get_text()
          cv=get_content_value(row.find('td'))
          movie_info[ck]=cv

print(pd.Series(movie_info))


