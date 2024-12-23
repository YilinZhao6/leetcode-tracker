# [70].  Climbing Stairs

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-8

## Problem Statement

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


```
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Final Solution

buttom-up approach
```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def recursive(n, memo={}):
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = recursive(n-1, memo) + recursive(n-2, memo)
            return memo[n]
        
        return recursive(n)

```

### Solution Explanation
Time Complexity: O(n^k)
Space Complexity: O(k)

By refering to the backtracking template, you can solve this problem easily!

Remember that the array is not given first. You need to create the array. Note that you should also set minimum candidate as well (add as another variablr in the backtracking process)

For backtracking, we create an empty result ifrst, and then let an worker (backtracking) algorithm to work on this empty array.

## Previous Attempts

No previous attempts


## Notes
- Backtracking Problem

## Tags
#backtracking