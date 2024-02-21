import requests
from bs4 import BeautifulSoup
url = "https://www.alibabagroup.com/en-US/"
r = requests.get(url)
print(r.status_code)