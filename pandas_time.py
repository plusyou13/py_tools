import pandas as pd
import datetime
df=pd.read_csv('./data/demo1.csv')
print(df['date'])
df['date']=pd.to_datetime(df['date'])
df['date']=df['date']+datetime.timedelta(hours=3)
print(df['date'])
df.to_csv('./data/demo2.csv',index=False)