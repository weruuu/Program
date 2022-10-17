import pandas as pd
from sqlalchemy import create_engine
import openpyxl

connect=create_engine('oracle://exp:exp123@10.100.0.10:1530/EXPORA')
sql = '''select  t.ORG_ID 组织编码,t.org_name 组织,k.kunnr 经销商编码,k.name1 经销商名称,t.the_year||LPAD(t.the_month,2,'0') 年月,t.costtypename 费用科目,
        d.budget_number 费用编号,d.cur_op_money 操作金额,d.operatorname 操作人,d.reason 操作类型,d.memo 备注,d.last_modify 操作时间
 from market.market_tb_number_detail d
inner join market.market_tb_number t on d.budget_number=t.budget_number
left join crm.crm_tb_kunnr k on t.kunnr=k.kunnr
where
t.the_year = '2022' and t.the_month = '7'
--((t.the_year='2023' and t.the_month in ('1','2','3','4','5','6'))
--    or (t.THE_YEAR = '2022' and t.the_month in ('7','8','9','10','11','12')))
and d.check_flag='Y'
and  t.budget_type = 'P'
order by d.last_modify'''
data=pd.read_sql(sql , connect)
df = pd.DataFrame(data,columns=['组织','经销商名称','年月','操作金额'])
df = df.groupby(['组织','经销商名称','年月']).sum()
df = df[df.操作金额!=0]
df.reset_index(inplace=True)
# print(df)
# df.to_excel('C:/Users/Eviless/Documents/GitHub/Program/Jupyter/test.xls',index= False)

book = openpyxl.Workbook()
#建立写入对象
write = pd.ExcelWriter(r'C:/Users/Eviless/Documents/GitHub/Program/Jupyter/test.xlsx', engine='openpyxl')
write.book = book
write.sheets = {ws.title: ws for ws in book.worksheets}
#写入数据
df.to_excel(write, sheet_name='sheet', header=True, index=False)
write.save()
write.close()