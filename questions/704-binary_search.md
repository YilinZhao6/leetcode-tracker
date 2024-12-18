# [704]. Binary Search

**Status**: [Solved ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2024-12-8

## Problem Statement

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

```
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

## Final Solution

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right=0, len(nums)-1
        while left<=right:
            mid=left+(right-left)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        
        return -1
```

### Solution Explanation
This problems basically asks us to writeup the binary search algorithm. 

Keypoints:
1. left should be initialized as 0, right initialized as len(nums)-1 (I made an mistake here)
2. Condition of while loop should be while left<=right, for the following reason:
   When left == right, we're looking at the last possible position where our target could be
   Using left < right would stop before checking this last position
   Therefore, we need left <= right to ensure we check ALL possible positions, including when the search has narrowed down to a single element.
3. When comparing target with nums[mid], it should be > (elif), <(elif)

## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right=0, len(nums)
        while left<=right:
            mid=left+(right-left)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        
        return -1
```

### What Went Wrong
I initiallized right to len(nums), but not len(nums)-1. This is a stupid mistake.
</details>

## Notes
NULL
## Tags
#binary_search