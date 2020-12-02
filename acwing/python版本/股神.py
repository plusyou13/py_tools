'''

股神

题目描述

有股神吗？

有，小赛就是！

经过严密的计算，小赛买了一支股票，他知道从他买股票的那天开始，股票会有以下变化：
第一天不变，以后涨一天，跌一天，涨两天，跌一天，涨三天，跌一天...依此类推。
为方便计算，假设每次涨和跌皆为1，股票初始单价也为1，请计算买股票的第n天每股股票值多少钱？



输入
输入包括多组数据；

每行输入一个n，1<=n<=10^9 。

样例输入
1

2

3

4

5

输出
请输出他每股股票多少钱，对于每组数据，输出一行。

样例输出
1

2

1

2

3

import math

n=int(input())
if n==1:
    price=1
else:
    k=math.ceil((math.sqrt(8*n+1)-1)/2)
    if n==k*(k+1)/2:
        price=1+(k-2)*(k-1)/2
    else:
        price=4+n-2*k
print(int(price))

'''


def value(n):
    x=3
    i=3
    j=1
    out=0
    while x<=n:
        if n<x+i:
            out=n-2*j
            break
        else:
            x+=i
            i+=1
            j+=1
    return out

while 1:
    try:
        n=int(input())
        if n<=2:
            print(n)
        else:
            print(value(n))
    except:
        break