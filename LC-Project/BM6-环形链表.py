# 判断给定的链表中是否有环。如果有环则返回true，否则返回false
# 
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @return bool布尔型
#



class Solution:
    def hasCycle(self , head: ListNode) -> bool:
        if head is None:
            return False
        
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
              return True
        
            
        return False