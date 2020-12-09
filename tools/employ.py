import re
import pandas as pd
#读取txt
dic = './data/employ.txt'
file = open(dic, encoding='utf-8').read()
#匹配
pattern1=re.compile("门店.(.*)",flags=re.I)
pattern2=re.compile("促销日期.(.*)",flags=re.I)
pattern3=re.compile("姓名.(.*)",flags=re.I)
pattern4=re.compile("电话号码.(.*)",flags=re.I)
pattern5=re.compile("工行卡号.(.*)",flags=re.I)
pattern6=re.compile("工资标准.(.*)",flags=re.I)
#查找
result1=re.findall(pattern1,file)
result2=re.findall(pattern2,file)
result3=re.findall(pattern3,file)
result4=re.findall(pattern4,file)
result5=re.findall(pattern5,file)
result6=re.findall(pattern6,file)
#建表
dat1 = {'门店':result1,'促销日期':result2,'姓名':result3,'电话号码':result4,'工行卡号':result5,'工资标准':result6}
df=pd.DataFrame(dat1)
# 写入
df.to_excel('data1.xlsx',index=False)




