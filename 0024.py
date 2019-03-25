# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def printList(self,head):
        p = head
        while p!=None:
            print(p.val,end='')
            p = p.next
        print('')
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        s = p
        p.next = head
        p1 = head
        p2 = head.next if head!=None else None
        
        while p1 != None and p2 !=None:
            p1.next = p2.next
            p2.next = p1
            p.next=p2
            
            p = p1
            p1 = p1.next
            p2 = p1.next if p1!=None else None

        return s.next
        
