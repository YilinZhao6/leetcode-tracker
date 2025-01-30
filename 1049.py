class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        #calculate total sum and dp target sum
        total_sum=0
        for stone in stones:
            total_sum+=stone

        #calcualte target sum
        target_sum=total_sum//2

        #create dp array
        dp=[True]+[False]*target_sum

        for stone in stones:
            #calculate reachable numbers:
            for Q in range(target_sum,stone-1,-1):
                dp[Q]=dp[Q] or dp[Q-stone]
        
        #find the dp closest to target_sum
        for i in range(target_sum,-1,-1):
            if dp[i]:
                return total_sum-2*i

        return 0