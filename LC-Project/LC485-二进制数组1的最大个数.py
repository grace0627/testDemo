#数组遍历
from itertools import count


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        #判断数组是否为空
        if nums is None or len(nums) ==0:
            return 0
        #遍历数组
        count = 0
        result = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count = count + 1
            else:
                result = max(result,count)
                count = 0
        return max(result,count)


#测试数据
t1 = Solution()
s1 = t1.findMaxConsecutiveOnes([1,1,0,1,1,1])
print(s1)

