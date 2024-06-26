from typing import Optional,List
import collections

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

'''
Same Tree
'''
def isSameTree( p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False

    return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)


'''
IsSubTree

'''
def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
    def dfs(root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            if isSameTree(root,subRoot):
                return True
        return dfs(root.left,subRoot) or dfs(root.right,subRoot)
    return dfs(root,subRoot)


'''
Lowest Common Ancestor

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    curr = root
    while curr:
        if p.val>curr.val and q.val>curr.val:
            curr = curr.right
        elif p.val<curr.val and q.val<curr.val:
            curr = curr.left
        else:
            return curr
    return root


'''
Level Order Traversal
'''

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        res = []
        q.append(root)
        while q:
            currList = []
            for _ in range(len(q)):
                node = q.popleft()
                currList.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(currList)
        return res


'''
Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res = []
    q = collections.deque()
    q.append(root)
    while q:
        x = len(q)-1
        for i in range(len(q)):
            node = q.popleft()
            if i == x:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res


'''
Good Nodes in binary tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''
def goodNodes(root: TreeNode) -> int:
    if not root:
        return 0
    res = [0]
    def dfs(root, preMax):
        if not root:
            return
        
        currVal = root.val
        if currVal >= preMax:
            res[0] += 1
            preMax = max(currVal,preMax)
        
        dfs(root.left,preMax)
        dfs(root.right,preMax)
    dfs(root,root.val)
    return res[0]

'''
Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
def isValidBST(root: Optional[TreeNode]) -> bool:
    def dfs(root, left, right):
        if not root:
            return True
        if not (root.val < right and root.val > left):
            return False
        
        return (dfs(root.left,left,root.val)# left call leave the left as it is
            and dfs(root.right,root.val,right)) # leave the right as it is
    return dfs(root,float('-inf'),float('inf'))

'''
Kth smallest element in the BST

'''
def kthSmallest( root: Optional[TreeNode], k: int) -> int:
    res = [0,k]
    
    def dfs(node):
        if not node:
            return

        dfs(node.left)
        res[1] -= 1
        if res[1] == 0:
            res[0] = node.val
            return
        dfs(node.right)
    dfs(root)
    return res[0]


'''
Construct Binary Tree from preorder and inorder
'''
def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0]) # just index for all in the left tree and right tree
    root.left = buildTree(preorder[1:mid+1],inorder[:mid])
    root.right = buildTree(preorder[mid+1:],inorder[mid+1:])
    return root


'''
Max Path Sum
'''
def maxPathSum( root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    res = [root.val]
    def dfs(root):
        if not root:
            return 0
        
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        leftMax = max(leftMax,0)
        rightMax = max(rightMax,0)
        currMax = root.val + leftMax + rightMax
        
        # calculate the max pathsum if we split
        res[0] = max(res[0],currMax)


        return root.val + max(leftMax,rightMax)#return the possible max sum from this node
    dfs(root)
    return res[0]


'''
Serialize and Deserialize
'''

class Codec:

    def serialize(self, root):
        res = []
        def preOrder(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return ','.join(res)
    def deserialize(self, data):
        vals = data.split(',')
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

