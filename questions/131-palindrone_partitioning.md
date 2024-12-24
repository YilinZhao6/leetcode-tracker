# [131]. Palindrome Partitioning

**Status**: [Done ✅]

**Difficulty**: [Medium]

**Last Attempted**: 2024-12-23

## Problem Statement

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

```python
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
```

## Final Solution


```python
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        s_list=list(s)
        def is_palindrome(letters):
            pt_1=0
            pt_2=len(letters)-1
            while pt_1<=pt_2:
                if letters[pt_1]==letters[pt_2]:
                    pt_1+=1
                    pt_2-=1
                else:
                    return False
            
            return True
        
        def backtrack(word_list, selected_words, result):
            # base case: add successful words
            if len(word_list) == 0:
                good_word = []
                for word in selected_words:  # changed from i to word for clarity
                    good_word.append(''.join(word))
                result.append(good_word)
                return
            
            word = []
            for i in range(len(word_list)):
                word.append(word_list[i])
                if is_palindrome(word):
                    selected_words.append(word[:])  # make a copy of word
                    # remove elements from word_list - here's the implementation:
                    remaining_list = word_list[i+1:]
                    backtrack(remaining_list, selected_words, result)
                    selected_words.pop()

        result=[]
        backtrack(s_list,[],result)
        return result

```

### Solution Explanation

## Previous Attempts

<details>
<summary>Attempt 1 - Failed ❌</summary>


</details>

## Notes
NULL
## Tags
#backtracking