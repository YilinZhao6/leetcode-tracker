# [226]. Invert Binary Tree

**Status**: [Solved ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2024-12-8

## Problem Statement

Given the root of a binary tree, invert the tree, and return its root.


```
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
```

## Final Solution

```python
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        #handle edge cases
        if not root:
            return None

        def swapchild(node):
            left_node=node.left
            right_node=node.right

            node.left=right_node
            node.right=left_node
        
        def dfs(node):
            if node is None:
                return
            
            swapchild(node)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return root
        
```

Solution Version Jan 18

```python
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def invert_nodes(node):
            if not node:
                return

            left_child=node.left
            right_child=node.right
            node.left=right_child
            node.right=left_child

            invert_nodes(node.left)
            invert_nodes(node.right)

        invert_nodes(root)

        return root  
```
### Solution Explanation
Two functions. One is to perform swapchild, the other is to traverse all children of a tree to perform swap child.

## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>

```python
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        #handle edge cases
        if not root:
            return None

        def swapchild(node):
            if node.right and node.left:
                left_node=node.left
                right_node=node.right

                node.left=right_node
                node.right=left_node
        
        def dfs(node):
            if node is None:
                return
            
            swapchild(node)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return root
        
```

### What Went Wrong
- Why it failed: 
    ```if node.right and node.left:```
    This line has issues. In fact, I don't need to check at all!

</details>

## Notes
Easy question! You mastered it!

## Tags
#binary_tree