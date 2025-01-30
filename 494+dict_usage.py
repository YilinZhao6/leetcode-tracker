class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #intialize dp
        dp={0:1}

        for num in nums:
            new_dp={}
            #need to use .items() to have access to both index and value
            for key, value in dp.items():
                new_dp[key+num]=new_dp.get(key+num,0)+value
                new_dp[key-num]=new_dp.get(key-num,0)+value
            dp=new_dp
            
        return dp.get(target,0)