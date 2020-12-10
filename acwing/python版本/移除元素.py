'''
27. 移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。
示例 2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。

说明:

为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
你可以想象内部操作如下:
// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);
// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''
from typing import List


class Solution:
    # # 双指针
    # 双指针其实就是两个数，分别代表两个index，表示数组中第几个数的意思。
    # 比如这里，我们让a代表一个index，b代表一个index
    # 然后我们让a一直往后移动，相当于nums[a]从数组第一个数遍历到最后一个数。
    # 当且仅当我们发现nums[a] != val的时候，我们把这个数拷贝到b指向的位置，默认b是从0开始的，然后b += 1指向下一个位置。
    # 这样我们就保证了前b个数，就是我们要的结果。不重复的数。

    def removeElement(self, nums: List[int], val: int) -> int:
        fast,slow=0,0
        while fast<=len(nums)-1:
            if nums[fast]==val:
                fast+=1
            else:
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
        return slow

if __name__ == '__main__':
    s=Solution()
    a=s.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
    print(a)