# [62].  Unique Paths

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-21

## Problem Statement

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.


```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

## Final Solution

Fill the dp table out! This question is as easy.
```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*m for _ in range(n)]

        for j in range(n):
            if obstacleGrid[0][j]==0:
                dp[0][j]=1
            else:
                dp[0][j]=0
            
        for i in range(m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=1
            else:
                dp[i][0]=0
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j]=0
        
        return dp[m-1][n-1]

```

### Solution Explanation
Remember to return dp[m-1][n-1] in the end!

## Previous Attempts

No previous attempts


## Notes
- Backtracking Problem

## Tags
#backtracking