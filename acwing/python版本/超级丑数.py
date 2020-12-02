'''
313. 超级丑数
编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

输入: n = 12, primes = [2,7,13,19]
输出: 32
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
说明:

1 是任何给定 primes 的超级丑数。
 给定 primes 中的数字以升序排列。
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
第 n 个超级丑数确保在 32 位有符整数范围内
'''
from typing import List
import heapq

class Solution:
    # 动态规划
    def nthSuperUglyNumber1(self, n: int, primes: List[int]) -> int:
        L = [0 for i in range(len(primes))]
        result = [0 for i in range(n)]
        result[0] = 1
        for i in range(1, len(result)):
            min_u = min([result[L[j]]*primes[j] for j in range(len(L))])
            result[i] = min_u
            for k in range(len(L)):
                if result[L[k]]*primes[k] == min_u:
                    L[k] += 1
        return result[n-1]

    # 动态规划三步走
    # 第一步: 定义数组元素的含义，我们的问题是要求查找第n个超级丑数。那我们就定义dp[i]的含义为：从小到大排列的第i个丑数值为dp[i]。

    # 第二步: 找出数组元素间的关系式，我们的目的是要求dp[n]。但是dp数组前后之间好像没有什么联系。动态规划转移方程不能定量的写出来。于是看了答案，淦！原来还可以用k指针来做！！！
    # K个指针指向dp中的元素，最小的丑数只可能出现在如dp[l2]的2倍、dp[l7]的7倍、dp[l13]的13倍和dp[l19]的19倍四者中间。
    # 通过移动K个指针，就能保证生成的丑数是有序的。通过求到最小值来保证丑数数组有序排列。

    # 第三步: 找出初始条件，题目给定条件为1是任何给定primes的超级丑数。所以dp[0] = 1

    # ###算法流程
    # 初始化数组dp和len(primes)个指针。dp[0] = 1，表示最小的丑数为1。K个指针都指向dp[0]。
    # 重复以下步骤n次，dp[i]表示第i + 1小的丑数：
    # dp[i] = min(x * dp[y] for x, y in zip(primes, pointer))
    # 比较K者大小，令dp[i]为其中的最小值。这个zip用的是真的灵性，我单方面宣布我是 @ powcaicai大神的粉丝了，
    # 这里把质数和跟指针打包成元组，然后直接调用就可以实现质数乘上指针对应的下标所指的dp数组的值。
    # 如果dp[i] == primes * dp[pointer]，指针后移一位。dp[n - 1]即为第n小的丑数，返回。

    # 复杂度分析
    # 时间复杂度：O(n)。生成一个丑数只需常量时间，所以生成n个丑数需要O(n)。
    # 空间复杂度：O(n)。dp数组的长度为n。



    def nthSuperUglyNumber2(self, n: int, primes: List[int]) -> int:
        dp = [0] * n
        pointer = [0] * len(primes)
        dp[0] = 1
        for i in range(1, n):
            dp[i] = min(x * dp[y] for x, y in zip(primes, pointer))
            for j in range(len(primes)):
                if dp[i] == primes[j] * dp[pointer[j]]:
                    pointer[j] += 1
        return dp[-1]

    # 创建堆
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = []
        heapq.heappush(heap, 1)
        hashmap = set()
        hashmap.add(1)
        curr_ugly = 1
        for _ in range(n):
            curr_ugly = heapq.heappop(heap)  # pop堆顶
            # print(heap)
            for p in primes:
                new_ugly = curr_ugly * p
                if new_ugly not in hashmap:
                    hashmap.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
            # print(heap)
        return curr_ugly



if __name__ == '__main__':
    s=Solution()
    a=s.nthSuperUglyNumber(80,[13,11,7])
    print(a)