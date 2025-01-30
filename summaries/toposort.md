# TOPOSORT Template
Date: 12/8/2024
Yilin Zhao

<details>
<summary>TOPOSORT Template</summary>

### Explanation

```python
        # Step 4: Topological Sorting using BFS (Kahn’s Algorithm)
        queue = deque([char for char in indegree if indegree[char] == 0])
        result = []
        
        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
```

**Notes**
Change queue if needed

</details>

