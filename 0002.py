# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        result = None
        pr = None
        ci = 0
        while p1!=None or p2!=None:
            v1 = 0 if p1 == None else p1.val
            v2 = 0 if p2 == None else p2.val
            s = v1 + v2 + ci
            if s >= 10:
                ci = 1
                s = s % 10
            else:
                ci = 0
            if result == None:
                result = ListNode(s)
                pr = result
            else:
                pr.next = ListNode(s)
                pr = pr.next
            p1 = p1.next if p1 != None else None
            p2 = p2.next if p2 != None else None
        if ci != 0:
            pr.next=ListNode(ci)
        return result


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next=ListNode(4)
    l1.next.next=ListNode(3)

    l2 = ListNode(5)
    l2.next=ListNode(6)
    l2.next.next=ListNode(4)

    s = Solution()
    result = s.addTwoNumbers(l1,l2)
    pr = result
    while pr != None:
        print(pr.val, end = '')
        pr = pr.next
