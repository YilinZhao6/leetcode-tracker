# [199]. Binary Tree Right Side View

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-30

## Problem Statement

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


## Final Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        queue=deque([root])
        right_side=[]

        while queue:
            level=[]
            for _ in range(len(queue)):
                cur=queue.popleft()
                level.append(cur)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            right_side.append(level[-1].val)
        
        return right_side
            
```

## Tags
#BFS_level_order