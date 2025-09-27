# ---------- TREE FUNDAMENTALS ----------

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1) Build and print tree
def print_tree(root: TreeNode):
    """Preorder print"""
    # TODO: if root is None return
    # TODO: print root.val
    # TODO: recurse left then right


# 2) Preorder traversal
def preorder(root: TreeNode) -> list[int]:
    res = []
    # TODO: fill with recursion
    return res


# 3) Tree depth
def max_depth(root: TreeNode) -> int:
    # TODO: if None return 0
    # TODO: return 1 + max(depth(left), depth(right))
    return 0


# 4) Level order traversal
from collections import deque
def level_order(root: TreeNode) -> list[list[int]]:
    levels = []
    # TODO: BFS with queue, collect level by level
    return levels


if __name__ == "__main__":
    # Tree:   1
    #        / \
    #       2   3
    root = TreeNode(1, TreeNode(2), TreeNode(3))

    print_tree(root)             # prints 1 2 3
    print(preorder(root))        # [1,2,3]
    print(max_depth(root))       # 2
    print(level_order(root))     # [[1],[2,3]]
