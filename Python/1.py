# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'
wb_data = requests.get(url)
Soup = BeautifulSoup(wb_data.text,'lxml')
Titles = Soup.select('p')
Score = Soup.select('li > span')
print(Titles)
#print(Score)
li_name = []
for title,score in zip(Titles,Score):
    print(title.get_text())

# for i in li_name :
#     if float(i[1]) >= 7.5:
#         print(i)