'''
659. 分割数组为连续子序列
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。
如果可以完成上述分割，则返回 true ；否则，返回 false 。

示例 1：
输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5


示例 2：
输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3, 4, 5
3, 4, 5


示例 3：
输入: [1,2,3,4,4,5]
输出: False
'''
import collections
import itertools
from typing import List
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        res = []
        for n in nums:
            for v in res:
                if n == v[-1] + 1:
                    v.append(n)
                    break
            else:
                res.insert(0, [n])
# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False...元素除了是 0、空、None、False 外都算 True。
        return all([len(v) >= 3 for v in res])


    def isPossible2(self, nums: List[int]) -> bool:
        """
        关心最小的索引start从哪里开始和结束
        """
        pre,precount=None,0
        start=collections.deque()
        for t,group in itertools.groupby(nums):#中间有断隔
            num=len(list(group))
            if pre is not None and t-pre!=1:
                for _ in range(precount):
                    if pre<start.popleft()+2:
                        return False
                pre,precount=None,0
            if pre is None or t-pre==1:
                if num-precount>0:#说明t要作为某一序列的开头
                    for _ in range(num-precount):
                        start.append(t)
                elif num-precount<0:
                    for _ in range(precount-num):
                        if t<start.popleft()+2+1:
                            return False
            pre,precount=t,num
        return all(nums[-1]>=x+2 for x in start)



if __name__ == '__main__':
    s=Solution()
    a=s.isPossible([1,2,3,4,4,5])
    print(a)














