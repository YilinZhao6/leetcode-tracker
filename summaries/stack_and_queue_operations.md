# Stack And Queue Operations

Date: 12/26/2024
Yilin Zhao

<details>
<summary>Stack Operations</summary>

### Explanation

```python
stack = []
stack.append(1)  # Push 1
stack.append(2)  # Push 2
print(stack[-1])  # Peek: 2
print(stack.pop())  # Pop: 2
print(stack)  # [1]

```

</details>

<details>
<summary>Queue Operations</summary>

### Explanation

```python
from collections import deque

dq = deque()
dq.append(1)         # Add to end: [1]
dq.appendleft(2)     # Add to front: [2, 1]
print(dq)           # Output: deque([2, 1])
print(dq.popleft())  # Remove from front: 2
print(dq.pop())      # Remove from end: 1
print(dq)           # Output: deque([])


```

</details>
