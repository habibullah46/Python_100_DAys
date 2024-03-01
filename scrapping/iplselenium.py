from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.google.com/")
search = driver.find_element('xpath','//*[@id="APjFqb"]')
search.send_keys("IPL")
search.send_keys(Keys.ENTER)
time.sleep(10)
ipl = search.find_element('xpath','/html/body/div[5]/div/div[12]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div/span/a')

