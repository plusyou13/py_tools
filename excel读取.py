import pandas as pd

df = pd.read_excel('./data/统计表.xlsx', skiprows=1, usecols="A:L", index_col=None)
print(df.tail())
df.to_excel('./data/data.xlsx', index=False)
