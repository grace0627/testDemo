#给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from multiprocessing import dummy


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #临时保存头结点
        dummy = ListNode(0)
        #指向head节点
        dummy.next = head
        #pre 保存head节点上一个节点的信息
        pre = dummy
        while ( head != None ):
            if head.val == val:
                pre.next = head.next
                head = head.next
            else:
                pre = head
                head = head.next

        return dummy.next