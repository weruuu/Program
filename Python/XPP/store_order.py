import tkinter as tk
from tkinter import filedialog
import pandas as pd
import cx_Oracle
import datetime
import shutil

# 创建Tkinter窗口
root = tk.Tk()
root.withdraw()

# 打开文件对话框，选择要读取的Excel文件
file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx;*.xls')])

# 如果未选择文件，则退出程序
if not file_path:
    exit()

print(file_path)

# 关闭Tkinter窗口
root.destroy()

# 读取Excel文件中的数据
df = pd.read_excel(file_path)
data = df.values.tolist()
print(datetime.datetime.now(),'Excel读取完成')

# 连接Oracle数据库
conn = cx_Oracle.connect('xpp_sfa/oracle@10.99.3.51:1521/EISP')
# conn = cx_Oracle.connect('localuser/demo1029@localhost:1521/orcl')
cursor = conn.cursor()

# 清空中间表
sql = 'call XPP_SFA.YYH_STEP4()'
cursor.execute(sql)

# 将数据写入Oracle表
count,total = 0,0
data_ins = []
for row in data:
    # if str(row[0]).find(' ') == -1:
    #     sale_date = "'"+str(row[0])+"',"
    # else :
    #     sale_date = "'"+str(row[0])[:str(row[0]).find(' ')]+"',"
    # kunnr,kunnr_name,cus_term_name,sku_code,cus_sku_name,box_num,remark  \
    #     = "'"+str(row[1])+"',","'"+str(row[2])+"',","'"+str(row[3])+"',","'"+str(row[4])+"',","'"+str(row[5])+"',","'"+str(row[6])+"',","'"+str(row[7]).replace('nan','')+"'"

    if str(row[0]).find(' ') == -1:
        sale_date = str(row[0])
    else :
        sale_date = str(row[0])[:str(row[0]).find(' ')]
    kunnr,kunnr_name,cus_term_name,sku_code,cus_sku_name,box_num,remark  \
        = str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]).replace('nan','')
    data_ins.append([sale_date , kunnr , kunnr_name , cus_term_name , sku_code , cus_sku_name , box_num , remark])
    # print(data_ins)
sql = 'INSERT INTO XPP_SFA.TS_STORE_ORDER_IMPORT_HISTORY_YYH_1ST (SALEDATE, CUSTOMERCODE, CUSTOMERNAME, CUSTOMERTERMINALNAME, SKUCODE, CUSTOMERSKU, BOXNUMSTR, REMARK) VALUES (:1,:2,:3,:4,:5,:6,:7,:8)'
# sql = 'INSERT INTO LOCALUSER.TS_STORE_ORDER_IMPORT_HISTORY_YYH_1ST (SALEDATE, CUSTOMERCODE, CUSTOMERNAME, CUSTOMERTERMINALNAME, SKUCODE, CUSTOMERSKU, BOXNUMSTR, REMARK) VALUES (:1,:2,:3,:4,:5,:6,:7,:8)'
cursor.executemany(sql,data_ins)
    # count += 1
    # if count >= 2000 :
    #     conn.commit()
    #     total = total + count
    #     print(now,'已写入数据', total)
    #     count = 0
conn.commit()
sql = 'SELECT COUNT(1) FROM XPP_SFA.TS_STORE_ORDER_IMPORT_HISTORY_YYH_1ST'
cursor.execute(sql)
insert_count = cursor.fetchall()
print(datetime.datetime.now(),'数据初始化完成',insert_count[0][0],'条')

# 数据清洗
sql = 'call XPP_SFA.YYH_STEP1()'
cursor.execute(sql)
print(datetime.datetime.now(),'数据清洗完成')

#异常数据校验
sql = 'select count(1) from XPP_SFA.ERRDATA1'
cursor.execute(sql)

results = cursor.fetchall()
if results[0][0] > 0 :
    sql = 'select distinct CUSTOMERCODE 经销商编码,CUSTOMERNAME 经销商名称,CUSTOMERTERMINALNAME 经销商系统门店名称,SFA_STORE_CODE SFA门店编码,SFA_STORE_NAME SFA门店名称,ERRMSG 错误信息 from XPP_SFA.ERRDATA1'
    cursor.execute(sql)
    df = pd.read_sql(sql , conn)
    err_kunnr_name = "/"+df.iloc[0][1]+"-门店异常.xlsx"
    df.to_excel('C:/Users/Eviless/Downloads'+err_kunnr_name,index=False,encoding='utf-8')
    print('门店关系异常')
    exit()
else :
    print(datetime.datetime.now(),'门店校验通过')
sql = 'select count(1) from XPP_SFA.ERRDATA2'
cursor.execute(sql)

results = cursor.fetchall()
if results[0][0] > 0 :
    sql = 'select * from XPP_SFA.ERRDATA2'
    cursor.execute(sql)
    df = pd.read_sql(sql , conn)
    err_kunnr_name = "/SKU异常.xlsx"
    df.to_excel('C:/Users/Eviless/Downloads'+err_kunnr_name,index=False,encoding='utf-8')
    print('SKU异常')
    exit()
else :
    print(datetime.datetime.now(),'SKU校验通过')

# 数据写入
sql = 'call XPP_SFA.YYH_STEP2()'
cursor.execute(sql)
print(datetime.datetime.now(),'写入完成')

# 数据核对
sql = 'select * from XPP_SFA.datacount'
cursor.execute(sql)
results = cursor.fetchall()
for i in results:
    print(i)

# 清空中间表
sql = 'call XPP_SFA.YYH_STEP4()'
cursor.execute(sql)
print(datetime.datetime.now(),'清空完成')

# 关闭数据库连接
cursor.close()
conn.close()

# 文件归档
shutil.move(file_path, 'C:/Users/Eviless/Downloads/历史回单/新桥/归档')
print(datetime.datetime.now(),'文件已归档')