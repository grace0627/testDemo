# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 使用stack解决
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        #遍历字符串
        for i in range(0,len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                     
                            temp = stack.pop()
                
                            if s[i] == ')':
                                if temp != '(':
                                    return False
                  
                            elif s[i] == ']':
                                if temp != '[':
                                    return False

                            elif s[i] == '}':
                                if temp != '{':
                                    return False         

        if len(stack) == 0:
            return True
        else:
            return False
                
t1 = Solution()
s1 = t1.isValid('[](){}')       
print(s1)    
         
