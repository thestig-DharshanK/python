from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
r=requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
soup=bs(r.content,features="html.parser")
web=soup.select("table.hockey-stats")[0]
c=web.find("thead").find("tr").find_all("th")
l=[]
for i in c:
    l.append(str(i.get_text()).strip())
print(l)
m=[]
r=web.find("tbody").find_all("tr")
f=[]
for i in r:
    j=i.find_all('td')
    m=[str(k.get_text()).strip() for k in j]
    f.append(m)
print(f)
df=pd.DataFrame(f,columns=l)
df=df.loc[~df["Team"].isin(['Did not play'])]
col=list(df.columns.values)
print(col)
print(df[col[0:4]])