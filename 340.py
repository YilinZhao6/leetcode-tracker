from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0  # No distinct characters allowed → return 0

        s_list = list(s)
        n = len(s_list)
        
        pt1, pt2 = 0, 0
        counter = defaultdict(int)  # Store character occurrences
        max_length = 0

        while pt2 < n:
            counter[s_list[pt2]] += 1  # Add character to window

            while len(counter) > k:  # More than k distinct → shrink window
                counter[s_list[pt1]] -= 1
                if counter[s_list[pt1]] == 0:
                    del counter[s_list[pt1]]  # Remove character when count reaches 0
                pt1 += 1  # Shrink window
            
            # Track the longest valid substring
            max_length = max(max_length, pt2 - pt1 + 1)

            pt2 += 1  # Expand window

        return max_length
