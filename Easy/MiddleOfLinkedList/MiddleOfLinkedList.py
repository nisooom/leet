# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        Llist = []
        while True:
            if head.next is None:
                Llist.append(head.val)
                break
            Llist.append(head.val)
            head = head.next

        finallist = ListNode(val=Llist[int(len(Llist) / 2)])
        for i in range(int(len(Llist) / 2) + 1, len(Llist) + 1):
            finallist.next = ListNode(val=Llist[i])
        return finallist        
