from bs4 import BeautifulSoup
import requests
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=热门&page_limit=100&page_start=0'
web_data = requests.get(url,headers = headers)
soup = BeautifulSoup(web_data.text,'lxml')
title = soup.select('a.item > p')

datas = json.loads(web_data.text)
results = list(datas.values())[0]
for i in range(0,len(results)):
    print(results[i]['title'],results[i]['rate'])
