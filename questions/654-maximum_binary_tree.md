# [654]. Maximum Binary Tree

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-30

## Problem Statement

You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

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
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None  # Return None for an empty list (base case)
        
        root = TreeNode()  # Create an empty root node
        
        def build_tree(node, lst):
            if not lst:
                return
            
            max_val = max(lst)  # Find maximum value
            max_index = lst.index(max_val)  # Find index of maximum value
            
            left_list = lst[:max_index]  # Left sublist
            right_list = lst[max_index + 1:]  # Right sublist
            
            node.val = max_val  # Assign max value to the current node
            
            if left_list:
                node.left = TreeNode()
                build_tree(node.left, left_list)  # Recursively build left subtree
                
            if right_list:
                node.right = TreeNode()
                build_tree(node.right, right_list)  # Recursively build right subtree
        
        build_tree(root, nums)  # Start building from the root with the full list
        return root

```

## Tags
#recursion