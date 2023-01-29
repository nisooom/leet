# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        finalNode = ListNode(val=head.val)
        while True:
            if head.next is None:
                break
            if head.next.val == head.val:
                continue
            else:
                finalNode.next = ListNode(val=head.next.val)
                finalNode = finalNode.next
            head = head.next

        return finalNode