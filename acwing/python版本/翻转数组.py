'''

翻转数组

题目描述

给定一个长度为n的整数数组a，元素均不相同，问数组是否存在这样一个片段，
只将该片段翻转就可以使整个数组升序排列。其中数组片段[l,r]表示序列a[l], a[l+1], ..., a[r]。
原始数组为a[1], a[2], ..., a[l-2], a[l-1], a[l], a[l+1], ..., a[r-1], a[r], a[r+1], a[r+2], ..., a[n-1], a[n]，
将片段[l,r]反序后的数组是
a[1], a[2], ..., a[l-2], a[l-1], a[r], a[r-1], ..., a[l+1], a[l], a[r+1], a[r+2], ..., a[n-1], a[n]。



输入
第一行数据是一个整数：n (1≤n≤105)，表示数组长度。

第二行数据是n个整数a[1], a[2], ..., a[n] (1≤a[i]≤109)。

样例输入
4

2 1 3 4

输出
输出“yes”，如果存在；否则输出“no”，不用输出引号。

样例输出
yes
'''


def fun(a, n):
    idxmin = 0
    idxmax = 0
    flag = 0  # 默认不存在
    count = 0
    for i in range(1, n):
        if a[i - 1] < a[i]:
            flag = 0
        if flag == 0 and a[i - 1] > a[i]:
            flag = 1
            count += 1
            idxmin = i - 1
            idxmax = i
        elif flag == 1 and a[i - 1] > a[i]:
            flag = 1
            idxmax = i

    if count == 1:
        if idxmin == 0:
            if idxmax == n - 1:
                return 1
            else:
                if a[idxmin] < a[idxmax + 1]:
                    return 1
        else:
            if idxmax == n - 1:
                if a[idxmax] > a[idxmin - 1]:
                    return 1
            else:
                if a[idxmin] < a[idxmax + 1] and a[idxmax] > a[idxmin - 1]:  # 前后值反转后也要满足大小关系
                    return 1
    else:
        return 0


n = int(input())  # 输入数组长度
list1 = list(map(int, input().split()))
# a = []
# for i in range(n):
#     a.append(list1[i])
a=list1
x = fun(a, n)
if x == 1:
    print('yes')
else:
    print('no')
