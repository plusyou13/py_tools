'''
188. 买卖股票的最佳时机 IV
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
你最多可以完成 k 笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
'''

from typing import List


class Solution:
    # 首先要确定k的取值范围否则会产生超时的问题，因为买卖占用两天，所以当k>=n//2，会变成122题，解法此处略过；
    # else：因为只能持有一只股票，因此流程肯定是[买，卖...,买，卖]把成本和利润创造两个一维数组，长短为k+1，流程和121一样，
    # 就是寻找最小成本然后计算最大利润，当k=1时，即为寻找算小价格然后计算最大利润。
    #
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        else:
            cost = [float('inf') for i in range(k + 1)]
            profit = [0 for i in range(k + 1)]
            for p in prices:
                for i in range(1, k + 1):
                    cost[i] = min(cost[i], p - profit[i - 1])
                    profit[i] = max(profit[i], p - cost[i])
            return profit[-1]

    #
    # 解题思路
    # 这道题目需要利用动态规划:
    # 首先进行状态定义：
    # dp[i][k][j]
    # i代表第i天，k代表已经完成几次交易，j代表目前拥有几只股票，为0和1两种状态。注意一次交易完成为完成一次买卖交易，仅买股票不会增加一次交易。
    #
    # 初始状态确定：
    # 这道题目一开始初始状态有问题导致测试样例无法通过，最终思考初始状态如下：
    # 第i天之前进行0笔交易目前拥有0只股票的最大利润是0
    # dp[i][0][0] = 0
    # 第i天之前进行0笔交易目前拥有1只股票的最大利润是前一天同一状态与当前天买入一只股票二者中的最大值
    # dp[i][0][1] = max(dp[i - 1][0][1], -prices[i]) if i > 0 else -prices[0]
    # 初始化第0天的已经完成k次交易初值
    # dp[0][j][0] = 0
    # dp[0][j][1] = -prices[0]
    #
    # 状态转移方程
    # 第i天已经交易j次且目前拥有0只股票的最大利润
    # dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])  # 前一天同状态和前一天已经交易了k-1次，当天卖出的最大值
    # 第i天已经交易j次且目前拥有1只股票的最大利润
    # dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])  # 前一天同状态和前一天已经交易k次，当天买入一只的最大值

    def maxProfit2(self, k, prices):
        if not prices: return 0
        if k >= len(prices) // 2:  # 转换成无数次交易
            dp = [[0 for i in range(2)] for j in range(2)]
            dp[0][0], dp[0][1], res = 0, -prices[0], 0
            for i in range(1, len(prices)):
                x, y = i % 2, (i - 1) % 2
                dp[x][0] = max(dp[y][0], dp[y][1] + prices[i])
                dp[x][1] = max(dp[y][1], dp[y][0] - prices[i])
                res = max(res, dp[x][0])
            return res
        else:
            dp = [[[None, None] for _ in range(k + 1)] for _ in range(len(prices))]
            # 赋边界值
            for i in range(len(prices)):
                dp[i][0][0] = 0
                dp[i][0][1] = max(dp[i - 1][0][1], -prices[i]) if i > 0 else -prices[0]
            for j in range(1, k + 1):
                dp[0][j][0] = 0
                dp[0][j][1] = -prices[0]
            for i in range(1, len(prices)):
                for j in range(1, k + 1):
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])

            # 最后从多次交易中选出最大利润即可
            max_value = 0
            for i in range(k + 1):
                max_value = max(max_value, dp[-1][i][0])
            return max_value


if __name__ == '__main__':
    s = Solution()
    a = s.maxProfit2(k=1, prices=[3, 2, 6, 5, 0, 3])
    print(a)
