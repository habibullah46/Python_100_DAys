import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://ticker.finology.in/"
r = requests.get(url)
# print(r.status_code)
soup = BeautifulSoup(r.text,"lxml")
# print(soup)
table = soup.find("table",class_="table table-sm table-hover screenertable")
# print(table.text)
header= table.find_all("th")
title_list = []
for i in header:
    title_list.append(i.text)
# print(title_list)
df=pd.DataFrame(columns=title_list)#colom is build in function which is use to make colom
# print(df)
rows=table.find_all("tr") # don't  use .text find_all
# print(rows)
for i in rows[1:]:
    row = i.find_all("td")
    table=[tr.text for tr in row]
    l = len(df)#len is build in function which is use to check the lenth

    df.loc[l]=table#.loc aik build in function ha jo lables ko tarteeb me lanay kay lia madad krti ha


df.to_excel("C:/Users/Habib Khalqi/Desktop/Python_100_DAys/scrapping/pandas2day.xlsx")
print(df)