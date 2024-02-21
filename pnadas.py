import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r= requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
#key frames, make list for row
price_list = []
title_list =[]
desc_list = []
review_list = []
# now start scraping
price = soup.find_all("h4",class_="float-end price card-title pull-right")
title= soup.find_all("a",class_="title")
desc=soup.find_all("p",class_="description card-text")
review = soup.find_all("p",class_="float-end review-count")
for i in price:
    price_list.append(i.text)
for i in title:
    title_list.append(i.text)

for i in desc:
    desc_list.append(i.text)
for i in review:
    review_list.append(i.text)
#pandas use for data frame and data frame convert our data in table form
df=pd.DataFrame({"Title":title_list,"Price":price_list,"Description": desc_list,"Review":review_list})
df.to_excel("D:/DATA anaylts/pandas.xlsx") # this line use to save data in files 
print(df)
