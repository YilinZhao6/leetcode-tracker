# [977].  Squares of a Sorted Array

**Status**: [Solved ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2024-12-8

## Problem Statement

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
```
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

## Final Solution

```python
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Initialize two pointers as well, but going from two ends of the array. Square them, then insert.
        slow_pt=0
        fast_pt=len(nums)-1


        #initialize the result array, where we'll store the values to (and finally reverse it)
        result=[]

        # two pointers need to overlap!! becuase we only put one value in to array.
        while slow_pt<=fast_pt:
            #Find the squared values
            f_pt_val=nums[fast_pt]**2
            s_pt_val=nums[slow_pt]**2

            if f_pt_val>=s_pt_val:
                result.append(f_pt_val)
                fast_pt-=1
            else:
                result.append(s_pt_val)
                slow_pt+=1

        #now we have all the values inserted in place
        result.reverse()
        return result
```

### Solution Explanation
Time Complexity: O(n) - we traverse the array once with the two pointers
Space Complexity: O(n) - we create a new array result to store n squared numbers

## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>

```python
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Initialize two pointers as well, but going from two ends of the array. Square them, then insert.
        slow_pt=0
        fast_pt=len(nums)-1


        #initialize the result array, where we'll store the values to (and finally reverse it)
        result=[]

        while slow_pt<fast_pt:
            #Find the squared values
            f_pt_val=nums[fast_pt]**2
            s_pt_val=nums[slow_pt]**2

        if f_pt_val>=s_pt_val:
            result.append(f_pt_val)
            fast_pt-=1
        else:
            result.append(s_pt_val)
            slow_pt+=1

        #now we have all the values inserted in place
        result=reverse(result)

        return result
```

### What Went Wrong
Time Limit Exceeded

```
Last Executed Input
Open Testcase
nums =
[-4,-1,0,3,10]
```
- Why it failed: 

Main Issue:

The condition slow_pt<fast_pt is wrong!
When pointers meet at middle element (slow_pt = fast_pt), the loop stops
Middle element never gets processed
Result array is incomplete
When trying to reverse an incomplete array, it keeps running, causing Time Limit Exceeded

Secondary Issues:

Wrong indentation of the if statement (it was outside the while loop)
Using reverse() function instead of result.reverse() method
These would have caused errors even if the loop worked correctly

</details>


## Notes
- Another two pointers problem

## Tags
#two_pointers