# [63].  Unique Paths-II

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-21

## Problem Statement

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

## Final Solution

For the intialization in row/column, this is different from unique paths I. It is depdenent on the previous block as well. I made this mistake.
```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        #add edge case control here

        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        if m==0 and n==0:
            return 0

        dp=[[0]*n for _ in range(m)]
        if obstacleGrid[0][0]==1:
            dp[0][0]==0
        else:
            dp[0][0]=1
        #initialize boundaries
        for i in range(1,m):
            if obstacleGrid[i][0]==1:
                dp[i][0]=0           
            else:
                dp[i][0]=dp[i-1][0]

        for j in range(1,n):
            if obstacleGrid[0][j]==1:
                dp[0][j]=0
            else:
                dp[0][j]=dp[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]

```

### Solution Explanation
Remember to return dp[m-1][n-1] in the end!

## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]

        if obstacleGrid[0][0]==1:
            return 0
        

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
- Backtracking Problem

## Tags
#backtracking