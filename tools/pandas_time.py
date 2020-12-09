import pandas as pd
import datetime

df = pd.read_csv(r'.\data\demo1.csv')
print(df['date'])
df['date'] = pd.to_datetime(df['date'])
# 调用DateOffset()时间偏移
# Timedelta相当于Python的datetime.timedelta
df['date'] = df['date'] + pd.DateOffset(hours=5)
# df['date'] = df['date'] + datetime.timedelta(hours=3)
print(df['date'])
df.to_csv(r'.\data\demo2.csv', index=False)
