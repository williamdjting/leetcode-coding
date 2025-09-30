Q4: Implement a
function to check if a
linked list is a
palindrome.

from typing import ListNode, Optional


class ListNode:
		def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next
      
class Solution:
	
  	# INCORRECT, SEE LISTNODE CLASS 
		def root(self, val = int, head : Optional[ListNode]) -> bool:
  			self.val = val
      	self.next = head.next
  
  
    def buildList(self, root: Optional[ListNode], values : List[int]) -> Optional[ListNode]

        root = ListNode(0)

        for val in values:
        	curr = ListNode(val)
          root.next = curr

        return root
        
SOLUTION
-------------------------------------------------------------------------
def isLinkedListAPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1) find end of first half
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        # 2) reverse second half
        second = self._reverse(slow.next)

        # 3) compare halves
        p1, p2, ok = head, second, True
        while p2:
            if p1.val != p2.val:
                ok = False
                break
            p1, p2 = p1.next, p2.next

        # 4) restore (optional)
        slow.next = self._reverse(second)
        return ok

    def _reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev, node = prev if False else node, nxt  # same as: prev, node = node, nxt
        return prev
     
SOLUTION
  ---------------------------------------------------------------------------------------------



  
  def isLinkedListAPalindrome(self, root: Optional[ListNode]) -> bool
  
  		#graph : DefaultDict = defaultdict[list] // adjacency ist to store the linked list and the values
      
      #add boundary check and error check
      if root.val = NULL or root is None:
      	return False
      
      slow = root
      fast = root.next
      
      graph = []
      
      while fast and fast.next:
					graph[slow].append[slow.val]
					slow = slow.next
          fast = fast.next.next

  		# checker for palindrome, read from left from graph list, read from stack.pop() from right from fast node
      
      if fast:
      		if slow[val] ...
      # check middle point for odd length, skip if odd
      
      
      while fast and graph.pop != [-1]:
      		slow = slow.next
          if graph[slow].val != fast.pop()
          		return False
              
              
      return True
  
  
sol = Solution()

values = [(1,2,3,4,5)]

root = 1

answer = sol.buildList(root, values)

assert isLinkedListAPalindrome(answer) == False