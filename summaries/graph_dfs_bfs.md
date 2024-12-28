# Graph DFS BFS

Date: 12/26/2024
Yilin Zhao

## DFS (Depth First Traversal)

<details>
<summary>Recursive DFS</summary>

### Explanation

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node)  # Process the node
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

```

</details>



<details>
<summary>Iterative DFS Using Stack</summary>

### Explanation

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)  # Process the node
            visited.add(node)
            # Add neighbors to the stack in reverse order for correct traversal
            stack.extend(reversed(graph[node]))
```

</details>

## BFS Breadth First Traversal

<details>
<summary>BFS Using Queue</summary>

### Explanation

```python
from collections import deque

def bfs(graph, start):
    visited = set()  # Track visited nodes
    queue = deque([start])  # Start with the initial node
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)  # Process the node
            visited.add(node)  # Mark node as visited
            
            # Add neighbors of the current node to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

```

</details>

