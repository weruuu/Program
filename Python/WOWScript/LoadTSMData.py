import xlrd
import pymysql

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

data = xlrd.open_workbook('D:\TSMExport\Horde - 巨龙追猎者.xlsx')
table = data.sheets()[0]
r = 1
while r < table.nrows:
    if table.cell_value(r,5).find('PM')>0 and table.cell_value(r,5)[11:13]!='12':
        recordtime = table.cell_value(r,5)[:11]+str(int(table.cell_value(r,5)[11:13])+12)+table.cell_value(r,5)[13:20]
    else:
        recordtime = table.cell_value(r,5)[:20]
    cursor.execute("insert into mysql.itemprice values('" + table.cell_value(r,0) + "',"+table.cell_value(r,1)+","+table.cell_value(r,2)+","+table.cell_value(r,4)+",'"+recordtime+"')")
    r+=1
connect.commit()
print('写入完成')

cursor.close()
connect.close()