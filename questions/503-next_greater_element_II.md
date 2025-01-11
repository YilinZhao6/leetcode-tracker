# [503]. Next Greater Element II

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2025-01-02

## Problem Statement

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

```Example 1:
Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

```



## Final Solution

```python
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        next_greater = {}
        stack = []
        result = [-1] * len(nums)  # Initialize result with -1

        # Loop twice to simulate circular array
        for i in range(2 * len(nums)):
            current_index = i % len(nums)  # Wrap around using modulo

            while stack and nums[current_index] > nums[stack[-1]]:
                element_index = stack.pop()
                result[element_index] = nums[current_index]

            if i < len(nums):  # Only push indices from the first pass
                stack.append(current_index)
        
        return result

```

## Tags
#monotonic_stack