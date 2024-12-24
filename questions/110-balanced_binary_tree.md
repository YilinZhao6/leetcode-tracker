# [110]. Balanced Binary Tree

**Status**: [Cannot Pass Some Test Cases ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2024-12-23

## Problem Statement

Given a binary tree, determine if it is height-balanced.

## Final Solution


```python
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True

        depths=[]
        def dfs_recursive(node, height):

            if not node:
                return
            
            if not node.left and not node.right:
                height+=1
                depths.append(height)
            
            height+=1

            dfs_recursive(node.left, height)   # Visit left subtree
            dfs_recursive(node.right, height)  # Visit right subtree

        dfs_recursive(root,0)

        if len(depths)==1:
            if depths[0]==1:
                return True
            else:
                return False

        if max(depths)-min(depths)<2:
            return True
        else:
            return False

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