'''
123. 买卖股票的最佳时机 III
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
'''

from typing import List


class Solution:
    # 一直维护min_price和max_profit两个变量，就可以一次遍历解决问题
    # 最大利润 = max{前一天最大利润, 今天的价格 - 之前最低价格}
    # 交易2 次，在第二次买的时候，价格其实是考虑了用了第一次赚的钱去补贴一部分

    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) < 2):
            return 0
        # min_price = prices[0]
        # inf = int(1e9)
        # minprice = inf

        min_price1 = min_price2 = float('inf')
        max_profits1 ,max_profits2= 0,0
        for i in range(len(prices)):
            min_price1 = min(min_price1, prices[i])
            max_profits1 = max(max_profits1, prices[i] - min_price1)
            min_price2 = min(min_price2, prices[i]-max_profits1 )
            max_profits2 = max(max_profits2, prices[i] - min_price2)
        return max_profits2


if __name__ == '__main__':
    s = Solution()
    a = s.maxProfit([3,3,5,0,0,3,1,4])
    print(a)




