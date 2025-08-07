# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        # base case: both Nodes are None

        if not p and not q:
            return True # because same
        
        # if only one is None, trees are different
        if not p or not q:
            return False
        

        # if values differ, trees are different
        if p.val != q.val: 
            return False
        
        #recursively check left and right subtrees and ask the same questions
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # if at any point in this recursion they break, then return as required
