# -*- coding: utf-8 -*-
import pymysql
from bs4 import BeautifulSoup
import requests
import json
import time
result = []
current_date = time.strftime("%Y%m%d", time.localtime())


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
url = 'http://cn.60wdb.com/items/c/2/15'
web_data = requests.get(url,headers = headers)
soup = BeautifulSoup(web_data.content,'lxml')
title = soup.select('div.iconname')
print(title)

