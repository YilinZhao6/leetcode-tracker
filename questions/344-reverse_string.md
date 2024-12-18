# [344]. Reverse String

**Status**: [Solved ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2024-12-09

## Problem Statement

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
```
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Final Solution

```python
class Solution(object):
    def reverseString(self, s):
        left_pt=0
        right_pt=len(s)-1

        while left_pt<=right_pt:
            temp=s[left_pt]
            #swap the value of left and right pointers
            s[left_pt]=s[right_pt]
            s[right_pt]=temp

            left_pt+=1
            right_pt-=1
        
        return s
```

### Solution Explanation
Two pointers! Both go from two ends of the array, swap their values each time, and see when they meet each other. However, remember to decrement the value of right_pt instead of left_pt

## Previous Attempts

No previous attempts!

## Tags
#strings #two_pointers