class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        sort_nums=sorted(nums)
        lengths=[]

        length=1
        for i in range(1,len(sort_nums)):
            if sort_nums[i]==sort_nums[i-1]+1:
                length+=1
            elif sort_nums[i]==sort_nums[i-1]:
                continue
            else:
                lengths.append(length)
                length=1

        lengths.append(length)

        return max(lengths)
