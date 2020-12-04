'''
410. 分割数组的最大值
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
'''
from typing import List
from random_num import get_randomNumber

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left



    def splitArray2(self, nums: List[int], m: int) -> int:
        # 二分查找
        # 指定二分查找范围
        left, right = max(nums), sum(nums)
        # 定义 测试中点是大还是小的 测试函数
        def test_mid(mid):
            # 初始化
            num = 1  # num表示使用该mid我们会得到几个数组
            s = 0  # s表示当前数组的和
            for i in nums:
                if s + i > mid:  # 如果当前数组已经超过mid，要停止这个数组
                    s = i  # 这个数变为下一个数组的开头
                    num += 1  # 会得到的数组数量+1
                else:
                    s += i
            return num > m  # 数组总数是否>m, 大于的话说明mid太小，二分查找取右边
            # 这里有一个注意点，如果num已经等于m了, 但此时如果left不等于right，范围还是会继续收敛的，
            # 且取的是左半边，目的是让我们能最终找到一个确切的值，这个值恰好就是取得了最大值的那个数组的和
            # (因为小于这个和的话，就不能通过num=m的测试；而大于这个m的话，即使通过了num=m的测试，
            # 范围也会继续向左边收敛，直到我们找到的就是这个和)。
        # 进行二分查找
        while left < right:  # 当left == right的时候就终止查找，返回任意一个
            mid = (left + right) // 2
            if_right = test_mid(mid)
            if if_right:
                left = mid + 1
            else:
                right = mid  # num <= m的情况
        return left



if __name__ == '__main__':
    s=Solution()
    a=s.splitArray2(nums=get_randomNumber(19),m=7)
    print(a)
