# Heap Hint

Date: 12/21/2024
Yilin Zhao

## Recursive Traversal

<details>
<summary>Some basic heap commands</summary>

### Explanation

```python
from heapq import heappush, heappop, heapify

# Creating a heap
heap = []

# Adding elements (heappush)
heappush(heap, 5)  # heap = [5]
heappush(heap, 3)  # heap = [3, 5]
heappush(heap, 7)  # heap = [3, 5, 7]
heappush(heap, 1)  # heap = [1, 3, 5, 7]

# Get minimum element without removing (peek)
min_element = heap[0]  # returns 1

# Remove and return minimum element (heappop)
smallest = heappop(heap)  # returns 1, heap = [3, 5, 7]

# Convert existing list to heap
numbers = [5, 3, 7, 1]
heapify(numbers)  # numbers is now a valid heap [1, 3, 7, 5]

# For max heap, you can use negative numbers (python have min heap by default)
max_heap = []
heappush(max_heap, -5)  # Push -5 to get 5
heappush(max_heap, -3)  # Push -3 to get 3
largest = -heappop(max_heap)  # Pop and negate to get largest

#the nlargest function
import heapq

heapq.nlargest(n, iterable, key=None)

#basic usage:
import heapq

nums = [1, 8, 3, 5, 7, 2]
largest_three = heapq.nlargest(3, nums)
print(largest_three)


#advanced usage:
import heapq

students = [
    ('Alice', 85),
    ('Bob', 92),
    ('Charlie', 88),
    ('David', 90)
]

# Get top 2 students with the highest scores
top_students = heapq.nlargest(2, students, key=lambda student: student[1])
print(top_students)


```

**Notes**
none

</details>


<details>
<summary>Remove From Heap</summary>

### Explanation

```python
def remove(value):
    # If value is in small_heap
    if value <= small_heap[0]:
        removed[value] = removed.get(value, 0) + 1
        # Rebalance if necessary
        while small_heap and removed.get(small_heap[0], 0) > 0:
            removed[small_heap[0]] -= 1
            heappop(small_heap)
    # If value is in large_heap
    else:
        removed[-value] = removed.get(-value, 0) + 1
        # Rebalance if necessary
        while large_heap and removed.get(-large_heap[0], 0) > 0:
            removed[-large_heap[0]] -= 1
            heappop(large_heap)
```

**Notes**
none

</details>
