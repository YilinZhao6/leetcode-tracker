class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        if len(strs)==1:
            return strs[0]
        
        min_length=float('inf')
        #find min length:
        for i in range(len(strs)):
            if len(strs[i])<min_length:
                min_length=len(strs[i])

        first_word=strs[0]
        result=[]

        def check_index(index,char,array):
            for i in range(len(array)):
                if array[i][index]!=char:
                    return False
            
            return True

        i=0
        while i<min_length:
            if check_index(i,first_word[i],strs[1:]):
                result.append(first_word[i])
                i+=1
            else:
                return ''.join(result)
        
        return ''.join(result)

##Simplified Solution

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Find the shortest string in the list (longest prefix can't be longer than this)
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for s in strs:
                if s[i] != char:
                    return shortest[:i]
        
        return shortest
