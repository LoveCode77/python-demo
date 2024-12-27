# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1:
            return l2
        if not l2:
            return l1
        l1.val+=l2.val
        if l1.val>=10:
            l1.next=self.addTwoNumbers(ListNode(l1.val//10),l1.next)
            l1.val%=10
        l1.next=self.addTwoNumbers(l1.next,l2.next)
        return l1


