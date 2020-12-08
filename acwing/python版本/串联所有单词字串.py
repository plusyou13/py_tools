'''
30. 串联所有单词的子串
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。



示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
'''
from typing import List, Counter


class Solution:
    def findSubstring(self, s, words):
        answer = []
        slen, wlen = len(s), len(words)

        # 判断特殊情况
        if len(words) == 0:
            return answer
        onewordlen = len(words[0])
        if slen < wlen * onewordlen:
            return answer

        # 建立第word里面的hashmap
        # word_dic = {}
        word_dic=Counter(words)
        # print(word_dic)
        # for i in words:
        #     if i in word_dic:
        #         word_dic[i] += 1
        #     else:
        #         word_dic[i] = 1

        for j in range(onewordlen):
            i = j
            move_dic = {}
            total_move = 0
            while i <= slen - onewordlen:

                ss = s[i:i + onewordlen]
                if ss in word_dic:
                    total_move += 1
                    if ss not in move_dic:
                        move_dic[ss] = 1
                    else:
                        move_dic[ss] += 1
                else:
                    # 情况2 当没有这个单词的时候 直接跳转
                    move_dic = {}
                    total_move = 0
                    i += onewordlen
                    continue
                # 当move_dic里面有和word_dic相同个单词时
                if total_move == wlen:
                    # 找到起始位置
                    start = i - onewordlen * (wlen - 1)

                    if move_dic == word_dic:
                        answer.append(start)

                    # 删除substring里面的第一个单词
                    start_s = s[start:start + onewordlen]
                    move_dic[start_s] -= 1
                    total_move -= 1

                    # 删除的一个特殊情况，这时候删除了单词但是move_dic里面的值==0，要删除key
                    if move_dic[start_s] == 0:
                        move_dic.pop(start_s)

                i += onewordlen

        return answer




    # 用1个hashmap记录words中单词的数量来加速匹配
    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        n, m = len(s), len(words)
        l = len(words[0]) if m else 0
        res = []
        # 当s长度大于等于words长度时，才有可能有解
        if n >= l * m:
            # 为加速查找，使用hash结构储存words中各字符的个数
            d = {}
            for i in words:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            # 字符偏移有l-1种情况
            for j in range(l):
                L = []
                for i in range(j, n - l + 1, l):
                    # 对s从i截取长度为l的切片
                    ss = s[i:i + l]
                    # 此处hash判断明显快于list判断
                    if ss not in d:
                        L = []
                    else:
                        # 当在L中ss的数目和words中数目(用hash快速匹配)一样时
                        # 说明ss多余，L去掉从头到第1个ss位置的部份
                        if L.count(ss) == d[ss]:
                            idx = L.index(ss)
                            L = L[idx + 1:]
                        # 不管数目如何，最后都要在L中添加ss
                        L.append(ss)
                        # 当L的长度达到m时，说明找到匹配
                        if len(L) == m:
                            # 此时i指针已经走到了匹配的结果中第m-1个（最后1个）长度为l的单词位置
                            # 需要将i指针位置减少(m-1)*l
                            res.append(i - (m - 1) * l)
        return res

if __name__ == '__main__':
    s=Solution()
    a=s.findSubstring(  s = "barfoothefoobarman",words = ["foo","bar"])
    print(a)