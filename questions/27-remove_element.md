# [27]. Remove Element

**Status**: [Solved ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2024-12-8

## Problem Statement

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

```
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## Final Solution

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #use two pointers, one slow one fast:
        slow_pt=0 #also our return val, k
        fast_pt=0


        while fast_pt<len(nums):
            if nums[fast_pt]==val:
                #move fastpt if values match, do not move slowpt, or assign value
                fast_pt+=1
            else:
                #assign val of fast_pt to slow_pt. move then both forward
                nums[slow_pt]=nums[fast_pt]
                slow_pt+=1
                fast_pt+=1
                
        #return original modified nums
        return slow_pt

        
```

### Solution Explanation
TWO pointers! I've done this problem for multiple times. The condition for while loop is: fast pointer does not go out of the array.

Fast pointer points to the index to be checked! Slow pointer points to the index where we are going to put the right value in.

Two scenarios:
1. Fast_pointer=target
   Move fast pointer forward. Do not move slow pointer, or assign values.
2. Fast_pointer!=target
   Assign value of fast pointer to slow pointer. Move them both forward.

## Previous Attempts

No Failed Attempts

## Notes
NULL

## Tags
#two_pointers