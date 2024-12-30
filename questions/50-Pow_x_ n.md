# [50]. Pow_x_n

**Status**: [Solved ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-30

## Problem Statement

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

```

Code


Testcase
Testcase
Test Result
50. Pow(x, n)
Solved
Medium
Topics
Companies
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

## Final Solution

```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
            
        if n>0:
            if n==1:
                return x
            elif n%2==0:
                return self.myPow(x**2,n/2)
            elif n%2==1:
                return x*self.myPow(x**2,(n-1)/2)
        
        if n<0:
            n=-n
            x=1/x
            return self.myPow(x,n)
        
            
```

## Tags
#recursion