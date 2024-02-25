import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.longines.com/en-us/watches/suggestions/mens-watches/mens-watches"
r= requests.get(url)
# print(r.status_code)
soup= BeautifulSoup(r.text,"lxml")
print("\n\t\t\t\t\t\t\tMan Watach\n____________________________________________________________________")
#print(soup)
title_list =[]
desp_list = []
quality_list = []
price_list = []
full = soup.find("div",class_="MuiGrid-root MuiGrid-container css-bh902y")
title = full.find_all("p",class_="MuiTypography-root MuiTypography-cta Typography_Container__MrWZd Typography_Transform_uppercase__lv158 css-bfw83a")
description = full.find_all("p",class_="MuiTypography-root MuiTypography-body1 Typography_Container__MrWZd Typography_Color_mediumGrey___tE24 css-1nsau0k")
quality=full.find_all("p",class_="MuiTypography-root MuiTypography-body1 Typography_Container__MrWZd Typography_Color_mediumGrey___tE24 ProductCard_Details__more__UrLia css-1nsau0k")
price = full.find_all("p",class_="MuiTypography-root MuiTypography-label Typography_Container__MrWZd Typography_Color_mediumGrey___tE24 css-1v2xuhd")
# print(quality)
for i in title:
    title_list.append(i.text)
for i in quality:
    quality_list.append(i.text)
for i in description:
    desp_list.append(i.text)
for i in price:
    price_list.append(i.text)
df= pd.DataFrame({"Name":title_list,"Description":desp_list,"Quality":quality_list,"Price":price_list})
df.to_excel("D:/DATA anaylts/Task1forMenwatch.xlsx")
print(df)