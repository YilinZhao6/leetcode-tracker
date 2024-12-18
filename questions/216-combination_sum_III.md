# [216]. Combination Sum

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-09

## Problem Statement

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

```
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
```

## Final Solution

```python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        #add argument variables as needed
        def backtrack(candidates, min_candidate, number_candidate, target, path, result):
            #if we have two conditions, then the stopping condition should also be two nested if conditionals
            if len(path)==number_candidate:
                if sum(path)==target:
                    result.append(path[:])
                
                #don't forget to return
                return
            
            #for pruning (which is not necessary, but makes the code more efficient)
            if sum(path)>target:
                return

            for i in range(min_candidate, 10-number_candidate+len(path)+1):
                path.append(i)
                backtrack(candidates, i+1, number_candidate, target, path, result)
                path.pop()

        result=[]
        array=[]
        #create array
        for i in range (1,10):
            array.append(i)
        
        #call the backtracking algorithm
        backtrack(array, 1, k, n, [], result)

        return result

```

### Solution Explanation

The keypoints are all written in comments. Note that the stopping condition of this backtracking contains two conditions--one is ```len(nums)==number_candidate```, and ```sum(path)==target```. Also, take note of the pruning, and how we add more argument to the base model of the backtracking template.

## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>

```python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        #add argument variables as needed
        def backtrack(candidates, min_candidate, number_candidate, target, path, result):

            if sum(path)==target:
                result.append(path[:])
            
            for i in range(min_candidate, 10-number_candidate+len(path)+1):
                path.append(i)
                backtrack(candidates, i+1, target, path, result)
                path.pop()

        result=[]
        array=[]
        #create array
        for i in range (1,10):
            array.append(i)
        
        #call the backtracking algorithm
        backtrack(array, 1, k, n, [], result)

        return result

```

### What Went Wrong
- Issue description
- Failed test case:
```
Input: 
Expected:
Actual:
```
- Why it failed: [Explanation]
</details>

## Notes


## Tags
#backtracking