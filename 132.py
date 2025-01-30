#Note: this code could be optimized in runtime.

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)

        def isPalindrome(i,j):
            if i>=j:
                return True
            if s[i]==s[j]:
                return isPalindrome(i+1,j-1)
            else:
                return False

        dp=[[False]*n for i in range(n)]
        for i in range(0,n):
            for j in range(i,n):
                if isPalindrome(i,j):
                    dp[i][j]=True
                else:
                    dp[i][j]=False
        
        #start to fill the dp_result array

        dp_result=[0]*n
        for i in range(n):
            dp_result[i]=i

        for i in range(1,n):
            if dp[0][i]:
                dp_result[i]=0
            #if not palindrome
            else:
                for j in range(i):
                    if dp[j+1][i]:
                        dp_result[i]=min(dp_result[i],dp_result[j]+1)
        
        return dp_result[n-1]
            
                