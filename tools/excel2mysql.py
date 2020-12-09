'''
import pymysql
import time
import random
#连接mysql
db = pymysql.connect('101.132.253.52','root','1123','test_db')
#获取mysql操作光标
cursor = db.cursor()
#初始化变量
count = 0
#设置sql语句循环次数
while count <= 1000000:
    count += 1
    #定义mysql字段的范围随机数变量
    num = random.randint(0,200)
    memo_num = random.randint(500,811)
    city_list = ['a','b','c','d']
    a = random.choice(city_list)
    #生成mysql语句插入语句
    sql = "insert  into city(id,city_code,city_name,memo)values(%d,%s,'%s',%s)" %(count,num,a,memo_num)
    #执行sql语句

    try:
        cursor.execute(sql)
        db.commit()
        print("1")
    #错误回滚
    except:
        db.rollback()
#关闭mysql
        print("0")

db.close()
'''
from sqlalchemy import create_engine
import pandas as pd
import pymysql

# 创建engine 用来执行SQL语句
engine = create_engine("mysql+pymysql://root:1123@127.0.0.1:3306/test_db?charset=utf8mb4")

df = pd.read_excel("./data/book.xlsx")
print(df)
df.to_sql(name="book", con=engine, schema='test_db', if_exists="replace")
