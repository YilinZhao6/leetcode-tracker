# [347]. Top K Frequent Elements

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-28

## Problem Statement

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

```
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

```

## Final Solution

First Solution Using Heap
```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    # Step 1: Count frequency of each element
    freq_map = Counter(nums)
    
    # Step 2: Use a heap to get k most frequent elements
    return heapq.nlargest(k, freq_map.keys(), key=freq_map.get)
```

Second Solution Using Bucket Sort
```python
from collections import Counter

def topKFrequent(nums, k):
    freq_map = Counter(nums)
    bucket = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in freq_map.items():
        bucket[freq].append(num)
    
    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result
```

## Tags
#BFS