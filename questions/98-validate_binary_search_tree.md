# [617]. Merge Two Binary Trees

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-30

## Problem Statement

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.



## Final Solution

```python
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_tree(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            
            if not (lower < node.val < upper):
                return False
            
            return (check_tree(node.left, lower, node.val) and
                    check_tree(node.right, node.val, upper))
        
        return check_tree(root)


```

## Tags
#recursion