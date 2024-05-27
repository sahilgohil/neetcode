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


'''
Diameter of a tree
'''
def diameterOfBinaryTree( root: Optional[TreeNode]) -> int:
    res = [0]
    def dfs(root):
        if not root:
            return -1 # height is negative if the root is null and 0 if the root is leaft node
        left = dfs(root.left)
        right = dfs(root.right)
        res[0] = max(res[0],2 + left + right) # calculate the diameter at the particular node
        return 1 + max(left,right) # return the max height at the particular node
    dfs(root)
    return res[0]

'''
110. Balanced Binary Tree
Given a binary tree, determine if it is 
height-balanced
.
'''
def isBalanced(root: Optional[TreeNode]) -> bool:

    def dfs(root):
        # if the root is empty then return the tree is balanced and height is -1
        if not root:
            return [True, -1]
        # go to the end of left and right tree
        left = dfs(root.left)
        right = dfs(root.right)
        # check if the subtree is balanced
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        # return the answer with the maxheight at the node
        return [balanced, 1 + max(left[1],right[1])]
    return dfs(root)[0]# return the answer