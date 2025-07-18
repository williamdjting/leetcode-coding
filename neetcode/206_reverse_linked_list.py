# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # current = head
        # tail = ListNode(current.val)
        # printList = []

        # while current.next:
        #     current = current.next # traverse while current.next is true
        #     tail.next = ListNode(current.val)

        # while tail.next:
        #     addTailValue = tail.val
        #     printList.append(addTailValue)

        # return printList

        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev 
