class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        #create the empty dp array
        dp=[0]*(n+1)

        #base cases
        #ignore dp=[0]
        dp[1]=1
        dp[2]=1

        for i in range(3,n+1):
            for j in range(1,i-1):
                #choose the max out of 2
                # j,i-j
                # j dp[i-j]
                dp[i]=max(dp[i],max(j*(i-j),j*dp[i-j]))
        
        return dp[n]