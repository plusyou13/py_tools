'''
860. 柠檬水找零
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：

输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。
示例 2：

输入：[5,5,10]
输出：true
示例 3：

输入：[10,10]
输出：false
示例 4：

输入：[5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。


提示：

0 <= bills.length <= 10000
bills[i] 不是 5 就是 10 或是 20
'''
import collections
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 创建字典
        have = collections.defaultdict(int)
        # 由于当客户给你五美元时，你需要找5-5美元，数组最长为10000，因此创建一个key为0值为10000的键值对，并且当顾客给你5美元时，只需在字典中key为5的加1就行
        have[0] = 10000
        # 遍历
        for i in range(len(bills)):
            # 需要找客户的钱
            haveToPay = bills[i] - 5
            # 找15美元的话p1为1，否则为0
            p1 = haveToPay // 10
            # 找5美元
            p2 = haveToPay % 10
            # 如果需要找15美元
            if p1:
                # 如果字典中key为10的个数小于等于0
                if have[p1 * 10] <= 0:
                    # 减去两个5块的键值对
                    have[5] -= 2
                    # 如果小于0，表示5快的不够找，返回False
                    if have[5] < 0:
                        return False
                # 如果足够支付，键值减1
                else:
                    have[p1 * 10] -= 1
            # 接下来找5块的
            have[p2] -= 1
            # 如果5快的不够，返回False
            if have[p2] < 0:
                return False
            # 收顾客的钱
            have[bills[i]] += 1
        return True



# 新建一个字典v，用来存现在有多少5元和10元。
# 如果顾客付的是5元，则5元数量加1；
# 如果顾客付的是10元，则5元数量减1，10元数量加1；如果5元数量不够，则无法找零；
# 如果顾客付的是20元，首先先用10元来找零，没有10元，则用5元找零，如果5元或10元数量不够，则无法找零。


    def lemonadeChange2(self, bills: List[int]) -> bool:
        v = {'five': 0, 'ten': 0}
        for i in range(len(bills)):
            if bills[i] == 5:
                v['five'] = v['five'] + 1
            elif bills[i] == 10:
                v['five'] = v['five'] - 1
                v['ten'] = v['ten'] + 1
                if v['five'] < 0 or v['ten'] < 0:
                    return False
                    break
            elif bills[i] == 20:
                if v['ten'] >= 1:
                    v['ten'] = v['ten'] - 1
                    v['five'] = v['five'] - 1
                else:
                    v['five'] = v['five'] - 3
                if v['five'] < 0 or v['ten'] < 0:
                    return False
                    break
        return True


if __name__ == '__main__':
    s=Solution()
    a=s.lemonadeChange2([5,5,5,10,10,20])
    print(a)
