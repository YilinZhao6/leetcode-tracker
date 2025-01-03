# [987]. Vertical Order Traversal of Tree

**Status**: [Solved ✅]

**Difficulty**: [Hard]

**Last Attempted**: 2025-1-1

## Problem Statement

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

```
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
Example 3:


Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
```

## Final Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        node_levels=[]
        def dfs(node, level):
            if not node:
                return

            node_levels.append(level)
            
            dfs(node.left, level-1)
            dfs(node.right, level+1)

        def dfs_final(node, level, depth):
            if not node:
                return

            result[level-leftmost_level].append(node.val)
            result_depths[level-leftmost_level].append(depth)

            dfs_final(node.left, level-1, depth+1)
            dfs_final(node.right, level+1, depth+1)

        dfs(root,0)
        leftmost_level=min(node_levels)
        rightmost_level=max(node_levels)

        #then we have the leftmost_level, which is supposedly a negative number
        result = [[] for _ in range(rightmost_level - leftmost_level + 1)]
        result_depths = [[] for _ in range(rightmost_level - leftmost_level + 1)]
        #do dfs again, but this time add up the compensation for leftmost_level
        dfs_final(root,0,0)


        # Sort each column based on depths
        for i in range(len(result)):
            # Create pairs of (depth, val) and sort them
            pairs = list(zip(result_depths[i], result[i]))
            pairs.sort()  # This will sort by depth first, then by value
            # Update result with sorted values
            result[i] = [val for depth, val in pairs]
                    


            
        return result

```

## Tags
#tree_traversal