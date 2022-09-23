#栈和哈希表
#在2中找到每一个元素的下一个更大值，保存在哈希表中，key为num2的元素，value为元素中下一个更大的值
from inspect import stack
from threading import stack_size


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
      
        res = []
        st = []
        hash = {}
        for num in nums2:
            while (len(st) != 0 and num > st[-1]):
                temp = st.pop()
                hash[temp] = num
            st.append(num)
        while len(st) != 0:
            temp = st.pop()
            hash[temp] = -1
        for i in nums1:
            res.append(hash[i])

    
        return res 

t1 = Solution()
s1 = t1.nextGreaterElement([4,1,2],[1,3,4,2])
print(s1)





