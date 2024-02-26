import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.flipkart.com/search?q=mobile+under+10000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+under+10000%7CMobiles&requestId=a1f60b2a-3410-4f73-92aa-da8fba6dfa1a&as-searchtext=mobile+under+10000&page=1"
r= requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
while True:
    np = soup.find("a",class_="_1LKTO3").get("href")
# print(np)
    cnp="https://www.flipkart.com"+np
    print(cnp)