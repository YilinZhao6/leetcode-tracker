class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)

        return heapq.nlargest(k,heap)[-1]