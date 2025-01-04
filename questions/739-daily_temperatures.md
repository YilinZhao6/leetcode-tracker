# [739]. Daily Temperatures

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-30

## Problem Statement

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

```
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
```



## Final Solution

```python
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []
        
        for i, temperature in enumerate(temperatures):
            # Ensure the stack is not empty before accessing the top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                start_date = stack.pop()
                result[start_date] = i - start_date
            # Push the current index onto the stack
            stack.append(i)
        
        return result
```

## Tags
#Monotonic Stack