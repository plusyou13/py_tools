'''
204. 计数质数
统计所有小于非负整数 n 的质数的数量。

示例 1：
输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

示例 2：
输入：n = 0
输出：0

示例 3：
输入：n = 1
输出：0
'''
import math
class Solution:

    def countPrimes(self, n: int) -> int:
        def is_primes(c):
            """
            判断c是否为质数
            """
            # for i in range(2, n):
            for i in range(2, int(pow(c, 0.5)) + 1):
                if c % i == 0:
                    return False
            return True

        ans = 0
        for j in range(2, n):
            if is_primes(j):
                ans += 1
        return ans

    def countPrimes1(self, n: int) -> int:
        res = 0
        for i in range(2, n):
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                # print(i)
                res += 1
        return res

    def countPrimes2(self, n: int) -> int:
        isPrimes = [1] * n
        res = 0
        for i in range(2, n):
            if isPrimes[i] == 1: res += 1
            j = i
            while i * j < n:
                isPrimes[i * j] = 0
                j += 1
        return res





if __name__ == '__main__':
    s= Solution()


    b=s.countPrimes2(100000000)
    print(b)

    a=s.countPrimes1(100000000)
    print(a)
