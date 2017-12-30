import pymysql

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='Eviless',
    passwd='',
    db='mysql',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

# 查询数据
sql = "SELECT * FROM testtb "
cursor.execute(sql)
for row in cursor.fetchall():  
    print(row)  
print('共查找出', cursor.rowcount, '条数据')

# 插入数据
sql = "insert into testtb values(4,'Eviless',25)"
cursor.execute(sql)
connect.commit()
print('写入完成')

# 关闭连接  
cursor.close()  
connect.close()  