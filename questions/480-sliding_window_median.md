# [480]. Sliding Window Median

**Status**: [Partially Solved ⚠️]

**Difficulty**: [Hard]

**Last Attempted**: 2024-12-21

## Problem Statement

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

```
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
```

## Final Solution

```python
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        if not nums:
            return nums
            
        small_heap = []  # max heap (negatives)
        large_heap = []  # min heap
        removed = {}
        counts = [0, 0]  # [small_size, large_size]

        def add_element(value):
            if not small_heap or value > -small_heap[0]:
                heappush(large_heap, value)
                counts[1] += 1
            else:
                heappush(small_heap, -value)
                counts[0] += 1
                
            # balancing based on valid sizes
            while counts[0] > counts[1] + 1:
                element = -heappop(small_heap)
                heappush(large_heap, element)
                counts[0] -= 1
                counts[1] += 1
            while counts[1] > counts[0] + 1:
                element = heappop(large_heap)
                heappush(small_heap, -element)
                counts[1] -= 1
                counts[0] += 1

        def remove(value):
            if not small_heap or value > -small_heap[0]:
                removed[value] = removed.get(value, 0) + 1
                counts[1] -= 1
            else:
                removed[value] = removed.get(value, 0) + 1
                counts[0] -= 1
            
            # Clean up heaps if needed
            while small_heap and removed.get(-small_heap[0], 0) > 0:
                removed[-small_heap[0]] -= 1
                heappop(small_heap)
            while large_heap and removed.get(large_heap[0], 0) > 0:
                removed[large_heap[0]] -= 1
                heappop(large_heap)

        def get_med():
            # Clean up heaps first
            while small_heap and removed.get(-small_heap[0], 0) > 0:
                removed[-small_heap[0]] -= 1
                heappop(small_heap)
            while large_heap and removed.get(large_heap[0], 0) > 0:
                removed[large_heap[0]] -= 1
                heappop(large_heap)
                
            if counts[0] == counts[1]:
                return 0.5 * (-small_heap[0] + large_heap[0])
            elif counts[0] > counts[1]:
                return -small_heap[0]
            else:
                return large_heap[0]

        # add initial elements
        for i in range(k):
            add_element(nums[i])
        
        medians = [get_med()]
        
        # slide window
        for i in range(k, len(nums)):
            add_element(nums[i])
            remove(nums[i-k])
            medians.append(get_med())
        
        return medians
```

### Solution Explanation
This code failed on testcase 27/43 of leetcode problem 480

## Previous Attempts

<details>
<summary>Attempt 1 - Don't have removal implemented</summary>

```python
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        #should be a max heap
       small_heap=[]
       #should be a min heap
       large_heap=[]

       def add_element(value):
            #then it should be in large heap
            if value>small_heap[0]:
                heappush(large_heap,-value):
            #it should be in small heap
            else:
                heappush(small_heap, value)
            #balancing the heap:
            if len(small_heap)>len(large_heap)+1:
                element=heappop(small_heap)
                heappush(large_heap,element)
            if len(large_heap)>len(small_heap)+1:
                element=heappop(large_heap)
                heappush(small_heap,element)


        #add initial element to heap
        heappush(small_heap, nums[0])
    
        #push rest of the elements on to heap until sliding window fulls
        for i in range(1,k):
            add_element(nums[i])
        
        #now, the sliding window it full. We add new elements to it, and calculate median.
        pointer=k
        medians=[]
        while k<len(nums[i]):
            #push element
            add_element(nums[pointer])
            #pending function to remove element
            remove()
            #calculate median
            if len(large_heap)=len(small_heap):
                median=0.5*(small_heap[0]-large_heap[0])
            if len(large_heap)=len(small_heap+1):
                median=small_heap[0]
            if len(large_heap)+1=len(small_heap):
                median=-large_heap[0]
            medians.append(median)
            k+=1
        
        return median
            
```

### What Went Wrong
None
</details>

<details>
<summary>Attempt 2 - Failed ❌</summary>

```python
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        if not nums:
            return nums
            
        # should be a max heap (will store negatives of smaller numbers)
        small_heap = []
        # should be a min heap (will store larger numbers as is)
        large_heap = []
        removed = {}
        medians=[]

        def add_element(value):
            # if value is greater than largest in small_heap
            if small_heap and value > -small_heap[0]:
                heappush(large_heap, value)
            # it should be in small_heap
            else:
                heappush(small_heap, -value)  # negate for max heap
            # balancing the heap:
            while len(small_heap) > len(large_heap) + 1:
                element = -heappop(small_heap)  # un-negate when moving
                heappush(large_heap, element)
            while len(large_heap) > len(small_heap) + 1:
                element = heappop(large_heap)
                heappush(small_heap, -element)  # negate when moving to small

        def remove(value):
            # If value is in small_heap
            if value <= -small_heap[0]:
                removed[-value] = removed.get(-value, 0) + 1
                while small_heap and removed.get(-small_heap[0], 0) > 0:
                    removed[-small_heap[0]] -= 1
                    heappop(small_heap)
            # If value is in large_heap
            else:
                removed[value] = removed.get(value, 0) + 1
                while large_heap and removed.get(large_heap[0], 0) > 0:
                    removed[large_heap[0]] -= 1
                    heappop(large_heap)

        # add initial element to heap
        heappush(small_heap, -nums[0])  # negate initial element
    
        for i in range(1, k):
            add_element(nums[i])
        
        #calculate first median
        if len(large_heap) == len(small_heap):
            median = 0.5 * (-small_heap[0] + large_heap[0])
        elif len(large_heap) == len(small_heap) + 1:
            median = large_heap[0]
        else:
            median = -small_heap[0]
        medians.append(median)
        
        pointer = k
        while pointer < len(nums):
            add_element(nums[pointer])
            remove(nums[pointer-k])
            
            if len(large_heap) == len(small_heap):
                median = 0.5 * (-small_heap[0] + large_heap[0])
            elif len(large_heap) == len(small_heap) + 1:
                median = large_heap[0]
            elif len(large_heap) + 1 == len(small_heap):
                median = -small_heap[0]
            medians.append(median)
            pointer += 1
        
        return medians
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
Heap Basic Usage:
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

# For max heap, you can use negative numbers
max_heap = []
heappush(max_heap, -5)  # Push -5 to get 5
heappush(max_heap, -3)  # Push -3 to get 3
largest = -heappop(max_heap)  # Pop and negate to get largest

```


## Tags
#sliding_window #heap