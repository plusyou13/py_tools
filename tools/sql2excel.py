import pymysql
import pandas as pd
# 连接mysql
conn = pymysql.connect(host='localhost', user='root',password='root',
                       database='test_db',charset="utf8mb4")
sql_1 = "select * from book "
#利用pandas直接获取数据
data = pd.read_sql(sql_1, conn)
conn.close()
writer = pd.ExcelWriter('demo2.xlsx')
# 利用to_excel()方法将不同的数据框及其对应的sheet名称写入该writer对象中
data.to_excel(writer,sheet_name='test_db')
# 数据写出到excel文件中,最后保存
writer.save()