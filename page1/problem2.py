# Definition for singly-linked list.

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            l1 = ListNode(0, None)
        if l2 is None:
            l2 = ListNode(0, None)
        current = l1.val + l2.val
        if current >= 10:
            if l1.next is None:
                l1.next = ListNode(1, None)
            else:
                l1.next.val = l1.next.val + 1

        return ListNode(current % 10, self.addTwoNumbers(l1.next, l2.next))


class ListNode(object):
    def __init__(self, val=0, next_val=None):
        self.val = val
        self.next = next_val
