class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        #create dp array
        dp=[[0]*(n+1) for _ in range(m+1)]

        #for each string, count the number of 0s and 1s:
        def count_zero(string):
            count=0
            for i in range(len(string)):
                if string[i]=='0':
                    count+=1

            return count

        def count_one(string):
            count=0
            for i in range(len(string)):
                if string[i]=='1':
                    count+=1

            return count

        for str in strs:
            zeros=count_zero(str)
            ones=count_one(str)
            for i in range(m,zeros-1,-1):
                for j in range(n,ones-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zeros][j-ones]+1)
        
        return dp[m][n]

            


