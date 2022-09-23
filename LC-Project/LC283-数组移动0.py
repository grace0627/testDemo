class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums)==0 :
            return 0
        
        #找到非0元素填充，剩余元素修改为0
        index = 0
        for i in range(0,len(nums)) :
            if nums[i] != 0:
                nums[index] = nums[i]
                index = index + 1

        for i in range(index,len(nums)):
            nums[i] = 0
        
        return nums

#测试数据

t1 = Solution()
s1 = t1.moveZeroes([0,1,0,3,12])
s2 = t1.moveZeroes([0])
print(s1,s2)