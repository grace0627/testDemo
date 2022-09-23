# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
from ast import If


class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        #判断两个链表是否为空      
        if pHead1 is  None or pHead2 is None:
            return None
        #创建两指针，分别指向两链表头节点
        pA = pHead1
        pB = pHead2
        
        while  pA != pB :
            #遍历完1链表，值为null 后又遍历2链表
            pA = pA.next if pA else pHead2
            pB = pB.next if pB else pHead1
        return pA

        


        