#consider a module to be the same as a code library.
#A file containing a set of functions you want ot include in your application
#example of python modeules
#maths
#Random
#os
#time

import math
sin = math.sin(30)
print(sin)
cos=math.cos(90)
print(cos)
#there are so manay libraries or modules you can use according to your requirement
# print("===============================")
# import random
#
# randomm=random.randint(1,33)
# #randint() is a built in function which is use to get different number btw any numbers
# print(randomm)
# print("========================================")
# a=[1,2,3,4,5,6,7]
# random.shuffle(a)
# #shuffle() is a built in function which is use to shuffle any number or any input data
# print(a)
# name=["habibullah","Azkar ul hassan","Hammad aziz"]
# random.shuffle(name)
# print(name)
# print("===========================================")
# import time
# current=time.time()
# print(current)
#
# currentime= time.ctime()
# print(currentime)
#
# print("hellow")
# sleep= time.sleep(3)
# print("world")
#
# print("========================")
# import os
# d=os.getcwd() #get current working directry
# #getcwd bhi aik function ha joki haman ya batata ha ki ham is work kis system par kam kar rha ha hamari current file location haman bata dayga
# print(d)
import requests
from bs4 import BeautifulSoup
import pandas
soup = BeautifulSoup()
url = "https://www.shopify.com/pricing"


