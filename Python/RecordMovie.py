import pymysql
from bs4 import BeautifulSoup
import requests
import json
result = []
# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='Eviless',
    passwd='demo1029',
    db='mysql',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=热门&page_limit=100&page_start=0'
web_data = requests.get(url,headers = headers)
soup = BeautifulSoup(web_data.text,'lxml')
title = soup.select('p')
datas = json.loads(web_data.text)
results = list(datas.values())[0]

sql = "truncate table mysql.movie"
cursor.execute(sql)
connect.commit()
for i in range(0,len(results)):
    #result.pop(,)
# 插入数据
    sql = "insert into mysql.movie values('"+results[i]['title']+"','"+results[i]['rate']+"','20171229')"
    cursor.execute(sql)
    connect.commit()



print('写入完成')

# 关闭连接
cursor.close()
connect.close()
