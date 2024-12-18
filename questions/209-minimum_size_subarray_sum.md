# [209]. Minimize Size Subarray Sum

**Status**: [ Partially Solved ⚠️]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-09

## Problem Statement

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

```
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 
```

## Final Solution

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left_pt=0
        right_pt=0

        lengths=[]

        while right_pt<len(nums):
            current_sum=sum(nums[left_pt:right_pt+1])
            if current_sum==target:
                lengths.append(right_pt-left_pt+1)
                right_pt+=1 #you should move the pointer here, or it will stay in this case forever
            elif current_sum<target:
                right_pt+=1
            elif current_sum>target:
                lengths.append(right_pt-left_pt+1)
                left_pt+=1


        return min(lengths) if lengths else 0
            
                



```

### Solution Explanation
Hey, this solution uses two pointers to implement a sliding window. 

It's partially done becuase it exceeds time limit for some scenarios. Maybe I shouldn't calculate current sum every time!

## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left_pt=0
        right_pt=0

        lengths=[]

        while right_pt<len(nums):
            if sum(nums[left_pt:right_pt+1])==target:
                lengths.append(right_pt-left_pt)
            elif sum(nums[left_pt:right_pt+1])<target:
                right_pt+=1
            elif sum(nums[left_pt:right_pt+1])>target:
                left_pt+=1

        return min(lengths) if lengths else 0
```

### What Went Wrong
- Issue description
  Time limit exceeded
- Why it failed:
I should move the pointers, even if the sums are equal! This is the main reason
</details>

## Notes
- Any additional insights
- Related problems
- Concepts to review

## Tags
#sliding_window