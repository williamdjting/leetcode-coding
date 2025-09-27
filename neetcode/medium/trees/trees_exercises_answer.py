from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right


# 1) Build & print (preorder)
def print_tree(root: Optional[TreeNode]):
    """Preorder print (root, left, right)."""
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


# 2) Preorder traversal → list
def preorder(root: Optional[TreeNode]) -> list[int]:
    res: list[int] = []
    def dfs(node: Optional[TreeNode]):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res


# 3) Tree max depth
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# 4) Level order traversal (BFS)
def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    levels: list[list[int]] = []
    q = deque([root])
    while q:
        size = len(q)
        level: list[int] = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        levels.append(level)
    return levels



# Trees
root = TreeNode(1, TreeNode(2), TreeNode(3))
print_tree(root)                 # 1 2 3
print(preorder(root))            # [1,2,3]
print(max_depth(root))           # 2
print(level_order(root))         # [[1],[2,3]]