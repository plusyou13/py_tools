'''
剑指 Offer 49. 丑数
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。



示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。
'''
import heapq
class Solution:


    def nthUglyNumber(self, n: int) -> int:
        #ugly number: can be only devided by 2,3,5
        #DP：dp[i]:the ith ugly number
        #dp[i]=min(dp[a]*2,dp[b]*3,dp[c]*5)
        dp = [1 for _ in range(n)]
        a = b = c = 0
        for i in range(1,n):
            dp[i] = min(dp[a]*2, dp[b]*3, dp[c]*5)
            if dp[i] == dp[a]*2: a += 1
            if dp[i] == dp[b]*3: b += 1
            if dp[i] == dp[c]*5: c += 1
        return dp[-1]

    def nthUglyNumber1(self, n: int) -> list:
        #ugly number: can be only devided by 2,3,5
        #DP：dp[i]:the ith ugly number
        #dp[i]=min(dp[a]*2,dp[b]*3,dp[c]*5)
        dp = [1 for _ in range(n)]
        a = b = c = 0
        for i in range(1,n):
            dp[i] = min(dp[a]*2, dp[b]*3, dp[c]*5)
            if dp[i] == dp[a]*2: a += 1
            if dp[i] == dp[b]*3: b += 1
            if dp[i] == dp[c]*5: c += 1
        return dp

    # 解法2：最小堆
    # 注意到丑数乘以2, 3, 5
    # 得到的数依旧是丑数。从1开始，不断的生成丑数2, 3, 4, 5。但注意到，如果只是单纯的由前个丑数乘以2, 3, 5
    # 得到下面的丑数，则不是顺序产生的，并且可能有重复，即1->2, 3, 5->4, 6, 10, 6, 9, 15->...，为保证顺序性，可采用最小堆和集合。
    # 设n = 4:
    #
    # [1] ->弹出堆顶1，得到
    # {2, 3, 5}
    # 压入堆中。res = [1]
    # [2, 3, 5] ->弹出堆顶2，得到
    # {4, 6, 10}
    # 压入堆中。res = [1, 2]
    # [3, 4, 5, 6, 10] ->弹出堆顶3，得到
    # {6, 9, 15}，求差集得到
    # {9, 15}
    # 压入堆中。res = [1, 2, 3]。从而满足了互异性。
    # [4, 5, 6, 10, 9, 15] ->弹出堆顶4，得到
    # {8, 12, 20}，压入堆中。res = [1, 2, 3, 4]。从而满足了顺序性。
    # 得到ugly_num = res[-1] = 4
    # 则有：
    #
    # 将1放入堆ls中
    # 遍历n次
    # 取出堆顶元素cur，放入res列表中
    # cur乘以2, 3, 5
    # 分别得到cur1，cur2，cur3,
    # 将
    # {cur1, cur2, cur3}
    # 与
    # {ls}
    # 求差集，将差集元素放入堆中
    # 返回res[-1]
    #

    def nthUglyNumber2(self, n: int) -> int:
        # ugly number: can be only devided by 2,3,5
        # using the min-heap
        res = []
        ls = [1]
        heapq.heapify(ls)
        for _ in range(n):
            cur = heapq.heappop(ls)
            res.append(cur)
            cur1, cur2, cur3 = cur * 2, cur * 3, cur * 5
            setls = set(ls)
            setTmp = {cur1, cur2, cur3}
            diff = setTmp.difference(setls)
            print(diff)
            if diff:
                for item in diff:
                    heapq.heappush(ls, item)
        return res[-1]



    # 暴力法
    def nthUglyNumber3(self, n: int) -> int:
        # ugly number: can be only devided by 2,3,5
        def isUglyNum(num):
            while num % 2 == 0:
                num //= 2
            while num % 3 == 0:
                num //= 3
            while num % 5 == 0:
                num //= 5
            return True if num == 1 else False
        cnt = 0
        num = 0
        while cnt < n:
            num += 1
            if isUglyNum(num): cnt += 1
        return num



if __name__ == '__main__':
    s=Solution()
    a=s.nthUglyNumber1(80)
    print(a)