import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://ticker.finology.in/"
r = requests.get(url)
# print(r.status_code)
soup = BeautifulSoup(r.text,"lxml")
# print(soup)
# table = soup.find("table ",class_"table table-sm table-hover screenertable")
table = soup.find("table",class_="table table-sm table-hover screenertable")
# print(table.text)

Header = table.find_all("th")
# print(Header)
title_list =[]
for i in Header:
    title_list.append(i.text)
print(title_list)
df=pd.DataFrame(columns=title_list)
# print(df)
rows = table.find_all("td")
print(rows)
for i in rows[1:]:
    row = i.find_all("td")
    table = [tr.text for tr in row]
    l = len(df)  # len is build in function which is use to check the lenth

    df.loc[l] = table
