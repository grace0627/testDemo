#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param target int整型 
# @param array int整型二维数组 
# @return bool布尔型
#
from re import A


class Solution:
    def Find(self , target: int, array: list[list[int]]) -> bool:
        # write code here
        if len(array) == 0 or len(array[0]) == 0:
            return False
        m = len(array) 
        n = len(array[0])
        i = 0
        j = n - 1
        while i <= (n-1) and j >= 0:
            if array[i][j] == target:
                return True

            elif array[i][j] < target:
                i = i + 1
            
            elif array[i][j] > target:
                j = j - 1

        return False

t1 = Solution()
s1 = t1.Find(15,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])           
print(s1)      