from bs4 import BeautifulSoup
import requests
import pymysql
import datetime

nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
nowDate = datetime.datetime.now().strftime('%Y-%m-%d')
nowHour = datetime.datetime.now().strftime('%H')
connect = pymysql.Connect(
    host='118.126.90.21',
    port=3306,
    user='BI',
    passwd='Sap123456',
    db='mysql',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
url = 'https://n.cbg.163.com/?serverid=9&order=unit_price+ASC'
web_data = requests.get(url,headers=headers)
soup = BeautifulSoup(web_data.text,'lxml')
title = soup.findAll('td',class_='c_Red')
qty = soup.select('td > p')
a = []
b = []
result = []
for i in title:
    a.append(i.get_text().replace('\n',''))
for q in qty:
    b.append(q.get_text().replace('\n',''))
a1 = [i.replace('元/万文','') for i in a if a.index(i)%2==1]
a2 = [i for i in a if a.index(i)%2==0]
for i,j,q in zip(a1,a2,qty):
    result.append([float(i),float(j),int(q.get_text().replace('万',''))])

for elem in result:
    sql = "insert into mysql.nsh_money values('"+nowTime+"',"+str(elem[0])+","+str(elem[1])+")"
    cursor.execute(sql)
    connect.commit()
print('写入完成',nowTime)
