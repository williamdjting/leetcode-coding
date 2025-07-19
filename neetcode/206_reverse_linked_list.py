from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution with reverseList method
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

# Helper function: Convert list to linked list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

# Helper function: Print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))

# Main function
def main():
    # Step 1: Create a linked list
    values = [1, 2, 3, 4, 5]
    head = build_linked_list(values)
    
    print("Original Linked List:")
    print_linked_list(head)

    # Step 2: Reverse the linked list
    solution = Solution()
    reversed_head = solution.reverseList(head)

    # Step 3: Print the reversed linked list
    print("Reversed Linked List:")
    print_linked_list(reversed_head)

# Execute the main function
main()
