# Syntax Shortcuts

Date: 12/26/2024
Yilin Zhao

## Bracket Coordination

<details>
<summary>Bracket Coordination</summary>

### Explanation

```python
def isValid(self, s):
    if not s:
        return True
        
    stack = []
    brackets = {')':'(', ']':'[', '}':'{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
            
    return len(stack) == 0
```


</details>

## Sorting Counter Objects


<details>
<summary>Sort by VALUE in DESCENDING order</summary>

### Explanation

```python
from collections import Counter

counter = Counter({'apple': 4, 'banana': 2, 'orange': 5})

# Sort by values in descending order
sorted_by_value = sorted(counter.items(), key=lambda x: x[1], reverse=True)
print(sorted_by_value)
```

WILL PRINT OUT:

```python
[('orange', 5), ('apple', 4), ('banana', 2)]
```

</details>

<details>
<summary>Sort by VALUE in ASCENDING order</summary>

### Explanation

```python
# Sort by values in ascending order
sorted_by_value_asc = sorted(counter.items(), key=lambda x: x[1])
print(sorted_by_value_asc)
```

WILL PRINT OUT:

```python
[('banana', 2), ('apple', 4), ('orange', 5)]
```

</details>

## Building Graphs

<details>
<summary>Graph Construction by defaultdict</summary>

### Explanation

```python
from collections import defaultdict

def build_graph(numCourses, prerequisites):
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    return graph

graph = build_graph(4, [[1,0],[2,1],[3,2]])
print(graph)
```

It would print out:

```python
{
    0: [1],  # Course 0 → Course 1
    1: [2],  # Course 1 → Course 2
    2: [3]   # Course 2 → Course 3
}


```

</details>

<details>
<summary>Graph Construction using standard List objects</summary>

### Explanation

```python
def build_graph(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]  # List of empty lists
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    return graph

graph = build_graph(4, [[1,0],[2,1],[3,2]])
print(graph)

```

It would print out:

```python
[
    [1],  # Node 0 → 1
    [2],  # Node 1 → 2
    [3],  # Node 2 → 3
    []    # Node 3 has no outgoing edges
]



```

</details>

## list(zip)

<details>
<summary>From LC987</summary>

### Explanation

```python
        # Sort each column based on depths
        for i in range(len(result)):
            # Create pairs of (depth, val) and sort them
            pairs = list(zip(result_depths[i], result[i]))
            pairs.sort()  # This will sort by depth first, then by value
            # Update result with sorted values
            result[i] = [val for depth, val in pairs]
```

Pairs would look like:

```python
pairs = list(zip(result_depths[i], result[i]))
# pairs would look like:
# [(0, 3),  # (depth=0, value=3)
#  (1, 2),  # (depth=1, value=2)
#  (1, 4),  # (depth=1, value=4)
#  (2, 1)]  # (depth=2, value=1)
```

</details>

## Intialize a TreeNode object

<details>
<summary>From LC654</summary>

### Explanation

```python
        node=TreeNode()
```


</details>

## Find Modes Using Counter

<details>
<summary>From LC501</summary>

### Explanation

```python
        # Step 3: Find Maximum Frequency
        max_freq = max(counter.values())
        
        # Step 4: Collect All Values with Maximum Frequency
        modes = [val for val, freq in counter.items() if freq == max_freq]```


</details>