import requests
from bs4 import BeautifulSoup
# url="https://www.bigcommerce.com/articles/ecommerce/best-ecommerce-website-design/"
url = "https://www.amazon.com/"
r=requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.text,"lxml") # we can get code of this link
#print(soup)
title=soup.find_all("a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
print(title)
