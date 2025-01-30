# [101]. Symmetric Tree

**Status**: [Solved ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2024/12/8

## Problem Statement

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


```
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
```

## Final Solution

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_two_nodes_equal(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            elif node1.val==node2.val:
                return check_two_nodes_equal(node1.left, node2.right) and check_two_nodes_equal(node1.right, node2.left)
            elif node1.val!=node2.val:
                return False

        left_tree_root=root.left
        right_tree_root=root.right

        return check_two_nodes_equal(left_tree_root, right_tree_root)
        
```

Jan 18 Solution

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_symmetric(node1,node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False

            if node1.val!=node2.val:
                return False
            
            return check_symmetric(node1.left,node2.right) and check_symmetric(node1.right,node2.left)
        
        return check_symmetric(root.left,root.right)
        
```

### Solution Explanation
1. Remember to compare the .val of two nodes instead of two nodes directly!
2. return only return to the upper level (like jr $ra in MIPS), so ```                return check_two_nodes_equal(node1.left, node2.right) and check_two_nodes_equal(node1.right, node2.left)```
3. Understanding of recursive functions!
   
## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_two_nodes_equal(node1, node2):
            if node1 is None and node2 is None:
                return
            elif node1==node2:
                check_two_nodes_equal(node1.left, node2.right)
                check_two_nodes_equal(node1.right, node2.left)
            elif node1!=node2:
                return False

        left_tree_root=root.left
        right_tree_root=root.right

        check_two_nodes_equal(left_tree_root, right_tree_root)

        return True

        
```

### What Went Wrong
1. Remember to compare the .val of two nodes instead of two nodes directly!
2. return only return to the upper level (like jr $ra in MIPS), so ```                return check_two_nodes_equal(node1.left, node2.right) and check_two_nodes_equal(node1.right, node2.left)```
3. Understanding of recursive functions!

</details>

## Notes
This one you are about to make it!

## Tags
#binary_tree