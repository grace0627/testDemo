class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums)==0 :
            return 0
        
        #找到非val值得元素填充，剩余元素修改为val
        index = 0
        for i in range(0,len(nums)) :
            if nums[i] != val:
                nums[index] = nums[i]
                index = index + 1

        for i in range(index,len(nums)):
            nums[i] = val
        
        return index
        
        

#测试数据

t1 = Solution()
s1 = t1.removeElement([0,1,0,3,12],0)
s2 = t1.removeElement([3,2,2,3],3)
print(s1,s2)