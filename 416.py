class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums:
            return False

        #calculate total sum
        total_sum=0
        for i in range(len(nums)):
            total_sum+=nums[i]
        
        if total_sum%2==1:
            return False

        dp_target=total_sum//2

        #create dp array (store booleans)
        dp=[True]+[False]*dp_target

        #for each number in array
        for i in range(len(nums)):
            for Q in range(dp_target,nums[i]-1,-1):
                dp[Q]=dp[Q] or dp[Q-nums[i]]

        return dp[dp_target]