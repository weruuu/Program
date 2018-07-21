from bs4 import BeautifulSoup
import requests
import pymysql
import datetime
import xlwt

nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
#
# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
# url = 'https://n.cbg.163.com/?serverid=9&order=unit_price+ASC'
# web_data = requests.get(url,headers=headers)
# soup = BeautifulSoup(web_data.text,'lxml')
# title = soup.findAll('td',class_='c_Red')
# qty = soup.select('td > p')
# a = []
# b = []
# result = []
# for i in title:
#     a.append(i.get_text().replace('\n',''))
# for q in qty:
#     b.append(q.get_text().replace('\n',''))
# a1 = [i.replace('元/万文','') for i in a if a.index(i)%2==1]
# a2 = [i for i in a if a.index(i)%2==0]
# for i,j,q in zip(a1,a2,qty):
#     result.append([float(i),float(j),int(q.get_text().replace('万',''))])
# print(result)

# sql = "delete from mysql.v_nsh where FROM_UNIXTIME(UNIX_TIMESTAMP(log_date),'%H')='"+nowHour+"'"
# cursor.execute(sql)
# connect.commit()

# for elem in result:
#     print(nowTime,elem[0],elem[1])
#     sql = "insert into mysql.nsh_money values('"+nowTime+"',"+str(elem[0])+","+str(elem[1])+")"
#     cursor.execute(sql)
#     connect.commit()
# print('写入完成')

sql = "select * from mysql.v_nsh"
cursor.execute(sql)
excel_set = []
for i in cursor:
    excel_set.append([i[0],i[1],str(i[2])])

# 关闭连接
cursor.close()
connect.close()

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('test')
for x in range(len(excel_set)):
    for y in range(len(excel_set[0])):
        worksheet.write(x, y, label=excel_set[x][y])
workbook.save('%s.xls' % ('nsh'))