from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.daraz.pk/mobiles-tablets-accessories/?spm=a2a0e.home.cate_8.1.35e34076JEwFzx")
search = driver.find_element('xpath','//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]')
# print(len(search.text))
title_list=[]

title = driver.find_elements('xpath','//*[@id="id-title"]')
# print(len(title))
for i in title:
    title_list.append(i.text)
# print(title_list)
Review_list = []
Review = driver.find_elements('xpath','//*[@id="id-rating"]')
# Reveew = driver.find_elements('xpath','/html/body/div[3]/div/div[4]/div[1]/div/div[1]/div[2]/div[3]/div/a/div[2]/div[2]/div')
for i in Review:
    Review_list.append(i.text)
# print(len(Review_list))
Price_list = []
price = driver.find_elements('xpath','//*[@id="id-price"]')
for i in price:
    Price_list.append(i.text)
print(len(Price_list))
# df=pd.DataFrame({"Title":title_list,"Price":price_list,"Description": desc_list,"Review":review_list})
df = pd.DataFrame({"Title":title_list,"Price":Price_list})
print(df)
# df.to_excel("D:/DATA anaylts/pandas.xlsx") # this line use to save data in files
# print(df)
