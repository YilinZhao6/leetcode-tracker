# [239]. Sliding Window Maximum

**Status**: [Solved ✅]

**Difficulty**: [Hard]

**Last Attempted**: 2024-12-28

## Problem Statement

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
```
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]

```

## Final Solution

Keep the value in sliding window decreasing!
```python
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        
        n = len(nums)
        result = []
        dq = deque()  # Store indices of nums in increasing order
        
        for i in range(n):
            # Remove indices that are out of the sliding window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # Append the max (front of the deque) to the result once the window is fully formed
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
```

## Tags
#Sliding Window