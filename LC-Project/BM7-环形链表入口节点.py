# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from asyncio.windows_events import NULL


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return NULL

        fast = pHead
        slow = pHead
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                fast = pHead
                
                while slow != fast:
                    fast = fast.next
                    slow = slow.next

                return fast
            else:
                return NULL   
