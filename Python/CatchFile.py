
#文本处理方式
from bs4 import BeautifulSoup
import requests

def get_data_str(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Cookie':'bid=GPtewA6eK4I; ll="118175"; viewed="10546125"; gr_user_id=73ab8e3f-b4db-4abc-b586-b8da242463dd; __utmz=223695111.1511957772.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=9C90110DEEC0991047FF82BD6A7C940D|e5e77e40ec798bce67ded2cd83d44631; __utmz=30149280.1512019237.11.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; __utmc=223695111; __utma=30149280.1621551535.1506312224.1514383065.1514455449.16; __utmb=30149280.0.10.1514455449; __utma=223695111.255928850.1511870848.1514383065.1514455449.9; __utmb=223695111.0.10.1514455449; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1514455450%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DJNSJuhxNtMn3HJg6q5rET42uEvVGh62KH3vOZKKUZf-8dPiISyH3IaY0qJ6gGg8T%26wd%3D%26eqid%3Df39d148b00008c28000000045a1ea508%22%5D; _pk_id.100001.4cf6=359fa5ec7b4ef87e.1511870848.9.1514455450.1514383065.; _pk_ses.100001.4cf6=*'
    }
    score = []
    titles = []
    #url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=热门&page_limit=100&page_start=0'
    web_data = requests.get(url,headers=headers)
    Soup = BeautifulSoup(web_data.text,'lxml')
    Title = str(Soup.select('p'))
    start_loc = Title.find(':')
    Title = Title[start_loc:]
    #print(Title)
    result = Title.split('{')
    result.pop(0)
    for a in result:
        titles.append(a[a.find('":"',8)+3:a.find('"',a.find('":"',8)+3)])
        score.append(a[8:11])
    output_list = list(zip(titles,score))
    output_list.sort(key=lambda x:x[1])
    output_list = output_list[::-1]
    for b in output_list:
        print(b)

#json解析方式
from bs4 import BeautifulSoup
import requests
import json
def get_data_json(url):
    result = []
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    #url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=热门&page_limit=100&page_start=0'
    web_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(web_data.text,'lxml')
    title = soup.select('p')
    datas = json.loads(web_data.text)
    results = list(datas.values())[0]
    for i in range(0,len(results)):
        result.pop(results[i]['title'],results[i]['rate'])