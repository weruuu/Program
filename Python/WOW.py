from bs4 import BeautifulSoup
import requests
import json
import time

searchitem = '抑魔金' #input()


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
url = 'https://api.bnade.com/items?name='+searchitem
      # +'&realm='
web_data = requests.get(url,headers = headers)
datas = json.loads(web_data.text)
results = datas[0]['id']

url = 'https://api.bnade.com/cheapest-auctions?itemId='+str(results)
web_data = requests.get(url,headers = headers)
datas = json.loads(web_data.text)
#soup = BeautifulSoup(web_data.text,'lxml')

for i in datas:
    print(i['owner'],i['buyout']/10000,i['quantity'],i['timeLeft'])