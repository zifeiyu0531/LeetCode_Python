# 删除链表中等于给定值 val 的所有节点。

# 示例:

# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p = ListNode(0)
        p_head = p
        p.next = head
        while p != None and p.next != None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return p_head.next