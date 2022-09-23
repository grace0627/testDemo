#给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false
from typing import Mapping


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == 0 :
            return False
        mapping= {}
        for i in nums:
            if i not in mapping:
                mapping[i] = 1
            else:
                mapping[i]= mapping[i] + 1
        for v in mapping.values():
            if v > 1:
                return True
        return False

t1 = Solution()
s1 = t1.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(s1)

        