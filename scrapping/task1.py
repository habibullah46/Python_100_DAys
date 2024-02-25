import requests
import pandas as pd
from bs4 import  BeautifulSoup
url = "https://www.longines.com/en-us/watches/suggestions/mens-watches/mens-watches"
# url = "https://www.longines.com//en-us/watches/suggestions/mens-watches/mens-watches"
r= requests.get(url)
# print(r.status_code)
soup = BeautifulSoup(r.text,"lxml")
# print(soup.text)
name=soup.find_all("h1",class_="MuiTypography-root MuiTypography-titleXXLarge Typography_Container__MrWZd Typography_Color_black__e8rYv css-egnubm")
# print(name)
# title = []
# for i in name:
#     title=name.find("span")
# print(title)
print("=============================")
title_list = []
dec_list = []
quality_list = []
price_list =[]
title = soup.find("p",class_="MuiTypography-root MuiTypography-cta Typography_Container__MrWZd Typography_Transform_uppercase__lv158 css-bfw83a")
descripton = soup.find("p",class_="MuiTypography-root MuiTypography-body1 Typography_Container__MrWZd Typography_Color_mediumGrey___tE24 css-1nsau0k")
quality = soup.find("p",class_="MuiTypography-root MuiTypography-body1 Typography_Container__MrWZd Typography_Color_mediumGrey___tE24 ProductCard_Details__more__UrLia css-1nsau0k")
price = soup.find("p",class_="MuiTypography-root MuiTypography-label Typography_Container__MrWZd Typography_Color_mediumGrey___tE24 css-1v2xuhd")
full=soup.find_all("div",class_="Grid_Wrapper__qAxOK ProductList_ContentWrapper__ixGnQ")
fulllist=[]
for i in title:
    title_list.append(i.text)
for i in descripton:
    dec_list.append(i.text)
for i in quality:
    quality_list.append(i.text)
for i in price:
    price_list.append(i.text)
for i in full:
    fulllist.append(i.text)
# print(fulllist)
df=pd.DataFrame(columns=fulllist)

print(df)
print("===============================")
