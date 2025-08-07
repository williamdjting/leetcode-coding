from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        if root is None:
            return 0
        


        count = 1 + max( self.maxDepth(root.left), self.maxDepth(root.right) )


        print("count", count)
        return count
    
# root = [3,9,20,None,None,15,7] #not a binary tree

# must construct it as a binary tree firstly
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()

sol.maxDepth(root)