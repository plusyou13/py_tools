'''
316. 去除重复字母（困难）
题目描述
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。
需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:
输入: "bcabc"
输出: "abc"

示例 2:
输入: "cbacdcbc"
输出: "acdb"
'''

# 这道题没有一个全局的删除次数 k。而是对于每一个在字符串 s 中出现的字母 c 都有一个 k 值。这个 k 是 c 出现次数 - 1。
# 沿用上面的知识的话，我们首先要做的就是计算每一个字符的 k，可以用一个字典来描述这种关系，其中 key 为 字符 c，value 为其出现的次数。
# 具体算法：
#
# 建立一个字典。其中 key 为 字符 c，value 为其出现的剩余次数。
# 从左往右遍历字符串，每次遍历到一个字符，其剩余出现次数 - 1.
# 对于每一个字符，如果其对应的剩余出现次数大于 1，我们可以选择丢弃（也可以选择不丢弃），否则不可以丢弃。
# 是否丢弃的标准和上面题目类似。如果栈中相邻的元素字典序更大，那么我们选择丢弃相邻的栈中的元素。
# 还记得上面题目的边界条件么？如果栈中剩下的元素大于 n - kn−k，我们选择截取前 n - kn−k 个数字。然而本题中的 k 是分散在各个字符中的，因此这种思路不可行的。
# 不过不必担心。由于题目是要求只出现一次。我们可以在遍历的时候简单地判断其是否在栈上即可。

import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        char_counter=collections.Counter(s)

        for char in s:
            if char not in stack:
                while stack and char<stack[-1] and char_counter[stack[-1]]>0:
                    stack.pop()
                stack.append(char)
            char_counter[char]-=1

        return ''.join(stack)

    # 由于本题中的stack并不是有序的，因此我们的优化点考虑空间换时间。而由于每种字符仅可以出现一次，这里使用hashset
    def removeDuplicateLetters2(self, s) -> int:
        stack = []
        seen = set()
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in seen:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)

if __name__ == '__main__':
    s=Solution()
    b=s.removeDuplicateLetters2('bcasdfgdfgasdhdfgrtesdfgasdfasdfdfgabcd')
    print(b)

