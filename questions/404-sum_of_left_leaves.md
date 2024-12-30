# [404]. Sum of Left Leaves

**Status**: [Solved ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2024-12-28

## Problem Statement

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

```
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0

```

## Final Solution

First Solution DFS (my template)
```python
def dfs_recursive(node, is_left):
    """
    Recursive DFS for Sum of Left Leaves (Leetcode 404)
    
    :param node: Current TreeNode being visited
    :param is_left: Boolean indicating if this node is a left child
    :return: Sum of left leaves in the subtree
    """
    if not node:
        return 0
    
    # Check if this node is a leaf and a left child
    if not node.left and not node.right and is_left:
        return node.val
    
    # Recurse for left and right subtrees
    left_sum = dfs_recursive(node.left, True)
    right_sum = dfs_recursive(node.right, False)
    
    return left_sum + right_sum


def sumOfLeftLeaves(root):
    return dfs_recursive(root, False)  # Root is not considered as a left child

```

Second Solution Using BFS (use the queue template)
```python
from collections import deque

def sumOfLeftLeaves(root):
    if not root:
        return 0
    
    total_sum = 0
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        # Check the left child
        if node.left:
            # Check if it's a leaf node
            if not node.left.left and not node.left.right:
                total_sum += node.left.val
            else:
                queue.append(node.left)
        
        # Add the right child to the queue (no special condition needed)
        if node.right:
            queue.append(node.right)
    
    return total_sum
```

## Tags
#BFS #DFS