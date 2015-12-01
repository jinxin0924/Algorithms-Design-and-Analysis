__author__ = 'Xing'
# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first,second=head,head
        while n:
            first=first.next
            n-=1
        if not first:
            return head.next
        while first.next!=None:
            first=first.next
            second=second.next
        second.next=second.next.next
        return head
