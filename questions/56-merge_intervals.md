# [Problem Number]. Problem Name

**Status**: [Solved ✅ | Partially Solved ⚠️ | In Progress 🚧 | Have Solution Idea 💡]

**Difficulty**: [Easy | Medium | Hard]

**Last Attempted**: YYYY-MM-DD

## Problem Statement

[Copy the problem statement here]

```
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Final Solution

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        def combineIntervals(array1, array2):
            newInterval=[]
            #in this case we don't need to merge
            if array1[1]<array2[0]:
                return -1
            #in rest of the case we should merge
            elif array1[0]<=array2[0]:  # Changed < to <= here
                newInterval.append(array1[0])
                if array1[1]<array2[1]:
                    newInterval.append(array2[1])
                else:
                    newInterval.append(array1[1])
                #by now we have created newInterval sucessfully
                return newInterval

            elif array1[0]>array2[0]:
                newInterval.append(array2[0])
                if array1[1]<array2[1]:
                    newInterval.append(array2[1])
                else:
                    newInterval.append(array1[1])
                return newInterval

        def check_array(points):
            if len(points) <= 1:
                return points
                
            result = []
            slow_pt = 0
            fast_pt = 1
            
            while fast_pt < len(points):
                merge_result = combineIntervals(points[slow_pt], points[fast_pt])
                if merge_result == -1:
                    #only add whey they have no overlapping intervals
                    result.append(points[slow_pt])
                    slow_pt = fast_pt
                else:
                    points[fast_pt] = merge_result  # Save merged result for next comparison
                    slow_pt = fast_pt
                fast_pt += 1
            
            # Don't forget to add the last interval we were working on
            result.append(points[slow_pt])
            return result

        intervals.sort(key=lambda x: x[0])
        return check_array(intervals)
```

### Solution Explanation
[Detailed explanation of your working solution, including:]
- Time Complexity: O(?)
- Space Complexity: O(?)
- Key Insights:
  - Point 1
  - Point 2

## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        def combineIntervals(array1, array2):
            newInterval=[]
            #in this case we don't need to merge
            if array1[1]<array2[0]:
                return -1
            #in rest of the case we should merge
            elif array1[0]<array2[0]:
                newInterval.append(array1[0])
                if array1[1]<array2[1]:
                    newInterval.append(array2[1])
                else:
                    newInterval.append(array1[1])
                #by now we have created newInterval sucessfully
                return newInterval

            elif array1[0]>array2[0]:
                newInterval.append(array2[0])
                if array1[1]<array2[1]:
                    newInterval.append(array2[1])
                else:
                    newInterval.append(array1[1])
                return newInterval

        def check_array(points):
            #now here is the main logic
            #the result array that we save combined intervals (or non-overlapping intervals in)
            result=[]

            #intialize two pointers
            slow_pt=0
            fast_pt=1

            while fast_pt<len(points):
                return_res=combineIntervals(points[slow_pt], points[fast_pt])
                #for non-overlapping intervals, I just put them in there
                if return_res==-1:
                    result.append(points[slow_pt])
                        #append the last element
                    if fast_pt==len(points)-1:
                        result.append(points[fast_pt])
                    #move pointers
                    slow_pt+=1
                    fast_pt+=1
                else:
                    #append the combined intervals
                    result.append(return_res)
                    #move pointers
                    slow_pt+=1
                    fast_pt+=1

                return result

        prev_result=intervals

        #potentially we need to check if there are overlapping intervals in result as well.
        while True:
            return_result=check_array(prev_result)
            if return_result==prev_result:
                return return_result
            else:
                prev_result=return_result
            
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

<details>
<summary>Attempt 2 - Failed ❌</summary>

```python
def second_attempt(nums):
    # Your second attempt code here
    pass
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
- Any additional insights
- Related problems
- Concepts to review

## Tags
#array #hash-table #etc