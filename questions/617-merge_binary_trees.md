# [617]. Merge Two Binary Trees

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-30

## Problem Statement

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

```

Example 1:


Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.
Example 2:


Input: nums = [3,2,1]
Output: [3,null,2,null,1]
```

## Final Solution

```python
# Definition for a binary tree node.
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
    
        def fillnodes(node1, node2, root=False):
            if root:
                root = TreeNode()
                if node1:
                    root.val += node1.val
                if node2:
                    root.val += node2.val
                root.left = fillnodes(node1.left if node1 else None, node2.left if node2 else None)
                root.right = fillnodes(node1.right if node1 else None, node2.right if node2 else None)
                return root

            if node1 and node2:
                node = TreeNode()
                node.val = node1.val + node2.val
                node.left = fillnodes(node1.left, node2.left)
                node.right = fillnodes(node1.right, node2.right)
                return node

            elif node1:
                node = TreeNode()
                node.val = node1.val
                node.left = fillnodes(node1.left, None)
                node.right = fillnodes(node1.right, None)
                return node

            elif node2:
                node = TreeNode()
                node.val = node2.val
                node.left = fillnodes(None, node2.left)
                node.right = fillnodes(None, node2.right)
                return node

            # Both nodes are None
            else:
                return None

        if not root1 and not root2:
            return None  # Both roots are None, return None
        
        return fillnodes(root1, root2, True)

```

## Tags
#recursion