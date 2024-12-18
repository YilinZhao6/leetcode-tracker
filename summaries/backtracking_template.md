# Backtracking Code Template

## Overview
Hey, this page is about the template of backtracking in python! You could refer to this code sample snippet whenever you do backtracking problems.

## Common Variations

<details>
<summary>Backtrack Template</summary>

### Explanation

```python
def backtrack(candidates, path, result):
    # Base case - when we've found a valid solution
    if is_solution(path):
        result.append(path[:])  # Make a copy of current path
        return
    
    # Try each possible candidate
    for i in range(len(candidates)):
        # Skip invalid choices (pruning)
        if not is_valid(candidates[i], path):
            continue
            
        # Make a choice
        path.append(candidates[i])
        
        # Recursively try to find solutions with this choice
        backtrack(candidates, path, result)
        
        # Undo the choice (backtrack)
        path.pop()

# Usage
def solve_problem(candidates):
    result = []
    backtrack(candidates, [], result)
    return result
```

**Notes**
Yet to be implemented.

</details>

