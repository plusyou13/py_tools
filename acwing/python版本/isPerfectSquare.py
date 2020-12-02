'''
367. 有效的完全平方数
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False
'''
class Solution:
    # 暴力法
    def isPerfectSquare1(self,num)->bool:
        i=1
        while i*i<num:
            i+=1
        return i*i==num
    # 二分法
    def isPerfectSquare2(self,num)->bool:
        left=1
        right=num
        while left<=right:
            mid=(left+right)//2
            if mid*mid<num:
                left=mid+1
            elif mid*mid>num:
                right=mid-1
            else:
                return True
    #数学定理
    def isPerfectSquare3(self, num) -> bool:
        i=1
        while num>0:
            num-=i
            i+=2
        return num==0

    # 牛顿迭代法
    def isPerfectSquare4(self,num)->bool:
        if 1==num:
            return True
        i=num//2
        while i*i>num:
            i=(i+num//i)//2
        return i*i==num

s=Solution()
t1=s.isPerfectSquare1(13)
t2=s.isPerfectSquare2(16)
t3=s.isPerfectSquare3(16)
t4=s.isPerfectSquare4(16)
print(t1)
print(t2)
print(t3)
print(t4)
