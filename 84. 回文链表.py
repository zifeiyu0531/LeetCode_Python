# 请判断一个链表是否为回文链表。

# 示例 1:

# 输入: 1->2
# 输出: false
# 示例 2:

# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        list_stack = []
        p = head
        while p != None:
            list_stack.append(p.val)
            p = p.next
        index = 0
        for num1, num2 in zip(list_stack, list_stack[::-1]):
            if num1 != num2:
                return False
            index += 1
            if index == len(list_stack)//2:
                break
        return True