# [112]. Path Sum

**Status**: [Solved ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2024-12-23

## Problem Statement

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

```

## Final Solution

```python
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
        def dfs(node, current_sum):
            if not node:
                return False  # Base case: Reached a null node, no valid path
            
            current_sum += node.val  # Add the current node's value
            
            # Check if it's a leaf node and the sum equals targetSum
            if not node.left and not node.right:
                return current_sum == targetSum
            
            # Continue DFS on left and right children
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)
        
        return dfs(root, 0)

```

### Solution Explanation
Good Application of Sliding Windows!
## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
        def dfs(node, sum):
            if not node and sum==0:
                return 1
            if not node and sum!=0:
                return 0

            #some execution here
            sum-=node.val

            dfs(node.left, sum)
            dfs(node.right, sum)
        
        if dfs(root, targetSum)==1:
            return True
        else:
            return False
```


</details>

## Notes
NULL
## Tags
#dfs #trees