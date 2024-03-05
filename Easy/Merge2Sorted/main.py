# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        s = "sda".isal

        head = ListNode()
        tail = head

        while list2 != None and list1 != None:
            if list2.val > list1.val:
                newNode = ListNode(list1.val)
                tail.next = newNode
                tail = tail.next
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                tail.next = newNode

                list2 = list2.next
                tail = tail.next

        while list2 != None:
            newNode = ListNode(list2.val)
            tail.next = newNode
            tail = tail.next

            list2 = list2.next

        while list1 != None:
            newNode = ListNode(list1.val)
            tail.next = newNode
            tail = tail.next
            list1 = list1.next

        return head.next

