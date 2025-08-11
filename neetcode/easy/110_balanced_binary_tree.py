from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        # if root is None:
        #     return False
        
        # # both sides should be returning a number with a difference of only 1 (so + or - 1)
        # # that means one node can have no root.left or root.right and the other can but cannot go two down

        # leftDepth = 1 + self.isBalanced(root.left)
        # rightDepth = 1 + self.isBalanced(root.right)


        # # print(leftDepth == rightDepth)
        # return leftDepth == rightDepth


        def check(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0  # height of empty tree is 0

            left = check(node.left)
            right = check(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1  # use -1 as a flag to mark imbalance

            return 1 + max(left, right)

        return check(root) != -1



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)



sol = Solution()

sol.isBalanced(root)

print(sol.isBalanced(root))