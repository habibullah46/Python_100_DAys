import requests
from bs4 import  BeautifulSoup
import pandas as pd
url = "https://www.iplt20.com/auction/2013"
r = requests.get(url)
# print(r.status_code)
soup = BeautifulSoup(r.text,"lxml")
full_data_list=[]
fulldata=BeautifulSoup.find_all("div",class_="tab-content")
print(fulldata)
for i in fulldata:
    full_data_list.append(i.text)
print(full_data_list)
