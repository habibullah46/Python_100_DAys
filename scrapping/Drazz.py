from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.daraz.pk/mobiles-tablets-accessories/?spm=a2a0e.home.cate_8.1.35e34076JEwFzx")
search = driver.find_element('xpath','//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]')
# print(len(search.text))