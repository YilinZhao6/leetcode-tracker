# [643]. Maximum Average Subarray I

**Status**: [Solved ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2024-12-21

## Problem Statement

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

```
Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
```

## Final Solution

```python
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums:
            return nums
        #fill the sliding window for inital elements
        queue=deque()
        curr_sum=0
        for i in range(k):
            queue.append(nums[i])
            curr_sum+=nums[i]

        max_sum=curr_sum

        for i in range(k,len(nums)):
            curr_sum-=queue.popleft()
            queue.append(nums[i])
            curr_sum+=nums[i]
            max_sum=max(max_sum, curr_sum)

        return max_sum/float(k)

```

### Solution Explanation
Good Application of Sliding Windows!
## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>

```python
None
```


</details>

## Notes
NULL
## Tags
#sliding_windows #array