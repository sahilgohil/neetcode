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

'''
Maximum depth of binary tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 
'''

def maxDepth(root: Optional[TreeNode]) -> int:
    def dfs(node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return 1 + max(dfs(node.left),dfs(node.right))
    return dfs(root)
