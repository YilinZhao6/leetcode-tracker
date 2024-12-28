# [216]. Number of Islands

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-26

## Problem Statement

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Final Solution

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        w=len(grid[0])
        h=len(grid)

        count=0

        def bfs(i,j):
            grid[i][j]='0'
            queue = deque([(i,j)])

            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            
            while queue:
                i,j = queue.popleft()
                for a,b in directions:
                    new_i, new_j=i+a, j+b
                    #need to add a limiting condition here!
                    if 0<=new_i<h and 0<=new_j<w:
                        if grid[new_i][new_j]=='1':
                            grid[new_i][new_j]='0'
                            queue.append((new_i,new_j))
                

        for i in range(h):
            for j in range(w):
                if grid[i][j]=='1':
                    count+=1
                    bfs(i,j)
        
        return count
```

## Tags
#graph_traversal