import pandas as pd
import numpy as np
import time

start_time = time.time()
# 读取Excel文件
df_list = pd.read_excel('input.xlsx',sheet_name='底稿1--总部下发数据库')
df1 = pd.read_excel('input.xlsx',sheet_name='底稿1--总部下发数据库')
df2 = pd.read_excel('input.xlsx',sheet_name='底稿2-门店历史分销量及费用')

df_l = np.array(df_list[['中心','省区']].drop_duplicates()).tolist()

# 根据列 A 和列 B 的组合值拆分数据并保存为多个文件
for i in df_l:
    # 获取指定列的值
    value_a = i[0]
    value_b = i[1]

    # 创建一个新的DataFrame，包含匹配组合值的行
    subset_df1 = df1.loc[(df1['中心'] == value_a) & (df1['省区'] == value_b)]
    subset_df2 = df2.loc[(df2['中心'] == value_a) & (df2['省区'] == value_b)]

    # 创建一个新的Excel文件
    writer = pd.ExcelWriter(f'.\output\{value_a}_{value_b}.xlsx')

    # 将DataFrame写入Excel文件的Sheet中
    subset_df1.to_excel(writer, sheet_name='底稿1--总部下发数据库', index=False)
    subset_df2.to_excel(writer, sheet_name='底稿2-门店历史分销量及费用', index=False)

    # 保存Excel文件
    writer.save()

print("拆分完成")
end_time = time.time()

print(end_time-start_time)