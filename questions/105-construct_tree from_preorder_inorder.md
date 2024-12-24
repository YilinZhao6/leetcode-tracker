# [105]. Construct Binary Tree from Preorder and Inorder Traversal

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-23

## Problem Statement

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]


```

## Final Solution
This question seems to be confusing. 
So for preorder, it's [root, left_tree, right_tree]. For inorder, it's [left_tree, root, right_tree].

The first element in preorder is the root. Then find the root in inorder. The slice before the root in inorder is the leftsubtree. The slice after the root is the rightsubtree.

```python
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
            
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root

```

### Solution Explanation

## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>


</details>

## Notes
NULL
## Tags
#tree_traversal