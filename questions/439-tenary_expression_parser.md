# [439]. Tenary Expression Parser

**Status**: [Solved ✅]

**Difficulty**: [Easy]

**Last Attempted**: 2025-01-02

## Problem Statement

Given a string expression representing arbitrarily nested ternary expressions, evaluate the expression, and return the result of it.

You can always assume that the given expression is valid and only contains digits, '?', ':', 'T', and 'F' where 'T' is true and 'F' is false. All the numbers in the expression are one-digit numbers (i.e., in the range [0, 9]).

The conditional expressions group right-to-left (as usual in most languages), and the result of the expression will always evaluate to either a digit, 'T' or 'F'.

```
Example 1:

Input: expression = "T?2:3"
Output: "2"
Explanation: If true, then result is 2; otherwise result is 3.
Example 2:

Input: expression = "F?1:T?4:5"
Output: "4"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(F ? 1 : (T ? 4 : 5))" --> "(F ? 1 : 4)" --> "4"
or "(F ? 1 : (T ? 4 : 5))" --> "(T ? 4 : 5)" --> "4"
Example 3:

Input: expression = "T?T?F:5:3"
Output: "F"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(T ? (T ? F : 5) : 3)" --> "(T ? F : 3)" --> "F"
"(T ? (T ? F : 5) : 3)" --> "(T ? F : 5)" --> "F"
```



## Final Solution

```python
class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        i = len(expression) - 1  # Start from the rightmost character
        
        while i >= 0:
            char = expression[i]
            
            if char.isdigit() or char.isalpha():
                stack.append(char)
            
            elif char == '?':
                # Handle ternary condition
                true_value = stack.pop()
                false_value = stack.pop()
                condition = expression[i - 1]
                
                # Evaluate based on condition
                stack.append(true_value if condition == 'T' else false_value)
                
                # Skip the condition character (T/F)
                i -= 1
            
            # Move to the next character
            i -= 1
        
        return stack[-1]
```

## Tags
#stack