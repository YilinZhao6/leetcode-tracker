# [77].  Squares of a Sorted Array

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-8

## Problem Statement

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

```
Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
```

## Final Solution

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(candidates, minimum_candidate, target_length, path, result):
            #if length of the current combination (path) equals to 2, append this combination to the result array!
            if len(path)==target_length:
                #put the path that fit into result[]
                result.append(path[:])

            for i in range(minimum_candidate, len(candidates)):
                path.append(candidates[i])

                backtrack(candidates, i+1, target_length, path, result)

                path.pop()
            
        #here's the main function
        result=[]
        array=[]
        #create the array
        for i in range (1, n+1):
            array.append(i)
        #the backtracking function modifies the result
        backtrack(array, 0, k, [], result)
        return result

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