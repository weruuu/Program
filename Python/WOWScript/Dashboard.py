import pymysql
from pyecharts.charts import Line
from pyecharts import options as opts
# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='demo1029',
    db='mysql',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()
ItemName = input('输入需要搜索的物品名称：')
xaxis = []
yaxis = []
yaxis1 = []
sql = "select * from mysql.itemprice where itemname = '"+ItemName+"' order by updatetime"
cursor.execute(sql)
for i in cursor.fetchall():
    xaxis.append(i[4])
    yaxis.append(i[1])
    yaxis1.append(i[3])
line = Line()
line.add_xaxis(xaxis)
line.add_yaxis(ItemName, yaxis)
line.add_yaxis(ItemName, yaxis1, yaxis_index =1)
line.extend_axis(yaxis=opts.AxisOpts())
line.render(path='d:/1.html')

cursor.close()
connect.close()