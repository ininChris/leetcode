# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        p1 = l1
        p2 = l2
        new = ListNode(0)
        last = new
        while p1!=None or p2!=None:
            if p1 !=None and p2 !=None:
                if p1.val > p2.val:
                    last.next = p2
                    p2 = p2.next
                else:
                    last.next = p1
                    p1 = p1.next
            elif p1 == None:
                last.next = p2
                p2 = p2.next
            elif p2 == None:
                last.next = p1
                p1 = p1.next
            last = last.next
        return new.next
        
                
        
