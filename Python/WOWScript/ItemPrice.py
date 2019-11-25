import time
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

current_date = time.strftime("%Y%m%d%H%M%S", time.localtime())
f = open('C:/World of Warcraft/_classic_/WTF/Account/192230126#6/SavedVariables/Auctionator.lua', 'r',encoding='utf-8', errors='ignore')
StartRec = 0
Result = []
LineNo = [0,0]
ItemName = ''
ItemPrice = ''
for line in f:
    # Result.append([])
    if line.find('巨龙追猎者')!=-1:
        StartRec = 1
    if line.find('巨龙追猎者')!=-1 or line.find('Eviless')!=-1:
        continue
    if StartRec == 1 and line.find('"] = {')!=-1:
        ItemName = line[line.find('"')+1:line.find('"',line.find('"')+1)]
        LineNo[0] += 1
    elif StartRec == 1 and line.find('mr')!=-1:
        ItemPrice = line[line.find('= ')+2:line.find(',')]
        LineNo[1] += 1
    else:
        continue
    if LineNo[0]==LineNo[1]:
        Result.append([ItemName,ItemPrice])

# for i in Result:
#     print(i)

# 插入数据
for i in range(0,len(Result)):
    sql = "insert into mysql.ItemPrice values('"+Result[i][0]+"','"+Result[i][1]+"','"+current_date+"')"
    cursor.execute(sql)
connect.commit()
print('写入完成')

cursor.close()
connect.close()

