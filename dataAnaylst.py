import requests
import pandas as pd
from bs4 import BeautifulSoup
#url = "https://www.bigcommerce.com/articles/ecommerce/best-ecommerce-website-design/"
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r= requests.get(url)
print(r)
soup=BeautifulSoup(r.text,"lxml")
# # print(soup)
# price = soup.find("li",class_="wow fadeIn")
# print(price.text)
# des = soup.find_all("div",class_="short-description-checkshort")
# for item in des:
#     print(item.text)
# for i in price:
#     print(i.text)
# # pricee= soup.find("a",class_="product-title")
# # print(pricee.text)
# mobile = soup.find("div",class_="card__price")
# print(mobile.text)
# mobilee = soup.find("div",class_="line__price")
# print(mobilee.text)
title=soup.find("a",class_="title")
print(title.text)
dis=soup.find("p",class_="description card-text")
print(dis.text)
titlee = soup.find_all("a",class_="title")

for item in titlee:
    print(item.text)
    print("======================================================\n")
desc = soup.find_all("p",class_="description card-text")
for item in desc:
    print(item.text)
    print("======================================================\n")

