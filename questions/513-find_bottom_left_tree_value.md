# [112]. Path Sum

**Status**: [Solved ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2024-12-23

## Problem Statement

Given the root of a binary tree, return the leftmost value in the last row of the tree.

## Final Solution
An easy question! Just use template for tree level order traversal
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        if not root:
            return root

        queue=collections.deque([root])
        result=[]

        while queue:
            level=[]
            for _ in range(len(queue)):
                cur=queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            result.append(level)
        
        a=len(result)-1
        
        return result[a][0]
        

```

### Solution Explanation
Just apply the level order traversal!!

## Notes
NULL
## Tags
#level_order_traversal #trees