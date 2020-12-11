'''
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''

from typing import List


class Solution:
    # 一直维护min_price和max_profit两个变量，就可以一次遍历解决问题
    # 最大利润 = max{前一天最大利润, 今天的价格 - 之前最低价格}
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) < 2):
            return 0
        min_price = prices[0]
        # inf = int(1e9)
        # minprice = inf
        max_profits = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profits = max(max_profits, prices[i] - min_price)
        return max_profits


if __name__ == '__main__':
    s = Solution()
    a = s.maxProfit([7, 1, 5, 3, 6, 4])
    print(a)
