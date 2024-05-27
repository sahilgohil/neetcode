from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
Invert the binary Tree

Given the root of a binary tree, invert the tree, and return its root.
'''
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def helper(node):
        if not node:
            return
        tmp = node.right
        node.right = node.left
        node.left = tmp
        helper(node.left)
        helper(node.right)
    helper(root)
    return root
